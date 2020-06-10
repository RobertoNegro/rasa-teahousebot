import json
import re
from abc import ABC, abstractmethod

from rasa_sdk import Action
from rasa_sdk.events import SlotSet, FollowupAction, EventType, AllSlotsReset, Form
from fuzzywuzzy import fuzz
from rasa_sdk.forms import FormAction, REQUESTED_SLOT


class PetersTeaHouseAPI:
    @staticmethod
    def sanitize_str(s: str):
        s = s.lower()
        s = re.sub(r'[^A-Za-z0-9\s]+', '', s)
        s = re.sub(r'\s+', ' ', s)
        return s

    @staticmethod
    def fuzzy_search(s: str, names: list, objs: dict):
        name = PetersTeaHouseAPI.sanitize_str(s)
        matches = names.copy()

        for m in matches:
            m.update({'ratio': fuzz.token_set_ratio(m['name'], name)})
        matches = sorted(matches, key=lambda k: k['ratio'], reverse=True)

        best_matches = [matches[0]]
        max_ratio = matches[0]['ratio']
        for i in range(1, len(matches)):
            if max_ratio == matches[i]['ratio']:
                best_matches.append(matches[i])

        result = dict()
        for m in best_matches:
            result[m['id']] = objs[m['id']]

        return result, max_ratio

    def __init__(self) -> None:
        super().__init__()
        with open('scraper/products.json', 'r') as f:
            self.products = json.load(f)
        with open('scraper/categories.json', 'r') as f:
            self.categories = json.load(f)
        with open('scraper/filters.json', 'r') as f:
            self.filters = json.load(f)

        self.products_names = [{'id': id, 'name': self.sanitize_str(self.products[id]['name'])} for id in self.products]
        self.categories_names = [{'id': id, 'name': self.sanitize_str(self.categories[id])} for id in self.categories]
        self.filters_names = [{'id': id, 'name': self.sanitize_str(self.filters[id])} for id in self.filters]

    def get_tea_by_id(self, id):
        if id in self.products:
            return self.products[id]
        else:
            return None

    def get_tea_by_name(self, name: str):
        return self.fuzzy_search(name, self.products_names, self.products) if name is not None else ([], 0)

    def get_category_by_name(self, name):
        return self.fuzzy_search(name, self.categories_names, self.categories) if name is not None else ([], 0)

    def get_filter_by_name(self, name):
        return self.fuzzy_search(name, self.filters_names, self.filters) if name is not None else ([], 0)

    def search(self, name, category, origin, organic, christmas, availability, new):
        matches = self.products

        # name filtering
        matches_by_name, ratio_by_name = self.get_tea_by_name(name)
        if ratio_by_name > 70:
            matches = matches_by_name

        # category filtering
        filtered_by_category, ratio_by_category = self.get_category_by_name(category)
        filtered_by_category_ids = [id for id in filtered_by_category] if ratio_by_category > 70 else []
        matches = {id: matches[id] for id in matches if matches[id]['category'] in filtered_by_category_ids}

        def filter_by_filter(products, filter_method, filter_value, min_ratio=70):
            filtered, ratio = filter_method(filter_value)
            filtered_combos = [id for id in filtered] if ratio > min_ratio else []

            def checker(product):
                check_dict = dict()
                for fc in filtered_combos:
                    attr, value = fc.split('=')
                    if attr not in check_dict:
                        check_dict[attr] = []
                    check_dict[attr].append(value)

                valid = True
                for attr in check_dict:
                    attr_valid = False
                    for v in check_dict[attr]:
                        if attr in product and product[attr] == v:
                            attr_valid = True
                    valid = valid and attr_valid
                return valid

            return {id: products[id] for id in products if checker(products[id])}

        matches = filter_by_filter(matches, self.get_filter_by_name, origin)
        matches = filter_by_filter(matches, self.get_filter_by_name, organic)
        matches = filter_by_filter(matches, self.get_filter_by_name, christmas)
        matches = filter_by_filter(matches, self.get_filter_by_name, availability)
        matches = filter_by_filter(matches, self.get_filter_by_name, new)

        return matches


