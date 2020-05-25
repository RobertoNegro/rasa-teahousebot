import json
import os
import pickle
import re

from pprint import pprint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import pandas as pd

GLOBAL_TEA_CATEGORY_ID = 348


def get_categories_and_filters(driver, lang='EN'):
    categories = dict()
    filters = dict()

    link = f'https://www.peters-teahouse.it/home/changeLanguage?lang={lang}&returnUrl=/category/{GLOBAL_TEA_CATEGORY_ID}/tea'
    print(f'Navigating to {link}')
    driver.get(link)

    filter_els = driver.find_elements_by_css_selector('.filtri-gruppo')
    for filter_el in filter_els:
        category_link_els = filter_el.find_elements_by_css_selector('a.filtri-singolo')
        for category_link_el in category_link_els:
            name = category_link_el.get_attribute('innerText').strip()
            link = category_link_el.get_attribute('href').strip()

            if len(name) > 0:
                query_params_split = link.split('?', 1)
                if len(query_params_split) > 1:
                    tags = query_params_split[1].split('&')
                    for t in tags:
                        t_splitted = t.split('=')
                        if len(t_splitted) > 1:
                            t_id = t_splitted[0].strip()
                            t_value = t_splitted[1].strip()
                            if t_id not in filters:
                                filters[t_id] = dict()
                            filters[t_id][t_value] = name
                else:
                    category_id_search = re.search(r'category/(\d+)/', link, re.IGNORECASE)
                    if category_id_search:
                        category_id = category_id_search.group(1).strip()
                        if category_id != str(GLOBAL_TEA_CATEGORY_ID):
                            categories[category_id] = name

    return categories, filters


def get_all_products(driver):
    return get_products(driver, GLOBAL_TEA_CATEGORY_ID)


def get_products(driver, category, filters=None):
    products = dict()

    link = f'https://www.peters-teahouse.it/category/{category}/tea?showAll=True'
    if filters is not None:
        for filter_id, filter_value in filters:
            link = link + '&' + str(filter_id) + '=' + str(filter_value)
    print(f'Navigating to {link}')
    driver.get(link)

    try:
        product_els = driver.find_elements_by_css_selector('.nomeProdotto a')
    except NoSuchElementException:
        return products

    for product_el in product_els:
        name = product_el.get_attribute('innerText')
        link = product_el.get_attribute('href')

        if len(name.strip()) > 0:
            product = dict()

            product_id_search = re.search(r'product/(\d+)/', link, re.IGNORECASE)
            if product_id_search:
                product_id = product_id_search.group(1).strip()
                if len(product_id) > 0:
                    if category != GLOBAL_TEA_CATEGORY_ID:
                        product['category'] = category
                    if filters is not None:
                        for filter_id, filter_value in filters:
                            product[filter_id] = filter_value
                    products[product_id] = product

    return products


def get_try(driver, selector, attribute, default='N.A.'):
    try:
        val = driver.find_element_by_css_selector(selector).get_attribute(attribute)
    except NoSuchElementException:
        val = default
    return val


def get_product_details(driver, product_id, lang='EN'):
    product = dict()

    link = f'https://www.peters-teahouse.it/home/changeLanguage?lang={lang}&returnUrl=/product/{product_id}/tea'
    print(f'Navigating to {link}')
    driver.get(link)

    name = get_try(driver, 'h1[itemprop="name"]', 'innerText')
    image = get_try(driver, 'img[itemprop="image"]', 'src')
    brand = get_try(driver, 'div[itemprop="brand"]', 'content')
    price = float(get_try(driver, 'span[itemprop="price"]', 'innerText'))
    price_currency = get_try(driver, 'span[itemprop="priceCurrency"]', 'content')
    description = get_try(driver, 'div[itemprop="description"] > div', 'innerText')
    ingredients = get_try(driver, '.prodDescBlock .row > div:not([itemprop]) > div', 'innerText')
    teaspons = get_try(driver, '.CUC-INO', 'innerText')
    temperature = get_try(driver, '.TEMP', 'innerText')
    time = get_try(driver, '.TINF', 'innerText')

    similar_to = []
    similar_to_els = driver.find_elements_by_css_selector('.prodottoConsigli .nomeProdotto a')
    for similar_to_el in similar_to_els:
        link = similar_to_el.get_attribute('href')
        product_id_search = re.search(r'product/(\d+)/', link, re.IGNORECASE)
        if product_id_search:
            product_id = product_id_search.group(1).strip()
            if len(product_id) > 0:
                similar_to.append(product_id)

    product['name'] = name
    product['image'] = image
    product['brand'] = brand
    product['price'] = price
    product['price_currency'] = price_currency
    product['description'] = description
    product['ingredients'] = ingredients
    product['teaspons'] = teaspons
    product['temperature'] = temperature
    product['time'] = time
    product['similar_to'] = similar_to

    return product


