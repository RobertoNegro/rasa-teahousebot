from math import ceil
from random import randint

sanitize = lambda s: ('"' + s + '"' if type(s) == str else str(s)) if str(s) != 'null' else 'null'


def get_unfeat_search_settings(category, origin, organic, christmas, availability, new, offset):
    return '- slot{"unfeat_search_settings": [' + sanitize(category) + ', ' + sanitize(origin) + ', ' + sanitize(
        organic) + ', ' + sanitize(christmas) + ', ' + sanitize(availability) + ', ' + sanitize(new) + ', ' + sanitize(
        offset) + ']}\n'


def get_filters_seq(origin, organic, christmas, availability, new):
    seq = ''
    if origin != 'null':
        seq += ', "origin": ' + sanitize(origin)
    if organic != 'null':
        seq += ', "organic": ' + sanitize(organic)
    if christmas != 'null':
        seq += ', "christmas": ' + sanitize(christmas)
    if availability != 'null':
        seq += ', "availability": ' + sanitize(availability)
    if new != 'null':
        seq += ', "new": ' + sanitize(new)
    return seq[2:]


greet = lambda: (
        '* greet\n' +
        '- action_deactivate_form\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_greet\n' +
        '- utter_how_can_i_help_you\n'
)

bye = lambda: (
        '* goodbye\n' +
        '- action_deactivate_form\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_goodbye\n'
)

thanks = lambda: (
        '* thanks\n' +
        '- utter_thanks\n'
)

thanks_bye = lambda: (
        '* thanks_goodbye\n' +
        '- action_deactivate_form\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_thanks_goodbye\n'
)

search_affirm = lambda category, origin, organic, christmas, availability, new, offset: (
        '* search_affirm\n' +
        '- action_suggest\n' +
        '- slot{"name": null}\n' +
        '- slot{"unfeat_name_cardinal": []}\n' +
        get_unfeat_search_settings(category, origin, organic, christmas, availability, new, offset)
)

search_deny = lambda first_time: (
        ('* form: ' if not first_time else '* ') + 'search_deny\n' +
        '- followup{"name": "action_clear_form"}\n' +
        '- action_clear_form\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n'
)

search_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'search\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_search\n' +
        '- form{"name": "form_action_search"}\n' +
        '- slot{"requested_slot": "category"}\n'
)

search_unknown = lambda first_time, category: (
        ('* form: ' if not first_time else '* ') +
        'search{"category": "' + category + '"}\n' +
        '- slot{"category": "' + category + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_search\n' +
        '- slot{"category": null}\n' +
        '- slot{"requested_slot": "category"}\n'
)

tea_name = lambda first_time, name: (
         ('* form: ' if not first_time else '* ') + 'tea_name{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n'
)

cardinal = lambda first_time, cardinal, name, form: (
        '* cardinal{"cardinal": "' + cardinal + '"}\n' +
        '- slot{"cardinal": "' + cardinal + '"}\n' +
        '- action_extract_name_from_cardinal\n' +
        '- slot{"cardinal": null}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form: followup{"name": "form_action_' + form + '"}\n' if not first_time else ''
)

cardinal_no_match = lambda first_time, cardinal, form: (
        ('* form: ' if not first_time else '* ') + 'cardinal{"cardinal": "' + cardinal + '"}\n' +
        '- slot{"cardinal": "' + cardinal + '"}\n' +
        '- action_extract_name_from_cardinal\n' +
        '- slot{"cardinal": null}\n' +
        '- slot{"name": null}\n' +
        '- form: followup{"name": "form_action_' + form + '"}\n' if not first_time else ''
)

search = lambda first_time, category: (
        ('* form: ' if not first_time else '* ') +
        'search{"category": "' + category + '"}\n' +
        '- slot{"category": "' + category + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_search\n' +
        ('- form{"name": "form_action_search"}\n' if first_time else '') +
        '- slot{"category": "' + category + '"}\n' +
        '- slot{"category": null}\n' +
        '- slot{"origin": null}\n' +
        '- slot{"organic": null}\n' +
        '- slot{"christmas": null}\n' +
        '- slot{"availability": null}\n' +
        '- slot{"new": null}\n' +
        '- slot{"name": null}\n' +
        '- slot{"cardinal": null}\n' +
        '- slot{"unfeat_name_cardinal": null}\n' +
        get_unfeat_search_settings(category, "null", "null", "null", "null", "null", 0) +
        '- form: followup{"name": "action_suggest"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- action_suggest\n' +
        '- slot{"name": null}\n' +
        '- slot{"unfeat_name_cardinal": []}\n' +
        get_unfeat_search_settings(category, "null", "null", "null", "null", "null", 5)
)