# region  ----- SEARCH -----
class FormActionSearch(FormAction):
    def __init__(self) -> None:
        super().__init__()
        self.api = PetersTeaHouseAPI()

    def name(self):
        return "form_action_search"

    @staticmethod
    def required_slots(tracker):
        return ["category"]

    def request_next_slot(self, dispatcher, tracker, domain):
        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                return [SlotSet(REQUESTED_SLOT, slot)]
        return None

    async def submit(self, dispatcher, tracker, domain):
        category = tracker.get_slot("category")
        origin = tracker.get_slot("origin")
        organic = tracker.get_slot("organic")
        christmas = tracker.get_slot("christmas")
        availability = tracker.get_slot("availability")
        new = tracker.get_slot("new")

        if category is not None:
            sanitized_category, ratio_category = self.api.get_category_by_name(category)
            if ratio_category <= 70:
                dispatcher.utter_message(template=f"utter_reask_category")
            else:
                dispatcher.utter_message(template="utter_ask_category_grounding")
                return [SlotSet("category", None),
                        SlotSet("origin", None),
                        SlotSet("organic", None),
                        SlotSet("christmas", None),
                        SlotSet("availability", None),
                        SlotSet("new", None),
                        SlotSet("name", None),
                        SlotSet("cardinal", None),
                        SlotSet("unfeat_name_cardinal", None),
                        SlotSet("unfeat_search_settings", (category, origin, organic, christmas, availability, new, 0)),
                        FollowupAction("action_suggest")]
        else:
            return [SlotSet("category", None),
                    SlotSet("origin", None),
                    SlotSet("organic", None),
                    SlotSet("christmas", None),
                    SlotSet("availability", None),
                    SlotSet("new", None),
                    SlotSet("name", None),
                    SlotSet("unfeat_name_cardinal", None),
                    SlotSet("unfeat_search_settings", (None, None, None, None, None, None, 0))]


def validate(self, dispatcher, tracker, domain):
    slot_values = self.extract_other_slots(dispatcher, tracker, domain)
    slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
    if slot_to_fill:
        slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))

    category = slot_values['category'] if 'category' in slot_values else None
    if category is not None:
        sanitized_category, ratio_category = self.api.get_category_by_name(category)
        if ratio_category <= 70:
            dispatcher.utter_message(template=f"utter_reask_category")
            slot_values['category'] = None

    return [SlotSet(slot, value) for slot, value in slot_values.items()]


class ClearForm(Action):
    def name(self):
        return "action_clear_form"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_can_i_help_you_again")
        return [Form(None), SlotSet(REQUESTED_SLOT, None)]


class ActionSuggest(Action):
    def __init__(self) -> None:
        super().__init__()
        self.api = PetersTeaHouseAPI()

    def name(self):
        return "action_suggest"

    def run(self, dispatcher, tracker, domain):
        category, origin, organic, christmas, availability, new, offset = tracker.get_slot("unfeat_search_settings")
        matches = self.api.search(None, category, origin, organic, christmas, availability, new)

        limit = 5  # constant for now

        matches_txt = ''

        name_cardinal = []

        limit += offset
        i = offset
        for id, m in list(matches.items())[offset:]:
            if offset < i < limit - 1:
                matches_txt += ', '
            elif i == limit - 1:
                matches_txt += ' and '
            matches_txt += m['name']
            name_cardinal.append(m)

            i += 1
            if i >= limit:
                break

        if len(matches_txt) > 0:
            dispatcher.utter_message(template="utter_suggest")
            dispatcher.utter_message(text=f"{matches_txt}.")
            if len(matches) > limit:
                dispatcher.utter_message(template="utter_suggest_hasmore")
            else:
                dispatcher.utter_message(template="utter_suggest_nomore")
                dispatcher.utter_message(template="utter_can_i_help_you_again")
        else:
            dispatcher.utter_message(template="utter_suggest_empty")

        return [SlotSet("name", None),
                SlotSet("unfeat_name_cardinal", None if len(name_cardinal) == 0 else name_cardinal),
                SlotSet("unfeat_search_settings", (category, origin, organic, christmas, availability, new, limit))]