def main():
    use_cache = True

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # no images
    options.add_experimental_option('prefs', {
        'profile.managed_default_content_settings.images': 2,
        'profile.default_content_setting_values.images': 2
    })

    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

    if use_cache and os.path.exists('cache/categories.pickle') and os.path.exists('cache/filters.pickle'):
        with open('cache/categories.pickle', 'rb') as f:
            categories = pickle.load(f)
        with open('cache/filters.pickle', 'rb') as f:
            filters = pickle.load(f)
    else:
        categories, filters = get_categories_and_filters(driver)
        with open('cache/categories.pickle', 'wb') as f:
            pickle.dump(categories, f)
        with open('cache/filters.pickle', 'wb') as f:
            pickle.dump(filters, f)

    print('Categories:')
    pprint(categories)
    print('Filters:')
    pprint(filters)

    if use_cache and os.path.exists('cache/all_products.pickle'):
        with open('cache/all_products.pickle', 'rb') as f:
            products = pickle.load(f)
    else:
        products = get_all_products(driver)
        with open('cache/all_products.pickle', 'wb') as f:
            pickle.dump(products, f)

    print('All products:')
    pprint(products)

    print('Getting products details:')
    for product_id in products:
        if use_cache and os.path.exists(f'cache/product_detail/{product_id}.pickle'):
            with open(f'cache/product_detail/{product_id}.pickle', 'rb') as f:
                product_details = pickle.load(f)
        else:
            product_details = get_product_details(driver, product_id)
            with open(f'cache/product_detail/{product_id}.pickle', 'wb') as f:
                pickle.dump(product_details, f)
        products[product_id].update(product_details)
        pprint(products[product_id])

    print('Getting by category...')
    for index, category_id in enumerate(categories):
        print(f'Checking category {category_id}... ({index + 1}/{len(categories)})')
        if use_cache and os.path.exists(f'cache/products_by_category/{category_id}.pickle'):
            with open(f'cache/products_by_category/{category_id}.pickle', 'rb') as f:
                products_by_category = pickle.load(f)
        else:
            products_by_category = get_products(driver, category_id)
            with open(f'cache/products_by_category/{category_id}.pickle', 'wb') as f:
                pickle.dump(products_by_category, f)
        for product_index, product_id in enumerate(products_by_category):
            print(f'Updating product {product_id}... ({product_index + 1}/{len(products_by_category)})')
            if product_id in products:
                products[product_id].update(products_by_category[product_id])
            else:
                print(f'The product {product_id} was not in the "all-products" page')
                products[product_id] = products_by_category[product_id]
                if use_cache and os.path.exists(f'cache/product_detail/{product_id}.pickle'):
                    with open(f'cache/product_detail/{product_id}.pickle', 'rb') as f:
                        product_details = pickle.load(f)
                else:
                    product_details = get_product_details(driver, product_id)
                    with open(f'cache/product_detail/{product_id}.pickle', 'wb') as f:
                        pickle.dump(product_details, f)
                products[product_id].update(product_details)

    print('Getting by filter...')
    for index, filter_id in enumerate(filters):
        print(f'Checking filter {filter_id}... ({index + 1}/{len(filters)})')
        for value_index, filter_value in enumerate(filters[filter_id]):
            print(
                f'Checking filter {filter_id} with value {filter_value}... ({value_index + 1}/{len(filters[filter_id])})')

            if use_cache and os.path.exists(f'cache/products_by_filter/{filter_id}_{filter_value}.pickle'):
                with open(f'cache/products_by_filter/{filter_id}_{filter_value}.pickle', 'rb') as f:
                    products_by_filter = pickle.load(f)
            else:
                products_by_filter = get_products(driver, GLOBAL_TEA_CATEGORY_ID, [(filter_id, filter_value)])
                with open(f'cache/products_by_filter/{filter_id}_{filter_value}.pickle', 'wb') as f:
                    pickle.dump(products_by_filter, f)
            for product_index, product_id in enumerate(products_by_filter):
                print(f'Updating product {product_id}... ({product_index + 1}/{len(products_by_filter)})')
                if product_id in products:
                    products[product_id].update(products_by_filter[product_id])
                else:
                    print(f'The product {product_id} was not in the "all-products" page')
                    products[product_id] = products_by_filter[product_id]
                    if use_cache and os.path.exists(f'cache/product_detail/{product_id}.pickle'):
                        with open(f'cache/product_detail/{product_id}.pickle', 'rb') as f:
                            product_details = pickle.load(f)
                    else:
                        product_details = get_product_details(driver, product_id)
                        with open(f'cache/product_detail/{product_id}.pickle', 'wb') as f:
                            pickle.dump(product_details, f)
                    products[product_id].update(product_details)

    print('Getting filters by category...')
    for category_index, category_id in enumerate(categories):
        print(f'Checking filters in category {category_id}... ({category_index + 1}/{len(categories)})')
        for filter_index, filter_id in enumerate(filters):
            print(f'Checking filter {filter_id}... ({filter_index + 1}/{len(filters)})')
            for value_index, filter_value in enumerate(filters[filter_id]):
                print(f'Checking filter {filter_id} with value {filter_value}... ({value_index + 1}/{len(filters[filter_id])})')
                if use_cache and os.path.exists(f'cache/products_by_category_and_filter/{category_id}_{filter_id}_{filter_value}.pickle'):
                    with open(f'cache/products_by_category_and_filter/{category_id}_{filter_id}_{filter_value}.pickle', 'rb') as f:
                        products_by_category_and_filter = pickle.load(f)
                else:
                    products_by_category_and_filter = get_products(driver, category_id, [(filter_id, filter_value)])
                    with open(f'cache/products_by_category_and_filter/{category_id}_{filter_id}_{filter_value}.pickle', 'wb') as f:
                        pickle.dump(products_by_filter, f)

                for product_index, product_id in enumerate(products_by_category_and_filter):
                    print(f'Updating product {product_id}... ({product_index + 1}/{len(products_by_category_and_filter)})')
                    if product_id in products:
                        products[product_id].update(products_by_category_and_filter[product_id])
                    else:
                        print(f'The product {product_id} was not in the "all-products" page')
                        products[product_id] = products_by_category_and_filter[product_id]
                        if use_cache and os.path.exists(f'cache/product_detail/{product_id}.pickle'):
                            with open(f'cache/product_detail/{product_id}.pickle', 'rb') as f:
                                product_details = pickle.load(f)
                        else:
                            product_details = get_product_details(driver, product_id)
                            with open(f'cache/product_detail/{product_id}.pickle', 'wb') as f:
                                pickle.dump(product_details, f)
                        products[product_id].update(product_details)

    with open(f'products.json', 'w') as f:
        f.write(json.dumps(products, indent=2))

    with open(f'categories.json', 'w') as f:
        f.write(json.dumps(categories, indent=2))

    f_filters = dict()
    for id in filters:
        for value in filters[id]:
            f_filters[str(id) + '=' + str(value)] = filters[id][value]
    with open(f'filters.json', 'w') as f:
        f.write(json.dumps(f_filters, indent=2))

    with open(f'dict_filters.json', 'w') as f:
        f.write(json.dumps(filters, indent=2))

    with open(f'products_name.list', 'w') as f:
        for p_id in products:
            f.write(products[p_id]['name'] + '\n')

    driver.close()


if __name__ == '__main__':
    main()
