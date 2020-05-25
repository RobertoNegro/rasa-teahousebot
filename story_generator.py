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
        '- utter_greet\n' +
        '- utter_how_can_i_help_you\n'
)

bye = lambda: (
        '* goodbye\n' +
        '- utter_goodbye\n'
)

thanks_bye = lambda: (
        '* thanks_goodbye\n' +
        '- utter_thanks_goodbye\n'
)

search_affirm = lambda category, origin, organic, christmas, availability, new, offset: (
        '* search_affirm\n' +
        '- action_suggest\n' +
        '- slot{"name": null}\n' +
        get_unfeat_search_settings(category, origin, organic, christmas, availability, new, offset)
)

search_deny = lambda: (
        '* search_deny\n' +
        '- utter_can_i_help_you_again\n'
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

search = lambda first_time, category: (
        ('* form: ' if not first_time else '* ') +
        'search{"category": "' + category + '"}\n' +
        '- slot{"category": "' + category + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_search\n' +
        '- slot{"category": "' + category + '"}\n' +
        '- slot{"category": null}\n' +
        '- slot{"origin": null}\n' +
        '- slot{"organic": null}\n' +
        '- slot{"christmas": null}\n' +
        '- slot{"availability": null}\n' +
        '- slot{"new": null}\n' +
        '- slot{"name": null}\n' +
        get_unfeat_search_settings(category, "null", "null", "null", "null", "null", 0) +
        '- form: followup{"name": "action_suggest"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- action_suggest\n' +
        '- slot{"name": null}\n' +
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
        get_unfeat_search_settings(category, origin, organic, christmas, availability, new, 0) +
        ((
                 '- followup{"name": "action_suggest"}\n' +
                 '- action_suggest\n' +
                 '- slot{"name": null}\n' +
                 get_unfeat_search_settings(category, origin, organic, christmas, availability, new, 5)
         ) if category != 'null' else (
                '- followup{"name": "form_action_search"}\n' +
                '- form_action_search\n' +
                '- form{"name": "form_action_search"}\n' +
                '- slot{"requested_slot": "category"}\n'
        ))
)

preparation_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'preparation\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_preparation\n' +
        '- form{"name": "form_action_preparation"}\n' +
        '- slot{"requested_slot": "name"}\n'
)

preparation_unknown = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'preparation{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_preparation\n' +
        '- slot{"name": null}\n' +
        '- slot{"requested_slot": "name"}\n'
)

preparation = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'preparation{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_preparation\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

preparation_prev = lambda name: (
        '* preparation\n' +
        '- form_action_preparation\n' +
        '- form{"name": "form_action_preparation"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

details_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'details\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_details\n' +
        '- form{"name": "form_action_details"}\n' +
        '- slot{"requested_slot": "name"}\n'
)

details_unknown = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'details{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_details\n' +
        '- slot{"name": null}\n' +
        '- slot{"requested_slot": "name"}\n'
)

details = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'details{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_details\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

details_prev = lambda name: (
        '* details\n' +
        '- form_action_details\n' +
        '- form{"name": "form_action_details"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

cost_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'cost\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_cost\n' +
        '- form{"name": "form_action_cost"}\n' +
        '- slot{"requested_slot": "name"}\n'
)

cost_unknown = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'cost{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_cost\n' +
        '- slot{"name": null}\n' +
        '- slot{"requested_slot": "name"}\n'
)

cost = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'cost{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_cost\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

cost_prev = lambda name: (
        '* cost\n' +
        '- form_action_cost\n' +
        '- form{"name": "form_action_cost"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

ingredients_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'ingredients\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_ingredients\n' +
        '- form{"name": "form_action_ingredients"}\n' +
        '- slot{"requested_slot": "name"}\n'
)

ingredients_unknown = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'ingredients{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_ingredients\n' +
        '- slot{"name": null}\n' +
        '- slot{"requested_slot": "name"}\n'
)

ingredients = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'ingredients{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_ingredients\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

ingredients_prev = lambda name: (
        '* ingredients\n' +
        '- form_action_ingredients\n' +
        '- form{"name": "form_action_ingredients"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

availability_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'availability\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_availability\n' +
        '- form{"name": "form_action_availability"}\n' +
        '- slot{"requested_slot": "name"}\n'
)

availability_unknown = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'availability{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_availability\n' +
        '- slot{"name": null}\n' +
        '- slot{"requested_slot": "name"}\n'
)

availability = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'availability{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_availability\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

availability_prev = lambda name: (
        '* availability\n' +
        '- form_action_availability\n' +
        '- form{"name": "form_action_availability"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

similar_products_empty = lambda first_time: (
        ('* form: ' if not first_time else '* ') +
        'similar_products\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_similar_products\n' +
        '- form{"name": "form_action_similar_products"}\n' +
        '- slot{"requested_slot": "name"}\n'
)

similar_products_unknown = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'similar_products{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_similar_products\n' +
        '- slot{"name": null}\n' +
        '- slot{"requested_slot": "name"}\n'
)