class ActionFilter(Action):
    def __init__(self) -> None:
        super().__init__()
        self.api = PetersTeaHouseAPI()

    def name(self):
        return "action_filter"

    def run(self, dispatcher, tracker, domain):
        origin = tracker.get_slot("origin")
        organic = tracker.get_slot("organic")
        christmas = tracker.get_slot("christmas")
        availability = tracker.get_slot("availability")
        new = tracker.get_slot("new")
        search_settings = tracker.get_slot("unfeat_search_settings")
        if search_settings is not None:
            prev_category, prev_origin, prev_organic, prev_christmas, prev_availability, prev_new, prev_offset = search_settings
        else:
            prev_category = None
            prev_origin = None
            prev_organic = None
            prev_christmas = None
            prev_availability = None
            prev_new = None
            prev_offset = None

        if prev_category is not None:
            return [SlotSet("origin", None),
                    SlotSet("organic", None),
                    SlotSet("christmas", None),
                    SlotSet("availability", None),
                    SlotSet("new", None),
                    SlotSet("name", None),
                    SlotSet("cardinal", None),
                    SlotSet("unfeat_name_cardinal", None),
                    SlotSet("unfeat_search_settings", (prev_category,
                                                       origin if origin is not None else prev_origin,
                                                       organic if organic is not None else prev_organic,
                                                       christmas if christmas is not None else prev_christmas,
                                                       availability if availability is not None else prev_availability,
                                                       new if new is not None else prev_new,
                                                       0)),
                    FollowupAction("action_suggest")]
        else:
            dispatcher.utter_message(template='utter_filter_before_category')
            return [SlotSet("origin", None),
                    SlotSet("organic", None),
                    SlotSet("christmas", None),
                    SlotSet("availability", None),
                    SlotSet("new", None),
                    SlotSet("name", None),
                    SlotSet("cardinal", None),
                    SlotSet("unfeat_name_cardinal", None),
                    SlotSet("unfeat_search_settings", (prev_category,
                                                       origin if origin is not None else prev_origin,
                                                       organic if organic is not None else prev_organic,
                                                       christmas if christmas is not None else prev_christmas,
                                                       availability if availability is not None else prev_availability,
                                                       new if new is not None else prev_new,
                                                       0)),
                    FollowupAction("form_action_search")]


# endregion ---------------


# region  ----- BY NAME -----
class ActionExtractNameFromCardinal(Action):
    def __init__(self) -> None:
        super().__init__()
        self.api = PetersTeaHouseAPI()

    def name(self):
        return "action_extract_name_from_cardinal"

    def run(self, dispatcher, tracker, domain):
        cardinal = tracker.get_slot("cardinal")
        cardinal = int(cardinal) - 1
        unfeat_name_cardinal = tracker.get_slot("unfeat_name_cardinal")

        if tracker.active_form is not None and 'name' in tracker.active_form:
            followup = [FollowupAction(tracker.active_form['name'])]

            if unfeat_name_cardinal is not None and 0 <= cardinal < len(unfeat_name_cardinal):
                return [
                           SlotSet("cardinal", None),
                           SlotSet("name", unfeat_name_cardinal[cardinal]['name'])] + followup
            return [
                       SlotSet("cardinal", None),
                       SlotSet("name", None)
                   ] + followup
        else:
            dispatcher.utter_message(template="utter_can_i_help_you_again", **tracker.slots)
            return [
                SlotSet("cardinal", None),
                SlotSet("name", None)
            ]