filter = lambda category, origin, organic, christmas, availability, new: (
        '* filter{' + get_filters_seq(origin, organic, christmas, availability, new) + '}\n' +
        '- slot{' + get_filters_seq(origin, organic, christmas, availability, new) + '}\n' +
        '- action_filter\n' +
        '- slot{"origin": null}\n' +
        '- slot{"organic": null}\n' +
        '- slot{"christmas": null}\n' +
        '- slot{"availability": null}\n' +
        '- slot{"new": null}\n' +
        '- slot{"name": null}\n' +
        '- slot{"cardinal": null}\n' +
        '- slot{"unfeat_name_cardinal": null}\n' +
        get_unfeat_search_settings(category, origin, organic, christmas, availability, new, 0) +
        ((
                 '- followup{"name": "action_suggest"}\n' +
                 '- action_suggest\n' +
                 '- slot{"name": null}\n' +
                 '- slot{"unfeat_name_cardinal": []}\n' +
                 get_unfeat_search_settings(category, origin, organic, christmas, availability, new, 5)
         ) if category != 'null' else (
                '- followup{"name": "form_action_search"}\n' +
                '- form_action_search\n' +
                '- form{"name": "form_action_search"}\n' +
                '- slot{"requested_slot": "category"}\n'
        ))
)