similar_products = lambda first_time, name: (
        ('* form: ' if not first_time else '* ') +
        'similar_products{"name": "' + name + '"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        ('- form: ' if not first_time else '- ') + 'form_action_similar_products\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

similar_products_prev = lambda name: (
        '* similar_products\n' +
        '- form_action_similar_products\n' +
        '- form{"name": "form_action_similar_products"}\n' +
        '- slot{"name": "' + name + '"}\n' +
        '- form{"name": null}\n' +
        '- slot{"requested_slot": null}\n' +
        '- utter_can_i_help_you_again\n'
)

values_category = ["Black Teas", "Oolong", "White Teas", "Gold Tea Selection", "Fruit Infusions", "Rooibos", "Herbal Teas",
            "Matcha and Flower Teas"]

values_new = ["New"]
values_organic = ["Organic", "Not organic"]
values_christmas = ["Christmas", "Not christmas"]
values_origin = ["Ceylon", "China", "India", "Taiwan", "Korea", "Tanzania", "South africa"]
values_availability = ["Available", "Not available"]

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


# possibilities = {
#     "new": ["New"],
#     "organic": ["Organic"],
#     "christmas": ["Christmas"],
#     "origin": ["China", "India"],
#     "availability": ["Available", "Not available"],
#     "category": ["Black Teas", "Oolong"],
# }

def produce_stories(n):
    res = ''

    for i in range(0, n):
        name_set = None
        filter_wait_for_category = False

        res += f'## story {i + 1}\n'

        cur_category = 'null'

        cur_origin = 'null'
        cur_organic = 'null'
        cur_christmas = 'null'
        cur_availability = 'null'
        cur_new = 'null'

        if randint(0, 2) >= 1:
            res += greet()

        at_least_one_category = False
        n_entities = randint(1, 5)
        for j in range(0, n_entities):
            rand_el = randint(0, 2)
            if rand_el == 0:
                name_set = None

                for _ in range(0, randint(1, 3)):
                    rand_el = randint(0, 4)
                    if rand_el == 0:
                        cur_origin = values_origin[randint(0, len(values_origin) - 1)]
                    elif rand_el == 1:
                        cur_organic = values_organic[randint(0, len(values_organic) - 1)]
                    elif rand_el == 2:
                        cur_christmas = values_christmas[randint(0, len(values_christmas) - 1)]
                    elif rand_el == 3:
                        cur_availability = values_availability[randint(0, len(values_availability) - 1)]
                    elif rand_el == 4:
                        cur_new = values_new[randint(0, len(values_new) - 1)]
                res += filter(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability, cur_new)

                if cur_category != 'null':
                    n_affirm = randint(0, 5)
                    offset = 10
                    for j in range(0, n_affirm):
                        res += search_affirm(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability,
                                             cur_new,
                                             offset)
                        offset += 5
                    n_deny = randint(0, 1)
                    for j in range(0, n_deny):
                        res += search_deny()
                else:
                    filter_wait_for_category = True

            elif rand_el == 1:
                name_set = None
                cur_category = 'null'

                cur_origin = 'null'
                cur_organic = 'null'
                cur_christmas = 'null'
                cur_availability = 'null'
                cur_new = 'null'

                max_rep = randint(1, 3)
                for i in range(0, max_rep):
                    if i == max_rep - 1:
                        cur_category = values_category[randint(0, len(values_category) - 1)]
                        res += search(not filter_wait_for_category and i == 0, cur_category)
                    else:
                        rand_el = randint(0, 1)
                        if rand_el == 0:
                            res += search_unknown(not filter_wait_for_category and i == 0, 'unknown')
                        else:
                            res += search_empty(not filter_wait_for_category and i == 0)
                filter_wait_for_category = False

                if cur_category != 'null':
                    n_affirm = randint(0, 5)
                    offset = 10
                    for j in range(0, n_affirm):
                        res += search_affirm(cur_category, cur_origin, cur_organic, cur_christmas, cur_availability,
                                             cur_new,
                                             offset)
                        offset += 5
                    n_deny = randint(0, 1)
                    for j in range(0, n_deny):
                        res += search_deny()

            else:
                # details, preparations, ingredients, cost, availability, similar_products
                def by_name(name_set, unknown, empty, normal, prev):
                    res = ''
                    if name_set is not None:
                        if randint(0, 3) == 0:
                            n_pre = randint(0, 2)
                            for i in range(0, n_pre):
                                if i == 0:
                                    res += unknown(True, 'unknown')
                                else:
                                    if randint(0, 1) == 0:
                                        res += unknown(False, 'unknown')
                                    else:
                                        res += empty(False)
                            name_set = products[randint(0, len(products) - 1)]
                            res += normal(n_pre == 0, name_set)
                        else:
                            res += prev(name_set)
                    else:
                        n_pre = randint(0, 3)
                        for i in range(0, n_pre):
                            if randint(0, 1) == 0:
                                res += unknown(i == 0, 'unknown')
                            else:
                                res += empty(i == 0)

                        name_set = products[randint(0, len(products) - 1)]
                        res += normal(n_pre == 0, name_set)
                    return name_set, res

                n_times = randint(1, 3)
                for _ in range(0, n_times):
                    rand_el = randint(0, 5)
                    if rand_el == 0:
                        name_set, r = by_name(name_set, details_unknown, details_empty, details, details_prev)
                        res += r
                    elif rand_el == 1:
                        name_set, r = by_name(name_set, preparation_unknown, preparation_empty, preparation,
                                              preparation_prev)
                        res += r
                    elif rand_el == 2:
                        name_set, r = by_name(name_set, ingredients_unknown, ingredients_empty, ingredients,
                                              ingredients_prev)
                        res += r
                    elif rand_el == 3:
                        name_set, r = by_name(name_set, cost_unknown, cost_empty, cost, cost_prev)
                        res += r
                    elif rand_el == 4:
                        name_set, r = by_name(name_set, availability_unknown, availability_empty, availability,
                                              availability_prev)
                        res += r
                    elif rand_el == 5:
                        name_set, r = by_name(name_set, similar_products_unknown, similar_products_empty, similar_products,
                                              similar_products_prev)
                        res += r

        rand_bye = randint(0, 4)
        if rand_bye >= 3:
            res += bye()
        elif rand_bye >= 1:
            res += thanks_bye()
        res += '\n'

    with open('stories.txt', 'w') as f:
        f.write(res)

    return res


if __name__ == '__main__':
    print(produce_stories(100))