class FormActionByName(FormAction, ABC):
    def __init__(self) -> None:
        super().__init__()
        self.api = PetersTeaHouseAPI()

    @staticmethod
    def required_slots(tracker):
        return ["name"]

    def request_next_slot(self, dispatcher, tracker, domain):
        additional_rets = []
        for slot in self.required_slots(tracker):
            if self._should_request_slot(tracker, slot):
                if slot == 'name':
                    cardinal = tracker.get_slot('cardinal')
                    if cardinal is not None:
                        cardinal = int(cardinal) - 1
                        unfeat_name_cardinal = tracker.get_slot('unfeat_name_cardinal')
                        if unfeat_name_cardinal is not None:
                            additional_rets = [SlotSet("name", unfeat_name_cardinal[cardinal]['name']),
                                               SlotSet("cardinal", None),
                                               FollowupAction(self.name())]
                    else:
                        dispatcher.utter_message(template=f"utter_ask_{slot}", **tracker.slots)
                        return [SlotSet(REQUESTED_SLOT, slot)] + additional_rets
                else:
                    return [SlotSet(REQUESTED_SLOT, slot)] + additional_rets
        return None if len(additional_rets) == 0 else additional_rets

    @abstractmethod
    async def done(self, product, dispatcher, tracker, domain):
        pass

    async def submit(self, dispatcher, tracker, domain):
        name = tracker.get_slot("name")

        matches_by_name, ratio_by_name = self.api.get_tea_by_name(name)
        if len(matches_by_name) == 0 or ratio_by_name <= 70:
            dispatcher.utter_message(template=f"utter_invalid_name")
            return [SlotSet("name", None)]

        if len(matches_by_name) == 1:
            for id in matches_by_name:
                await self.done(matches_by_name[id], dispatcher, tracker, domain)
        else:
            txt = 'I\'ve found: '
            unfeat_name_cardinal = []
            for i, id in enumerate(matches_by_name):
                txt += f'{matches_by_name[id]["name"]}'
                if i < len(matches_by_name) - 2:
                    txt += f', '
                elif i < len(matches_by_name) - 1:
                    txt += f' or '
                unfeat_name_cardinal.append(matches_by_name[id])
            txt += '.'
            dispatcher.utter_message(text=txt)
            return [SlotSet("unfeat_name_cardinal", unfeat_name_cardinal), SlotSet("name", None),
                    FollowupAction(self.name())]

        return []

    def validate(self, dispatcher, tracker, domain):
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher, tracker, domain))

        name = slot_values['name'] if 'name' in slot_values else None
        if name is not None:
            matches_by_name, ratio_by_name = self.api.get_tea_by_name(name)
            if len(matches_by_name) == 0 or ratio_by_name <= 70:
                dispatcher.utter_message(template=f"utter_invalid_name")
                slot_values['name'] = None
        else:
            cardinal = slot_values["cardinal"] if 'cardinal' in slot_values else None
            if cardinal is not None:
                cardinal = int(cardinal) - 1
                unfeat_name_cardinal = slot_values[
                    "unfeat_name_cardinal"] if 'unfeat_name_cardinal' in slot_values else None
                if unfeat_name_cardinal is not None:
                    slot_values['name'] = unfeat_name_cardinal[cardinal]['name']
                slot_values['cardinal'] = None
        return [SlotSet(slot, value) for slot, value in slot_values.items()]


class FormActionDetails(FormActionByName):
    def name(self):
        return "form_action_details"

    async def done(self, product, dispatcher, tracker, domain):
        description = product['description']
        dispatcher.utter_message(text=f"{description}.")


class FormActionPreparations(FormActionByName):
    def name(self):
        return "form_action_preparation"

    async def done(self, product, dispatcher, tracker, domain):
        teaspons = product['teaspons']
        temperature = product['temperature']
        time = product['time']
        dispatcher.utter_message(text=f"You have to dip {teaspons} of tea leaves for {time} in water at {temperature}.")


class FormActionCosts(FormActionByName):
    def name(self):
        return "form_action_cost"

    async def done(self, product, dispatcher, tracker, domain):
        cost = product['price']
        dispatcher.utter_message(text=f"This tea costs {cost} euros per hectogram.")


class FormActionIngredients(FormActionByName):
    def name(self):
        return "form_action_ingredients"

    async def done(self, product, dispatcher, tracker, domain):
        ingredients = product['ingredients']
        if ingredients != 'N.A.':
            dispatcher.utter_message(text=f"{ingredients}.")
        else:
            dispatcher.utter_message(template="utter_not_available")


class FormActionAvailability(FormActionByName):
    def name(self):
        return "form_action_availability"

    async def done(self, product, dispatcher, tracker, domain):
        availability = product['q_stock']
        if availability == 'available':
            dispatcher.utter_message(template="utter_availability_available")
        else:
            dispatcher.utter_message(template="utter_availability_not_available")


class FormActionSimilarProducts(FormActionByName):
    def name(self):
        return "form_action_similar_products"

    async def done(self, product, dispatcher, tracker, domain):
        similar_to = product['similar_to']
        similar_teas = []
        for id in similar_to:
            found = self.api.get_tea_by_id(id)
            if found is not None:
                similar_teas.append(found)

        txt = ''
        for index, tea in enumerate(similar_teas):
            if 0 < index < len(similar_teas) - 1:
                txt += ', '
            elif index == len(similar_teas) - 1:
                txt += ' and '
            txt += tea['name']

        if len(txt) > 0:
            dispatcher.utter_message(template="utter_similar_products")
            dispatcher.utter_message(text=f"{txt}.")
        else:
            dispatcher.utter_message(template="utter_similar_products_empty")