def by_name_types(event_type):
    empty = lambda first_time: (
            ('* form: ' if not first_time else '* ') +
            '' + event_type + '\n' +
            ('- form: ' if not first_time else '- ') + 'form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"requested_slot": "name"}\n'
    )

    unknown = lambda first_time, name: (
            ('* form: ' if not first_time else '* ') +
            '' + event_type + '{"name": "' + name + '"}\n' +
            '- slot{"name": "' + name + '"}\n' +
            ('- form: ' if not first_time else '- ') + 'form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"name": null}\n' +
            '- slot{"requested_slot": "name"}\n'
    )

    valid = lambda first_time, name: (
            ('* form: ' if not first_time else '* ') +
            '' + event_type + '{"name": "' + name + '"}\n' +
            '- slot{"name": "' + name + '"}\n' +
            ('- form: ' if not first_time else '- ') + 'form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"name": "' + name + '"}\n' +
            '- form{"name": null}\n' +
            '- slot{"requested_slot": null}\n' +
            '- utter_can_i_help_you_again\n'
    )

    multiple_choices = lambda first_time, name: (
            ('* form: ' if not first_time else '* ') + '' + event_type + '{"name": "' + name[:len(name) // 2] + '"}\n' +
            '- slot{"name": "' + name[:len(name) // 2] + '"}\n' +
            ('- form: ' if not first_time else '- ') + 'form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"name": "' + name[:len(name) // 2] + '"}\n' +
            '- slot{"unfeat_name_cardinal": []}\n' +
            '- slot{"name": null}\n' +
            '- form: followup{"name": "form_action_' + event_type + '"}\n' +
            '- form{"name": null}\n' +
            '- slot{"requested_slot": null}\n' +
            '- form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"requested_slot": "name"}\n'
    )

    with_cardinal = lambda first_time, cardinal, name: (
            ('* form: ' if not first_time else '* ') + event_type + '{"cardinal": "' + cardinal + '"}\n' +
            '- slot{"cardinal": "' + cardinal + '"}\n' +
            '- form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"name": "' + name + '"}\n' +
            '- slot{"cardinal": null}\n' +
            '- form: followup{"name": "form_action_' + event_type + '"}\n' +
            '- form: form_action_' + event_type + '\n' +
            '- form{"name": null}\n' +
            '- slot{"requested_slot": null}\n' +
            '- utter_can_i_help_you_again\n'
    )

    prev = lambda first_time, name: (
            ('* form: ' if not first_time else '* ') + '' + event_type + '\n' +
            '- form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"name": "' + name + '"}\n' +
            '- form{"name": null}\n' +
            '- slot{"requested_slot": null}\n' +
            '- utter_can_i_help_you_again\n'
    )

    deny = lambda first_time: (
            ('* form: ' if not first_time else '* ') + 'search_deny\n' +
            '- action_deactivate_form\n' +
            '- form{"name": null}\n' +
            '- slot{"requested_slot": null}\n' +
            '- utter_can_i_help_you_again\n'
    )

    cardinal_reask = lambda first_time: (
            ('- form: ' if not first_time else '- ') + 'form_action_' + event_type + '\n' +
            '- form{"name": "form_action_' + event_type + '"}\n' +
            '- slot{"name": null}\n' +
            '- slot{"requested_slot": "name"}\n'
    )

    cardinal_confirm = lambda first_time, name: (
            ('- form: ' if not first_time else '- ') + 'form_action_' + event_type + '\n' +
            '- form{"name": null}\n' +
            '- slot{"requested_slot": null}\n' +
            '- utter_can_i_help_you_again\n'
    )

    return empty, unknown, valid, multiple_choices, with_cardinal, prev, deny, cardinal_reask, cardinal_confirm


values_category = ["Black Teas", "Oolong", "White Teas", "Gold Tea Selection", "Fruit Infusions", "Rooibos",
                   "Herbal Teas",
                   "Matcha and Flower Teas"]

values_new = ["New"]
values_organic = ["Organic", "Not organic"]
values_christmas = ["Christmas", "Not christmas"]
values_origin = ["Ceylon", "China", "India", "Taiwan", "Korea", "Tanzania", "South africa"]
values_availability = ["Available", "Not available"]
values_cardinal = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
values_invalid_cardinal = ['11', '12', '13', '14', '15', '-1', '-2', '-3', '-4', '-5', '0']

products = ['Amarettino Black Tea', 'Assam BPS Typhoo Black Tea', 'Assam Exquisite TGFOP Black Tea',
            'Assam Genteel FTGFOP Black Tea', 'Assam Goldtips TGFOP Black Tea', 'Assam TGFOP Satrupa Organic Black Tea',
            'Ayurveda Relax Herbal Tea', 'Bancha Green Tea', 'Beauty Herbal Tea', 'Bergamino Black Tea',
            'Bitter Orange Black Tea', 'Body and Soul Herbal Tea', 'Caramel Black Tea', 'Ceylon Curl Green Green Tea',
            'Ceylon OP1 Pettiagalla Black Tea', 'Ceylon Orange Pekoe Blend Black Tea', 'Chamomile Herbal Tea',
            'Chamomile Organic Herbal Tea', 'China Keemun Black Tea', 'China Milky Oolong', 'China Rose Black Tea',
            'China Yunnan Pu Erh Black Tea', 'Chocolate Black Tea', 'Christmas Dream Black Tea', 'Chun Mee Green Tea',
            'Cinnamon Punch Fruit Infusion', 'Cocoa and Dates Fruit Infusion', 'Coconut Kiss Fruit Infusion',
            'Copacabana Fruit Infusion', 'Corea OP Jeju Green Tea Bio', 'Cranberry Queen Fruit Infusion',
            'Darjeeling Earl Grey Green Tea', 'Darjeeling First Flush TGFOP Black Tea',
            'Darjeeling Gold GFOP Black Tea', 'Darjeeling Green Risheehat Green Tea', 'Darjeeling Himalaya Black Tea',
            'Darjeeling Margaret\'s Hope Black Tea', 'Darjeeling Standard FOP Black Tea', 'Delicious Herbal Tea',
            'Depurapiù Herbal Tea', 'Dimbula OP Black Tea', 'Earl Green Green Tee', 'Earl Grey Black Tea',
            'Earl Grey Lady Blue Black Tea', 'Earl Grey Special Soft Black Tea (without thein)',
            'Elisir Aloe Vera Herbal Tea FES', 'English Breakfast Black Tea',
            'English Breakfast Soft Black Tea (without thein)', 'English Rose Black Tea', 'Exotic Harmony Green Tea',
            'Fennel Herbal Tea', 'Forest Gifts Herbal Tea', 'Garden Eden Fruit Infusion', 'Genmaicha Green Tea',
            'Ginger Green Tea', 'Goji Berry Green Tea', 'Golden Yunnan Black Tea', 'Good Evening Herbal Tea',
            'Good Luck Charm Fruit Infusion', 'Greek Mountain Herbal Tea', 'Green Forest Green Tea',
            'Green Manjolai Organic Green Tea', 'Green Rooibos Classic', 'Green Rooibos Peach',
            'Green Rooibos Vanilla and Lemon', 'Gunpowder Menthos Green Tea', 'Gunpowder Temple of Heaven Green Tea',
            'Gyokuro Green Tea', 'Happy Fruits Fruit Infusion', 'Hawaii Cocktail Fruit Infusion',
            'Herbal Dreams Herbal Tea', 'Hibiscus Flower Herbal Tea', 'Highland Toffee Black Tea',
            'Ice Crystal Green Tea', 'Indian Chai Organic Black Tea', 'Indian Ocean Black Tea',
            'Irish Breakfast Black Tea', 'Japan Shincha Organic Green Tea', 'Japanese Cherry Green Tea',
            'Jasmine Green Tea', 'Jasmine Pearl White Tea', 'Jun Shan Silver Needle White Tea',
            'Kashmir Chai Walla Green Tea', 'Kenya GFOP Tinderet Black Tea', 'Kimono Green Tea',
            'Korakundah FOP Organic Green Tea', 'Kukicha Green Tea', 'Lady Camilla Herbal Tea', 'Lapacho FES',
            'Lapsang Souchong Crocodile Black Tea', 'Lemongrass organic Black Tea',
            'Lightness from the Forest Fruit Infusion', 'Lightness Herbal Tea', 'Liquorice Black Tea',
            'Little Red Riding Hood Fruit Infusion', 'Lung Ching Green Tea', 'Lung Ching Superior Green Tea',
            'Magic Relax Herbal Tea', 'Mallowflowers Herbal Tea', 'Mandarin Organic Green Tea',
            'Mango Tropical Fruit Infusion', 'Maori Dance Black Tea', 'Marrakech Organic Green Mint Tea',
            'Matcha Asahi Green Tea Powder Ceremonial 40g', 'Matcha Haruka Green Tea Powder 100g',
            'Meditation Herbal Tea', 'Mediterranean Herbal Tea', 'Merry Christmas Black Tea',
            'Mini Tuocha China Pu Erh Black Tea', 'Mint Ginger Freshness Herbal Tea', 'Mon Amour Fruit Infusion',
            'Moringa Life Tree Herbal Tea', 'Mu Herbal Tea FES', 'Mulled Wine Spices', 'Nana Mint Herbal Tea',
            'Nilgiri FOP Oothu Organic Black Tea', 'Oolong Se Chung', 'Open Fire Fruit Infusion',
            'Orange Ginger Fruit Infusion', 'Orange Poem Fruit Infusion', 'Organic Spring Herbal Tea',
            'Orient Rose Green Tea', 'Pagoda Summer Fruit Infusion', 'Pai Mu Tan White Tea BIO',
            'Peppermint Herbal Tea', 'Pi Lou Chun Dong Ting Green Tea', 'Pink Summer Green Tea',
            'Pomegranate Fruit Infusion', 'Pressed Green Tea Heart', 'Pressed Green Tea Star',
            'Princess Sissi Black Tea', 'Red Passion Fruit Infusion', 'Rooibos African Chai', 'Rooibos Almond',
            'Rooibos Chocolate', 'Rooibos Classic', 'Rooibos Flower Dance', 'Rooibos Lemon', 'Rooibos Orange',
            'Rooibos Orange and Carrot', 'Rooibos Orange and Mint', 'Rooibos Papaya and Cinnamon',
            'Rooibos Passion Fruit', 'Rooibos Vanilla', 'Rooibos Wild Berry', 'Santa Claus Fruit Infusion',
            'Sencha Kyoto Green Tea', 'Sencha Organic Green Tea', 'Sikkim - Piantagione Temi Black Tea',
            'Silk Road Green Tea', 'Slim Plus Herbal Tea', 'Soft Berries Cocktail Fruit Infusion',
            'Souvenir de Printemps', 'Special Golden Yunnan Spiral Black Tea', 'Spicy Lemon Green Tea',
            'Spring Harmony White Tea BIO', 'Sun of the East Green Tea', 'Sweet & Spicy Organic Herbal Tea',
            'Sweet Christmas Fruit Infusion', 'Sweet Dreams Herbal Tea', 'Sweet Lemon Fruit Infusion',
            'Sweet Symphony Fruit Infusion', 'Tanzania GFOP Luponde Organic Green Tea', 'Tea & Spices Black Tea',
            'Tea Brick Compressed Black Tea FES', 'Teaflower Casanova Black Tea', 'Teaflower Monte Bianco White Tea',
            'Teaflower Moulin Rouge Black Tea', 'Teaflower Orient Flame Black Tea', 'Teaflower Sunshine White Tea',
            'Thousand and One Night Fruit Infusion', 'Tibetan Monks\' Black Tea', 'Turkish Apple Fruit Infusion',
            'Vanilla Bourbon Black Tea', 'Violet White Tea', 'Vitality Herbal Tea', 'Walnut Oolong Tea',
            'Wellness Herbal Tea', 'White Bud Organic White Tea', 'White Dragon Organic White Tea BIO',
            'White Peony Organic White Tea', 'Wild Berry Black Tea', 'Wild Berry Fruit Infusion',
            'Winter Fairytale Fruit Infusion', 'Winter Green Tea', 'Winter Magic Black Tea',
            'Wuyuan Jasmin Organic Green Tea', 'Yamamoto Green Tea', 'Yellow Emperor Green Tea', 'Yunnan Green Tea',
            'Apple Strudel Black Tea', 'Golden Nepal Maloom Black Tea Bio', 'Mandarine and Cinnamon Black Tea',
            'Nuwara Eliya FOP Black Tea', 'Perfumes of Lavender Black Tea BIO', 'Pu Erh Vaniglia and Caramel Black Tea',
            'Russian Caravan Black Tea mixture', 'Rwanda Rukeri Black tea', 'Strawberry Cream Black Tea',
            'Thai Black Tea black tea', 'Turmeric Power Black Tea', 'Caribbean Oolong', 'Dong Ding Oolong',
            'China Hojicha Green Tea', 'Curcuma and Ginger green tea', 'Green Breakfsat Bio green Tea',
            'Green Tea Peach', 'Honeymoon Green Tea BIO', 'Indonesia Java OP Green Tea BIO', 'Kabusecha Green Tea',
            'Matcha green Tea Roses', 'Starsdust Green Tea Limited Edition', 'White Green Monkey Green Tea',
            'Exotic Dream white tea', 'Himalaya White Tea', 'Anji White White Tea', 'Ceylon St. James Black tea',
            'Nepal Jun Chiyabari Oolong BIO', 'Fresh Peach Fruit Infusion', 'Magical Christmas fruit infusion',
            'Mandarine Dream Fruit Infusion', 'Melon Splash Fruit Infusion', 'Pepita Fruit Infusion FES',
            'Pura Vida Fruit Infusion', 'Sparks of Joy Fruit Infusion', 'Tropical Moringa Fruit Infusion',
            'Tropical Paradise fruit Infusion Bio', 'Turmeric and vanilla fruit Infusion', 'Rooibos Caramel',
            'Rooibos ginger', 'Rooibos Wild Pure', 'Cumin Mint Herbal Tea FES', 'Greek Mountain Orange Herbal Tea Bio',
            'Green Mate Herbal Tea', 'Lavender and Chamomile Herbal Tea', 'Magic Mountain Herbal Tea Bio',
            'Melissa Herbal Tea FES', 'Matcha for Cooking Green Tea Powder 20g',
            'Matcha-Genmaicha Instant Green Tea BIO 50g', 'Matcha-Kukicha Instant Green Tea BIO 50g']


def prob(perc):
    return randint(0, 99) < perc


def split_prob(n):
    p_each = ceil(100 / n)
    v = randint(0, 99)
    for i in range(0, n):
        if v < p_each * (i + 1):
            return i


def affirm_sequence(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability, cur_new):
    res = ''
    if prob(50):
        n_affirm = 1
    else:
        if prob(75):
            n_affirm = 0
        else:
            n_affirm = randint(2, 3)

    offset = 10
    for j in range(0, n_affirm):
        res += search_affirm(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability, cur_new, offset)
        offset += 5

    if prob(75):
        res += search_deny(True)
    return res


def set_filters_sequence(cur_origin, cur_organic, cur_christmas, cur_availability, cur_new):
    if prob(75):
        n_filters = 1
    else:
        if prob(75):
            n_filters = 2
        else:
            n_filters = 3
    for _ in range(0, n_filters):
        filter_type = split_prob(5)
        if filter_type == 0:
            cur_origin = values_origin[randint(0, len(values_origin) - 1)]
        elif filter_type == 1:
            cur_organic = values_organic[randint(0, len(values_organic) - 1)]
        elif filter_type == 2:
            cur_christmas = values_christmas[randint(0, len(values_christmas) - 1)]
        elif filter_type == 3:
            cur_availability = values_availability[randint(0, len(values_availability) - 1)]
        elif filter_type == 4:
            cur_new = values_new[randint(0, len(values_new) - 1)]
    return cur_origin, cur_organic, cur_christmas, cur_availability, cur_new


def produce_stories(n):
    res = ''
    for story_index in range(1, n + 1):
        res += f'## story {story_index}\n'
        if prob(75):
            res += greet()

        name_set = None
        cur_category = 'null'
        cur_origin = 'null'
        cur_organic = 'null'
        cur_christmas = 'null'
        cur_availability = 'null'
        cur_new = 'null'

        is_cardinal_possible = False
        is_filter_asking_for_category = False

        if prob(50):
            n_elements = 1
        else:
            if prob(50):
                n_elements = 2
            else:
                if prob(50):
                    n_elements = 3
                else:
                    n_elements = 4

        for _ in range(0, n_elements):
            if _ > 0:
                if prob(10):
                    res += thanks()

            sp = split_prob(3)
            if sp == 0:
                name_set = None
                cur_category = 'null'
                cur_origin = 'null'
                cur_organic = 'null'
                cur_christmas = 'null'
                cur_availability = 'null'
                cur_new = 'null'
                is_cardinal_possible = False

                if prob(75):
                    max_rep = 0
                else:
                    max_rep = randint(1, 2)

                for i in range(0, max_rep):
                    if prob(50):
                        res += search_unknown(not is_filter_asking_for_category and i == 0, 'unknown')
                    else:
                        res += search_empty(not is_filter_asking_for_category and i == 0)

                if max_rep == 0 or prob(75):
                    cur_category = values_category[randint(0, len(values_category) - 1)]
                    res += search(not is_filter_asking_for_category and max_rep == 0, cur_category)
                    is_cardinal_possible = True
                    res += affirm_sequence(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability,
                                           cur_new)
                    is_filter_asking_for_category = False
                else:
                    if prob(75):
                        res += search_deny(False)
            elif sp == 1:
                name_set = None
                cur_origin, cur_organic, cur_christmas, cur_availability, cur_new = set_filters_sequence(cur_origin,
                                                                                                         cur_organic,
                                                                                                         cur_christmas,
                                                                                                         cur_availability,
                                                                                                         cur_new)
                res += filter(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability, cur_new)
                if cur_category == 'null':
                    is_cardinal_possible = False
                    is_filter_asking_for_category = True
                else:
                    is_cardinal_possible = True
                    res += affirm_sequence(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability,
                                           cur_new)
            elif sp == 2:
                # details, preparations, ingredients, cost, availability, similar_products
                def by_name(form_name, is_cardinal_possible, name_set, functs):
                    res = ''
                    empty, unknown, valid, multiple_choices, with_cardinal, prev, deny, cardinal_reask, cardinal_confirm = functs

                    if name_set is None or prob(33):
                        if prob(50):
                            n_pre = 0
                        else:
                            n_pre = randint(1, 2)
                        for i in range(0, n_pre):
                            if i == 0:
                                res += unknown(i == 0, 'unknown')
                            else:
                                if prob(50):
                                    res += unknown(i == 0, 'unknown')
                                else:
                                    res += empty(i == 0)
                        if n_pre > 0 and prob(75):
                            res += deny(n_pre == 0)
                        else:
                            name_set = products[randint(0, len(products) - 1)]

                            if is_cardinal_possible:
                                if n_pre > 0:
                                    type_of_reply = split_prob(4)
                                    if type_of_reply == 0:
                                        res += multiple_choices(n_pre == 0, name_set)
                                        is_cardinal_possible = True
                                        if prob(25):
                                            res += cardinal_no_match(False, values_invalid_cardinal[
                                                randint(0, len(values_invalid_cardinal) - 1)], form_name)
                                            res += cardinal_reask(True)
                                        res += cardinal(False, values_cardinal[randint(0, len(values_cardinal) - 1)],
                                                        name_set, form_name)
                                        res += cardinal_confirm(True, name_set)
                                    elif type_of_reply == 1:
                                        res += valid(n_pre == 0, name_set)
                                    elif type_of_reply == 2:
                                        res += tea_name(False, name_set)
                                        res += cardinal_confirm(False, name_set)
                                    else:
                                        res += with_cardinal(n_pre == 0,
                                                             values_cardinal[randint(0, len(values_cardinal) - 1)],
                                                             name_set)
                                else:
                                    type_of_reply = split_prob(3)
                                    if type_of_reply == 0:
                                        res += multiple_choices(n_pre == 0, name_set)
                                        is_cardinal_possible = True
                                        if prob(25):
                                            res += cardinal_no_match(False, values_invalid_cardinal[
                                                randint(0, len(values_invalid_cardinal) - 1)], form_name)
                                            res += cardinal_reask(True)
                                        res += cardinal(False, values_cardinal[randint(0, len(values_cardinal) - 1)],
                                                        name_set, form_name)
                                        res += cardinal_confirm(True, name_set)
                                    elif type_of_reply == 1:
                                        res += valid(n_pre == 0, name_set)
                                    else:
                                        res += with_cardinal(n_pre == 0,
                                                             values_cardinal[randint(0, len(values_cardinal) - 1)],
                                                             name_set)
                            else:
                                type_of_reply = split_prob(2)
                                if type_of_reply == 0:
                                    res += multiple_choices(n_pre == 0, name_set)
                                    is_cardinal_possible = True
                                    if prob(25):
                                        res += cardinal_no_match(False, values_invalid_cardinal[
                                            randint(0, len(values_invalid_cardinal) - 1)], form_name)
                                        res += cardinal_reask(True)
                                    res += cardinal(False, values_cardinal[randint(0, len(values_cardinal) - 1)],
                                                    name_set, form_name)
                                    res += cardinal_confirm(False, name_set)
                                elif type_of_reply == 1:
                                    res += valid(n_pre == 0, name_set)
                    else:
                        res += prev(True, name_set)

                    return is_cardinal_possible, name_set, res

                if prob(75):
                    n_times = 1
                else:
                    if prob(75):
                        n_times = 2
                    else:
                        n_times = 3

                for _ in range(0, n_times):
                    action = split_prob(6)
                    r = ''
                    if action == 0:
                        is_cardinal_possible, name_set, r = by_name('details', is_cardinal_possible, name_set,
                                                                    by_name_types('details'))
                    elif action == 1:
                        is_cardinal_possible, name_set, r = by_name('preparation', is_cardinal_possible, name_set,
                                                                    by_name_types('preparation'))
                    elif action == 2:
                        is_cardinal_possible, name_set, r = by_name('ingredients', is_cardinal_possible, name_set,
                                                                    by_name_types('ingredients'))
                    elif action == 3:
                        is_cardinal_possible, name_set, r = by_name('cost', is_cardinal_possible, name_set,
                                                                    by_name_types('cost'))
                    elif action == 4:
                        is_cardinal_possible, name_set, r = by_name('availability', is_cardinal_possible, name_set,
                                                                    by_name_types('availability'))
                    elif action == 5:
                        is_cardinal_possible, name_set, r = by_name('similar_products', is_cardinal_possible, name_set,
                                                                    by_name_types('similar_products'))
                    res += r

        if prob(75):
            res += bye()
        else:
            res += thanks_bye()
        res += '\n'

    with open('stories.txt', 'w') as f:
        f.write(res)

    return res


if __name__ == '__main__':
    print(produce_stories(1000))
