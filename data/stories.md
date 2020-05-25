## story 1
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "China Keemun Black Tea"}
- slot{"name": "China Keemun Black Tea"}
- form: form_action_similar_products
- slot{"name": "China Keemun Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "China Keemun Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "China Keemun Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 2
* filter{"christmas": "Christmas", "new": "New"}
- slot{"christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form: form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, "Organic", null, null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, "Organic", null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again

## story 3
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Green Rooibos Vanilla and Lemon"}
- slot{"name": "Green Rooibos Vanilla and Lemon"}
- form: form_action_ingredients
- slot{"name": "Green Rooibos Vanilla and Lemon"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 4
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}

## story 5
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Ceylon"}
- slot{"origin": "Ceylon"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Ceylon", null, null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Ceylon", "organic": "Organic"}
- slot{"origin": "Ceylon", "organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Ceylon", "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 30]}
* filter{"origin": "Tanzania", "new": "New"}
- slot{"origin": "Tanzania", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Tanzania", null, null, null, "New", 30]}
* search_deny
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Pepita Fruit Infusion FES"}
- slot{"name": "Pepita Fruit Infusion FES"}
- form: form_action_availability
- slot{"name": "Pepita Fruit Infusion FES"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Pepita Fruit Infusion FES"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 6
* greet
- utter_greet
- utter_how_can_i_help_you
* availability{"name": "Greek Mountain Herbal Tea"}
- slot{"name": "Greek Mountain Herbal Tea"}
- form_action_availability
- slot{"name": "Greek Mountain Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Greek Mountain Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Greek Mountain Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost
- form: form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "Yunnan Green Tea"}
- slot{"name": "Yunnan Green Tea"}
- form: form_action_cost
- slot{"name": "Yunnan Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Yunnan Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Yunnan Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "Taiwan", "availability": "Not available", "new": "New"}
- slot{"origin": "Taiwan", "availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Taiwan", null, null, "Not available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Taiwan", null, null, "Not available", "New", 5]}
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Nepal Jun Chiyabari Oolong BIO"}
- slot{"name": "Nepal Jun Chiyabari Oolong BIO"}
- form: form_action_ingredients
- slot{"name": "Nepal Jun Chiyabari Oolong BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "Mandarine and Cinnamon Black Tea"}
- slot{"name": "Mandarine and Cinnamon Black Tea"}
- form_action_availability
- slot{"name": "Mandarine and Cinnamon Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 7
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "South africa", "availability": "Not available"}
- slot{"origin": "South africa", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "South africa", null, null, "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Rooibos Orange"}
- slot{"name": "Rooibos Orange"}
- form: form_action_ingredients
- slot{"name": "Rooibos Orange"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "South africa", "organic": "Organic", "availability": "Not available"}
- slot{"origin": "South africa", "organic": "Organic", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "South africa", "Organic", null, "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "South africa", "organic": "Organic", "availability": "Not available", "new": "New"}
- slot{"origin": "South africa", "organic": "Organic", "availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "South africa", "Organic", null, "Not available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Nuwara Eliya FOP Black Tea"}
- slot{"name": "Nuwara Eliya FOP Black Tea"}
- form: form_action_availability
- slot{"name": "Nuwara Eliya FOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Nuwara Eliya FOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 8
* greet
- utter_greet
- utter_how_can_i_help_you
* availability{"name": "Dong Ding Oolong"}
- slot{"name": "Dong Ding Oolong"}
- form_action_availability
- slot{"name": "Dong Ding Oolong"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Silk Road Green Tea"}
- slot{"name": "Silk Road Green Tea"}
- form: form_action_similar_products
- slot{"name": "Silk Road Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Silk Road Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 9
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"availability": "Available"}
- slot{"availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, "Available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 10
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Darjeeling Margaret's Hope Black Tea"}
- slot{"name": "Darjeeling Margaret's Hope Black Tea"}
- form: form_action_similar_products
- slot{"name": "Darjeeling Margaret's Hope Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 11
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Ceylon", "organic": "Organic"}
- slot{"origin": "Ceylon", "organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Ceylon", "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 12
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Herbal Teas"}
- slot{"category": "Herbal Teas"}
- form: form_action_search
- slot{"category": "Herbal Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 30]}
* thanks_goodbye
- utter_thanks_goodbye

## story 13
* greet
- utter_greet
- utter_how_can_i_help_you
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Earl Grey Black Tea"}
- slot{"name": "Earl Grey Black Tea"}
- form: form_action_availability
- slot{"name": "Earl Grey Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Japanese Cherry Green Tea"}
- slot{"name": "Japanese Cherry Green Tea"}
- form: form_action_ingredients
- slot{"name": "Japanese Cherry Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"christmas": "Christmas", "new": "New"}
- slot{"christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}

## story 14
* greet
- utter_greet
- utter_how_can_i_help_you
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Cranberry Queen Fruit Infusion"}
- slot{"name": "Cranberry Queen Fruit Infusion"}
- form: form_action_similar_products
- slot{"name": "Cranberry Queen Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost{"name": "Sweet Symphony Fruit Infusion"}
- slot{"name": "Sweet Symphony Fruit Infusion"}
- form_action_cost
- slot{"name": "Sweet Symphony Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* filter{"christmas": "Not christmas"}
- slot{"christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, "Not christmas", null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, "Not christmas", null, null, 5]}
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* filter{"origin": "China", "christmas": "Not christmas"}
- slot{"origin": "China", "christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", "China", null, "Not christmas", null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", "China", null, "Not christmas", null, null, 5]}
* thanks_goodbye
- utter_thanks_goodbye

## story 15
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Not organic"}
- slot{"organic": "Not organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"organic": "Not organic", "christmas": "Not christmas"}
- slot{"organic": "Not organic", "christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", "Not christmas", null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 16
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"christmas": "Christmas", "new": "New"}
- slot{"christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"organic": "Organic", "christmas": "Christmas", "availability": "Available", "new": "New"}
- slot{"organic": "Organic", "christmas": "Christmas", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", "Christmas", "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 17
* filter{"christmas": "Not christmas", "availability": "Not available"}
- slot{"christmas": "Not christmas", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Not christmas", "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 18
* greet
- utter_greet
- utter_how_can_i_help_you
* preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation
- form: form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Exotic Dream white tea"}
- slot{"name": "Exotic Dream white tea"}
- form: form_action_preparation
- slot{"name": "Exotic Dream white tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Exotic Dream white tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 19
* greet
- utter_greet
- utter_how_can_i_help_you
* cost{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "Kabusecha Green Tea"}
- slot{"name": "Kabusecha Green Tea"}
- form: form_action_cost
- slot{"name": "Kabusecha Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Kabusecha Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 20
* greet
- utter_greet
- utter_how_can_i_help_you
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Green Breakfsat Bio green Tea"}
- slot{"name": "Green Breakfsat Bio green Tea"}
- form: form_action_availability
- slot{"name": "Green Breakfsat Bio green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Assam Goldtips TGFOP Black Tea"}
- slot{"name": "Assam Goldtips TGFOP Black Tea"}
- form: form_action_availability
- slot{"name": "Assam Goldtips TGFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Assam Goldtips TGFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 21
* greet
- utter_greet
- utter_how_can_i_help_you
* details{"name": "Lapacho FES"}
- slot{"name": "Lapacho FES"}
- form_action_details
- slot{"name": "Lapacho FES"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Ayurveda Relax Herbal Tea"}
- slot{"name": "Ayurveda Relax Herbal Tea"}
- form: form_action_ingredients
- slot{"name": "Ayurveda Relax Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 25]}
* thanks_goodbye
- utter_thanks_goodbye

## story 22
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Orange Ginger Fruit Infusion"}
- slot{"name": "Orange Ginger Fruit Infusion"}
- form: form_action_availability
- slot{"name": "Orange Ginger Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation{"name": "Matcha-Kukicha Instant Green Tea BIO 50g"}
- slot{"name": "Matcha-Kukicha Instant Green Tea BIO 50g"}
- form_action_preparation
- slot{"name": "Matcha-Kukicha Instant Green Tea BIO 50g"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Matcha-Kukicha Instant Green Tea BIO 50g"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Matcha-Kukicha Instant Green Tea BIO 50g"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 23
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 24
* greet
- utter_greet
- utter_how_can_i_help_you
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Open Fire Fruit Infusion"}
- slot{"name": "Open Fire Fruit Infusion"}
- form: form_action_preparation
- slot{"name": "Open Fire Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Open Fire Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Open Fire Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 25
* greet
- utter_greet
- utter_how_can_i_help_you
* cost{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost
- form: form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost{"name": "Good Luck Charm Fruit Infusion"}
- slot{"name": "Good Luck Charm Fruit Infusion"}
- form: form_action_cost
- slot{"name": "Good Luck Charm Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "Earl Grey Black Tea"}
- slot{"name": "Earl Grey Black Tea"}
- form_action_availability
- slot{"name": "Earl Grey Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Earl Grey Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Earl Grey Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Darjeeling Gold GFOP Black Tea"}
- slot{"name": "Darjeeling Gold GFOP Black Tea"}
- form: form_action_availability
- slot{"name": "Darjeeling Gold GFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Darjeeling Gold GFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 26
* filter{"origin": "Tanzania"}
- slot{"origin": "Tanzania"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Tanzania", null, null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form: form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* thanks_goodbye
- utter_thanks_goodbye

## story 27
* search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* filter{"origin": "India", "christmas": "Christmas"}
- slot{"origin": "India", "christmas": "Christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "India", null, "Christmas", null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "India", null, "Christmas", null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "India", null, "Christmas", null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "India", null, "Christmas", null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "India", null, "Christmas", null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "India", null, "Christmas", null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Forest Gifts Herbal Tea"}
- slot{"name": "Forest Gifts Herbal Tea"}
- form: form_action_ingredients
- slot{"name": "Forest Gifts Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Forest Gifts Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Forest Gifts Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "Taiwan", "christmas": "Not christmas"}
- slot{"origin": "Taiwan", "christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "Taiwan", null, "Not christmas", null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "Taiwan", null, "Not christmas", null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "Taiwan", null, "Not christmas", null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "Taiwan", null, "Not christmas", null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", "Taiwan", null, "Not christmas", null, null, 20]}
* details{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_details
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: details{"name": "Teaflower Casanova Black Tea"}
- slot{"name": "Teaflower Casanova Black Tea"}
- form: form_action_details
- slot{"name": "Teaflower Casanova Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Teaflower Casanova Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Teaflower Casanova Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 28
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* filter{"availability": "Available"}
- slot{"availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Available", null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Available", null, 15]}
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* goodbye
- utter_goodbye

## story 29
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form: form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 20]}
* goodbye
- utter_goodbye

## story 30
* greet
- utter_greet
- utter_how_can_i_help_you
* details{"name": "China Rose Black Tea"}
- slot{"name": "China Rose Black Tea"}
- form_action_details
- slot{"name": "China Rose Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "China Rose Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "Indian Chai Organic Black Tea"}
- slot{"name": "Indian Chai Organic Black Tea"}
- form_action_availability
- slot{"name": "Indian Chai Organic Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Herbal Teas"}
- slot{"category": "Herbal Teas"}
- form_action_search
- slot{"category": "Herbal Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 15]}
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Greek Mountain Herbal Tea"}
- slot{"name": "Greek Mountain Herbal Tea"}
- form: form_action_availability
- slot{"name": "Greek Mountain Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Greek Mountain Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 31
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* filter{"origin": "Korea", "christmas": "Christmas"}
- slot{"origin": "Korea", "christmas": "Christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, "Christmas", null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, "Christmas", null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, "Christmas", null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, "Christmas", null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, "Christmas", null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* cost{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "Exotic Dream white tea"}
- slot{"name": "Exotic Dream white tea"}
- form: form_action_cost
- slot{"name": "Exotic Dream white tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Exotic Dream white tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Indonesia Java OP Green Tea BIO"}
- slot{"name": "Indonesia Java OP Green Tea BIO"}
- form: form_action_similar_products
- slot{"name": "Indonesia Java OP Green Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 32
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Taiwan"}
- slot{"origin": "Taiwan"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Taiwan", null, null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Apple Strudel Black Tea"}
- slot{"name": "Apple Strudel Black Tea"}
- form: form_action_similar_products
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Lady Camilla Herbal Tea"}
- slot{"name": "Lady Camilla Herbal Tea"}
- form: form_action_ingredients
- slot{"name": "Lady Camilla Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Lady Camilla Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 33
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"availability": "Not available", "new": "New"}
- slot{"availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, "Not available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* filter{"origin": "China"}
- slot{"origin": "China"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", "China", null, null, null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", "China", null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", "China", null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", "China", null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 34
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 30]}
* filter{"new": "New"}
- slot{"new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, "New", 15]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* thanks_goodbye
- utter_thanks_goodbye

## story 35
* greet
- utter_greet
- utter_how_can_i_help_you
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Mediterranean Herbal Tea"}
- slot{"name": "Mediterranean Herbal Tea"}
- form: form_action_availability
- slot{"name": "Mediterranean Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Mediterranean Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Mediterranean Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Mediterranean Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Herbal Dreams Herbal Tea"}
- slot{"name": "Herbal Dreams Herbal Tea"}
- form: form_action_availability
- slot{"name": "Herbal Dreams Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Perfumes of Lavender Black Tea BIO"}
- slot{"name": "Perfumes of Lavender Black Tea BIO"}
- form: form_action_similar_products
- slot{"name": "Perfumes of Lavender Black Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Perfumes of Lavender Black Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"christmas": "Christmas"}
- slot{"christmas": "Christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, "Christmas", null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, "Christmas", null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, "Christmas", null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, "Christmas", null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, "Christmas", null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 36
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* filter{"origin": "Korea", "availability": "Available"}
- slot{"origin": "Korea", "availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Korea", null, null, "Available", null, 30]}
* filter{"origin": "Ceylon", "availability": "Not available"}
- slot{"origin": "Ceylon", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Ceylon", null, null, "Not available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Ceylon", null, null, "Not available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", "Ceylon", null, null, "Not available", null, 10]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 30]}
* details{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_details
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: details{"name": "Honeymoon Green Tea BIO"}
- slot{"name": "Honeymoon Green Tea BIO"}
- form: form_action_details
- slot{"name": "Honeymoon Green Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "Gyokuro Green Tea"}
- slot{"name": "Gyokuro Green Tea"}
- form_action_availability
- slot{"name": "Gyokuro Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 37
* filter{"origin": "Taiwan"}
- slot{"origin": "Taiwan"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Taiwan", null, null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Taiwan", "organic": "Organic", "availability": "Available", "new": "New"}
- slot{"origin": "Taiwan", "organic": "Organic", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Taiwan", "Organic", null, "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Korea", "organic": "Organic", "availability": "Available", "new": "New"}
- slot{"origin": "Korea", "organic": "Organic", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", "Organic", null, "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Korea", "organic": "Organic", "availability": "Available", "new": "New"}
- slot{"origin": "Korea", "organic": "Organic", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", "Organic", null, "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Taiwan", "organic": "Organic", "availability": "Not available", "new": "New"}
- slot{"origin": "Taiwan", "organic": "Organic", "availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Taiwan", "Organic", null, "Not available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}

## story 38
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Teaflower Orient Flame Black Tea"}
- slot{"name": "Teaflower Orient Flame Black Tea"}
- form: form_action_availability
- slot{"name": "Teaflower Orient Flame Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Teaflower Orient Flame Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Teaflower Orient Flame Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 39
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"new": "New"}
- slot{"new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 30]}
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Rooibos African Chai"}
- slot{"name": "Rooibos African Chai"}
- form: form_action_similar_products
- slot{"name": "Rooibos African Chai"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Rooibos African Chai"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Not organic", "availability": "Available"}
- slot{"organic": "Not organic", "availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, "Not organic", null, "Available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, "Not organic", null, "Available", null, 5]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 40
* search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Earl Grey Lady Blue Black Tea"}
- slot{"name": "Earl Grey Lady Blue Black Tea"}
- form: form_action_ingredients
- slot{"name": "Earl Grey Lady Blue Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Winter Magic Black Tea"}
- slot{"name": "Winter Magic Black Tea"}
- form: form_action_similar_products
- slot{"name": "Winter Magic Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 41
* filter{"origin": "Korea", "organic": "Not organic", "new": "New"}
- slot{"origin": "Korea", "organic": "Not organic", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", "Not organic", null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 30]}
* goodbye
- utter_goodbye

## story 42
* greet
- utter_greet
- utter_how_can_i_help_you
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Gunpowder Temple of Heaven Green Tea"}
- slot{"name": "Gunpowder Temple of Heaven Green Tea"}
- form: form_action_availability
- slot{"name": "Gunpowder Temple of Heaven Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "Hibiscus Flower Herbal Tea"}
- slot{"name": "Hibiscus Flower Herbal Tea"}
- form_action_availability
- slot{"name": "Hibiscus Flower Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Vanilla Bourbon Black Tea"}
- slot{"name": "Vanilla Bourbon Black Tea"}
- form: form_action_availability
- slot{"name": "Vanilla Bourbon Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 43
* greet
- utter_greet
- utter_how_can_i_help_you
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Golden Nepal Maloom Black Tea Bio"}
- slot{"name": "Golden Nepal Maloom Black Tea Bio"}
- form: form_action_similar_products
- slot{"name": "Golden Nepal Maloom Black Tea Bio"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Assam TGFOP Satrupa Organic Black Tea"}
- slot{"name": "Assam TGFOP Satrupa Organic Black Tea"}
- form: form_action_availability
- slot{"name": "Assam TGFOP Satrupa Organic Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 44
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* filter{"organic": "Not organic", "new": "New"}
- slot{"organic": "Not organic", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, "Not organic", null, null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, "Not organic", null, null, "New", 5]}
* thanks_goodbye
- utter_thanks_goodbye

## story 45
* greet
- utter_greet
- utter_how_can_i_help_you
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients
- form: form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Himalaya White Tea"}
- slot{"name": "Himalaya White Tea"}
- form: form_action_ingredients
- slot{"name": "Himalaya White Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 46
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 47
* search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 48
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Organic", "christmas": "Not christmas", "new": "New"}
- slot{"organic": "Organic", "christmas": "Not christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", "Not christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* details{"name": "Sencha Organic Green Tea"}
- slot{"name": "Sencha Organic Green Tea"}
- form_action_details
- slot{"name": "Sencha Organic Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Pink Summer Green Tea"}
- slot{"name": "Pink Summer Green Tea"}
- form: form_action_similar_products
- slot{"name": "Pink Summer Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Pink Summer Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Pink Summer Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 25]}
* goodbye
- utter_goodbye

## story 49
* greet
- utter_greet
- utter_how_can_i_help_you
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Peppermint Herbal Tea"}
- slot{"name": "Peppermint Herbal Tea"}
- form: form_action_similar_products
- slot{"name": "Peppermint Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 30]}
* similar_products{"name": "Hibiscus Flower Herbal Tea"}
- slot{"name": "Hibiscus Flower Herbal Tea"}
- form_action_similar_products
- slot{"name": "Hibiscus Flower Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, "Organic", null, null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, "Organic", null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 50
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 51
* cost{"name": "Liquorice Black Tea"}
- slot{"name": "Liquorice Black Tea"}
- form_action_cost
- slot{"name": "Liquorice Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Liquorice Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Liquorice Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 52
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"availability": "Not available", "new": "New"}
- slot{"availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, "Not available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* goodbye
- utter_goodbye

## story 53
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients
- form: form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Ceylon OP1 Pettiagalla Black Tea"}
- slot{"name": "Ceylon OP1 Pettiagalla Black Tea"}
- form: form_action_ingredients
- slot{"name": "Ceylon OP1 Pettiagalla Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Ceylon OP1 Pettiagalla Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Ceylon OP1 Pettiagalla Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Not organic", "availability": "Not available", "new": "New"}
- slot{"organic": "Not organic", "availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, "Not organic", null, "Not available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, "Not organic", null, "Not available", "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, "Not organic", null, "Not available", "New", 10]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 54
* filter{"christmas": "Not christmas"}
- slot{"christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Not christmas", null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* cost{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost
- form: form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost{"name": "Turkish Apple Fruit Infusion"}
- slot{"name": "Turkish Apple Fruit Infusion"}
- form: form_action_cost
- slot{"name": "Turkish Apple Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* thanks_goodbye
- utter_thanks_goodbye

## story 55
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 30]}
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Exotic Harmony Green Tea"}
- slot{"name": "Exotic Harmony Green Tea"}
- form: form_action_ingredients
- slot{"name": "Exotic Harmony Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Exotic Harmony Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 56
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 20]}
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form: form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* thanks_goodbye
- utter_thanks_goodbye

## story 57
* greet
- utter_greet
- utter_how_can_i_help_you
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Good Evening Herbal Tea"}
- slot{"name": "Good Evening Herbal Tea"}
- form: form_action_preparation
- slot{"name": "Good Evening Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "Winter Fairytale Fruit Infusion"}
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form: form_action_cost
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}

## story 58
* preparation{"name": "Rooibos African Chai"}
- slot{"name": "Rooibos African Chai"}
- form_action_preparation
- slot{"name": "Rooibos African Chai"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Rooibos African Chai"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"christmas": "Not christmas"}
- slot{"christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Not christmas", null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Rwanda Rukeri Black tea"}
- slot{"name": "Rwanda Rukeri Black tea"}
- form: form_action_preparation
- slot{"name": "Rwanda Rukeri Black tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "White Dragon Organic White Tea BIO"}
- slot{"name": "White Dragon Organic White Tea BIO"}
- form_action_availability
- slot{"name": "White Dragon Organic White Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "White Dragon Organic White Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 59
* greet
- utter_greet
- utter_how_can_i_help_you
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Good Luck Charm Fruit Infusion"}
- slot{"name": "Good Luck Charm Fruit Infusion"}
- form: form_action_preparation
- slot{"name": "Good Luck Charm Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Darjeeling Standard FOP Black Tea"}
- slot{"name": "Darjeeling Standard FOP Black Tea"}
- form: form_action_availability
- slot{"name": "Darjeeling Standard FOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Darjeeling Standard FOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "Korea", "organic": "Organic"}
- slot{"origin": "Korea", "organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 60
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form: form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 61
* greet
- utter_greet
- utter_how_can_i_help_you
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"requested_slot": "name"}
* form: details
- form: form_action_details
- form{"name": "form_action_details"}
- slot{"requested_slot": "name"}
* form: details{"name": "Spring Harmony White Tea BIO"}
- slot{"name": "Spring Harmony White Tea BIO"}
- form: form_action_details
- slot{"name": "Spring Harmony White Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Spring Harmony White Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Spring Harmony White Tea BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"christmas": "Christmas", "new": "New"}
- slot{"christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"organic": "Not organic", "christmas": "Christmas", "new": "New"}
- slot{"organic": "Not organic", "christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", "Christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"organic": "Not organic", "christmas": "Christmas", "availability": "Available", "new": "New"}
- slot{"organic": "Not organic", "christmas": "Christmas", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", "Christmas", "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Taiwan", "organic": "Not organic", "christmas": "Christmas", "availability": "Available", "new": "New"}
- slot{"origin": "Taiwan", "organic": "Not organic", "christmas": "Christmas", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Taiwan", "Not organic", "Christmas", "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 62
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Not organic", "availability": "Not available"}
- slot{"organic": "Not organic", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", null, "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}

## story 63
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Violet White Tea"}
- slot{"name": "Violet White Tea"}
- form: form_action_similar_products
- slot{"name": "Violet White Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Violet White Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"availability": "Not available"}
- slot{"availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 64
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_deny
- utter_can_i_help_you_again
* preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Organic Spring Herbal Tea"}
- slot{"name": "Organic Spring Herbal Tea"}
- form: form_action_preparation
- slot{"name": "Organic Spring Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Organic Spring Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Organic Spring Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Organic Spring Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 65
* greet
- utter_greet
- utter_how_can_i_help_you
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Darjeeling Himalaya Black Tea"}
- slot{"name": "Darjeeling Himalaya Black Tea"}
- form: form_action_similar_products
- slot{"name": "Darjeeling Himalaya Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Anji White White Tea"}
- slot{"name": "Anji White White Tea"}
- form: form_action_availability
- slot{"name": "Anji White White Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost{"name": "Assam Exquisite TGFOP Black Tea"}
- slot{"name": "Assam Exquisite TGFOP Black Tea"}
- form: form_action_cost
- slot{"name": "Assam Exquisite TGFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Assam Exquisite TGFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Assam Exquisite TGFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Assam Exquisite TGFOP Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Winter Magic Black Tea"}
- slot{"name": "Winter Magic Black Tea"}
- form: form_action_availability
- slot{"name": "Winter Magic Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 66
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* filter{"organic": "Not organic"}
- slot{"organic": "Not organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Not organic", null, null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Not organic", null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Not organic", null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Not organic", null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Not organic", null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Russian Caravan Black Tea mixture"}
- slot{"name": "Russian Caravan Black Tea mixture"}
- form: form_action_similar_products
- slot{"name": "Russian Caravan Black Tea mixture"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* thanks_goodbye
- utter_thanks_goodbye

## story 67
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 25]}
* filter{"origin": "China"}
- slot{"origin": "China"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", "China", null, null, null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", "China", null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 68
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Ceylon", "availability": "Not available"}
- slot{"origin": "Ceylon", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Ceylon", null, null, "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Genmaicha Green Tea"}
- slot{"name": "Genmaicha Green Tea"}
- form: form_action_availability
- slot{"name": "Genmaicha Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Genmaicha Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "India", "availability": "Available"}
- slot{"origin": "India", "availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "India", null, null, "Available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 69
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Organic", "availability": "Not available"}
- slot{"organic": "Organic", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", null, "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 70
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"availability": "Available", "new": "New"}
- slot{"availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Mandarine and Cinnamon Black Tea"}
- slot{"name": "Mandarine and Cinnamon Black Tea"}
- form: form_action_availability
- slot{"name": "Mandarine and Cinnamon Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 71
* filter{"origin": "Ceylon", "new": "New"}
- slot{"origin": "Ceylon", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Ceylon", null, null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* filter{"organic": "Not organic", "new": "New"}
- slot{"organic": "Not organic", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, "Not organic", null, null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, "Not organic", null, null, "New", 5]}
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* thanks_goodbye
- utter_thanks_goodbye

## story 72
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Highland Toffee Black Tea"}
- slot{"name": "Highland Toffee Black Tea"}
- form: form_action_availability
- slot{"name": "Highland Toffee Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Highland Toffee Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 30]}
* goodbye
- utter_goodbye

## story 73
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "China", "new": "New"}
- slot{"origin": "China", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "China", null, null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Kimono Green Tea"}
- slot{"name": "Kimono Green Tea"}
- form: form_action_preparation
- slot{"name": "Kimono Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Kimono Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 25]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 74
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Korea", "availability": "Available"}
- slot{"origin": "Korea", "availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", null, null, "Available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"origin": "Korea", "organic": "Not organic", "christmas": "Not christmas", "availability": "Available", "new": "New"}
- slot{"origin": "Korea", "organic": "Not organic", "christmas": "Not christmas", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", "Not organic", "Not christmas", "Available", "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 75
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 76
* greet
- utter_greet
- utter_how_can_i_help_you
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Yellow Emperor Green Tea"}
- slot{"name": "Yellow Emperor Green Tea"}
- form: form_action_availability
- slot{"name": "Yellow Emperor Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 77
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Souvenir de Printemps"}
- slot{"name": "Souvenir de Printemps"}
- form: form_action_ingredients
- slot{"name": "Souvenir de Printemps"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Souvenir de Printemps"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"availability": "Not available"}
- slot{"availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, "Not available", null, 30]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Herbal Teas"}
- slot{"category": "Herbal Teas"}
- form: form_action_search
- slot{"category": "Herbal Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 25]}
* thanks_goodbye
- utter_thanks_goodbye

## story 78
* preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation
- form: form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"requested_slot": "name"}
* form: preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Vanilla Bourbon Black Tea"}
- slot{"name": "Vanilla Bourbon Black Tea"}
- form: form_action_preparation
- slot{"name": "Vanilla Bourbon Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 25]}
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Magic Relax Herbal Tea"}
- slot{"name": "Magic Relax Herbal Tea"}
- form: form_action_similar_products
- slot{"name": "Magic Relax Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Magic Relax Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Magic Relax Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Green Rooibos Peach"}
- slot{"name": "Green Rooibos Peach"}
- form: form_action_similar_products
- slot{"name": "Green Rooibos Peach"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_details
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: details{"name": "Lady Camilla Herbal Tea"}
- slot{"name": "Lady Camilla Herbal Tea"}
- form: form_action_details
- slot{"name": "Lady Camilla Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "India", "christmas": "Christmas", "new": "New"}
- slot{"origin": "India", "christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", "India", null, "Christmas", null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", "India", null, "Christmas", null, "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", "India", null, "Christmas", null, "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", "India", null, "Christmas", null, "New", 15]}
* thanks_goodbye
- utter_thanks_goodbye

## story 79
* filter{"organic": "Not organic"}
- slot{"organic": "Not organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* availability{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_availability
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: availability{"name": "Apple Strudel Black Tea"}
- slot{"name": "Apple Strudel Black Tea"}
- form: form_action_availability
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Apple Strudel Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients{"name": "Green Mate Herbal Tea"}
- slot{"name": "Green Mate Herbal Tea"}
- form_action_ingredients
- slot{"name": "Green Mate Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Green Mate Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 80
* greet
- utter_greet
- utter_how_can_i_help_you
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products
- form: form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Korakundah FOP Organic Green Tea"}
- slot{"name": "Korakundah FOP Organic Green Tea"}
- form: form_action_similar_products
- slot{"name": "Korakundah FOP Organic Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Earl Grey Special Soft Black Tea (without thein)"}
- slot{"name": "Earl Grey Special Soft Black Tea (without thein)"}
- form: form_action_similar_products
- slot{"name": "Earl Grey Special Soft Black Tea (without thein)"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 81
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "China", "new": "New"}
- slot{"origin": "China", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "China", null, null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* filter{"christmas": "Christmas", "availability": "Not available"}
- slot{"christmas": "Christmas", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, "Christmas", "Not available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, "Christmas", "Not available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, "Christmas", "Not available", null, 10]}
* goodbye
- utter_goodbye

## story 82
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Irish Breakfast Black Tea"}
- slot{"name": "Irish Breakfast Black Tea"}
- form: form_action_ingredients
- slot{"name": "Irish Breakfast Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation{"name": "Matcha green Tea Roses"}
- slot{"name": "Matcha green Tea Roses"}
- form_action_preparation
- slot{"name": "Matcha green Tea Roses"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Matcha green Tea Roses"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", null, null, null, 30]}
* filter{"organic": "Organic", "christmas": "Not christmas", "new": "New"}
- slot{"organic": "Organic", "christmas": "Not christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", "Not christmas", null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", "Not christmas", null, "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", "Not christmas", null, "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, "Organic", "Not christmas", null, "New", 15]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 83
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Black Teas"}
- slot{"category": "Black Teas"}
- form: form_action_search
- slot{"category": "Black Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, null, null, null, null, 30]}
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost
- form: form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost{"name": "Yellow Emperor Green Tea"}
- slot{"name": "Yellow Emperor Green Tea"}
- form: form_action_cost
- slot{"name": "Yellow Emperor Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Yellow Emperor Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details{"name": "Garden Eden Fruit Infusion"}
- slot{"name": "Garden Eden Fruit Infusion"}
- form_action_details
- slot{"name": "Garden Eden Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"name": "Garden Eden Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Organic", "availability": "Not available"}
- slot{"organic": "Organic", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, "Organic", null, "Not available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Black Teas", null, "Organic", null, "Not available", null, 5]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 84
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Organic", "new": "New"}
- slot{"organic": "Organic", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form: form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* filter{"christmas": "Christmas", "availability": "Available", "new": "New"}
- slot{"christmas": "Christmas", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, "Christmas", "Available", "New", 30]}
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"requested_slot": "name"}
* form: details{"name": "Nepal Jun Chiyabari Oolong BIO"}
- slot{"name": "Nepal Jun Chiyabari Oolong BIO"}
- form: form_action_details
- slot{"name": "Nepal Jun Chiyabari Oolong BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Nepal Jun Chiyabari Oolong BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Nepal Jun Chiyabari Oolong BIO"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "Tanzania", "christmas": "Christmas", "availability": "Available", "new": "New"}
- slot{"origin": "Tanzania", "christmas": "Christmas", "availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", "Tanzania", null, "Christmas", "Available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", "Tanzania", null, "Christmas", "Available", "New", 5]}
* goodbye
- utter_goodbye

## story 85
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Tanzania", "christmas": "Not christmas", "availability": "Not available"}
- slot{"origin": "Tanzania", "christmas": "Not christmas", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Tanzania", null, "Not christmas", "Not available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* thanks_goodbye
- utter_thanks_goodbye

## story 86
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 20]}
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Magical Christmas fruit infusion"}
- slot{"name": "Magical Christmas fruit infusion"}
- form: form_action_similar_products
- slot{"name": "Magical Christmas fruit infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Magical Christmas fruit infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_preparation
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: preparation{"name": "Gyokuro Green Tea"}
- slot{"name": "Gyokuro Green Tea"}
- form: form_action_preparation
- slot{"name": "Gyokuro Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Gyokuro Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 87
* filter{"organic": "Not organic"}
- slot{"organic": "Not organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 88
* filter{"origin": "Taiwan", "organic": "Organic"}
- slot{"origin": "Taiwan", "organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Taiwan", "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 89
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 25]}
* search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_deny
- utter_can_i_help_you_again
* details{"name": "Sikkim - Piantagione Temi Black Tea"}
- slot{"name": "Sikkim - Piantagione Temi Black Tea"}
- form_action_details
- slot{"name": "Sikkim - Piantagione Temi Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"name": "Sikkim - Piantagione Temi Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"name": "Sikkim - Piantagione Temi Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Not organic", "availability": "Not available"}
- slot{"organic": "Not organic", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, "Not organic", null, "Not available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, "Not organic", null, "Not available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, "Not organic", null, "Not available", null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, "Not organic", null, "Not available", null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, "Not organic", null, "Not available", null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, "Not organic", null, "Not available", null, 25]}
* filter{"origin": "Korea", "organic": "Not organic", "availability": "Not available"}
- slot{"origin": "Korea", "organic": "Not organic", "availability": "Not available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", "Korea", "Not organic", null, "Not available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", "Korea", "Not organic", null, "Not available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", "Korea", "Not organic", null, "Not available", null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", "Korea", "Not organic", null, "Not available", null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", "Korea", "Not organic", null, "Not available", null, 20]}
* thanks_goodbye
- utter_thanks_goodbye

## story 90
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"organic": "Not organic", "christmas": "Christmas", "new": "New"}
- slot{"organic": "Not organic", "christmas": "Christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", "Christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"organic": "Not organic", "christmas": "Not christmas", "new": "New"}
- slot{"organic": "Not organic", "christmas": "Not christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", "Not christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_similar_products
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: similar_products{"name": "Winter Fairytale Fruit Infusion"}
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form: form_action_similar_products
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Winter Fairytale Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Organic", "christmas": "Not christmas", "new": "New"}
- slot{"organic": "Organic", "christmas": "Not christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", "Not christmas", null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* cost
- form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost{"name": "unknown"}
- slot{"name": "unknown"}
- form: form_action_cost
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: cost
- form: form_action_cost
- form{"name": "form_action_cost"}
- slot{"requested_slot": "name"}
* form: cost{"name": "Green Rooibos Vanilla and Lemon"}
- slot{"name": "Green Rooibos Vanilla and Lemon"}
- form: form_action_cost
- slot{"name": "Green Rooibos Vanilla and Lemon"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 91
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"christmas": "Christmas"}
- slot{"christmas": "Christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, "Christmas", null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* filter{"organic": "Not organic", "christmas": "Christmas"}
- slot{"organic": "Not organic", "christmas": "Christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", "Christmas", null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Fruit Infusions"}
- slot{"category": "Fruit Infusions"}
- form: form_action_search
- slot{"category": "Fruit Infusions"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, null, null, 15]}
* filter{"availability": "Available"}
- slot{"availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, "Available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, "Available", null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, "Available", null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, "Available", null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, "Available", null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Fruit Infusions", null, null, null, "Available", null, 25]}
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Magic Relax Herbal Tea"}
- slot{"name": "Magic Relax Herbal Tea"}
- form: form_action_ingredients
- slot{"name": "Magic Relax Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 92
* greet
- utter_greet
- utter_how_can_i_help_you
* ingredients
- form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Pi Lou Chun Dong Ting Green Tea"}
- slot{"name": "Pi Lou Chun Dong Ting Green Tea"}
- form: form_action_ingredients
- slot{"name": "Pi Lou Chun Dong Ting Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Pi Lou Chun Dong Ting Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"origin": "Korea", "new": "New"}
- slot{"origin": "Korea", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Korea", null, null, null, "New", 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* details{"name": "Mini Tuocha China Pu Erh Black Tea"}
- slot{"name": "Mini Tuocha China Pu Erh Black Tea"}
- form_action_details
- slot{"name": "Mini Tuocha China Pu Erh Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Mini Tuocha China Pu Erh Black Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "unknown"}
- slot{"category": "unknown"}
- form: form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again

## story 93
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "Herbal Teas"}
- slot{"category": "Herbal Teas"}
- form_action_search
- slot{"category": "Herbal Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 5]}
* search_deny
- utter_can_i_help_you_again
* cost{"name": "Happy Fruits Fruit Infusion"}
- slot{"name": "Happy Fruits Fruit Infusion"}
- form_action_cost
- slot{"name": "Happy Fruits Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Slim Plus Herbal Tea"}
- slot{"name": "Slim Plus Herbal Tea"}
- form: form_action_ingredients
- slot{"name": "Slim Plus Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"christmas": "Not christmas", "new": "New"}
- slot{"christmas": "Not christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 25]}
* filter{"christmas": "Not christmas", "new": "New"}
- slot{"christmas": "Not christmas", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, "Not christmas", null, "New", 5]}
* goodbye
- utter_goodbye

## story 94
* greet
- utter_greet
- utter_how_can_i_help_you
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Good Luck Charm Fruit Infusion"}
- slot{"name": "Good Luck Charm Fruit Infusion"}
- form: form_action_availability
- slot{"name": "Good Luck Charm Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"availability": "Available"}
- slot{"availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, null, null, "Available", null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* goodbye
- utter_goodbye

## story 95
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 96
* greet
- utter_greet
- utter_how_can_i_help_you
* preparation{"name": "Sparks of Joy Fruit Infusion"}
- slot{"name": "Sparks of Joy Fruit Infusion"}
- form_action_preparation
- slot{"name": "Sparks of Joy Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* similar_products
- form_action_similar_products
- form{"name": "form_action_similar_products"}
- slot{"name": "Sparks of Joy Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Sparks of Joy Fruit Infusion"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Not organic"}
- slot{"organic": "Not organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Not organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Rooibos Wild Pure"}
- slot{"name": "Rooibos Wild Pure"}
- form: form_action_ingredients
- slot{"name": "Rooibos Wild Pure"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"organic": "Organic"}
- slot{"organic": "Organic"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, null, "Organic", null, null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Herbal Teas"}
- slot{"category": "Herbal Teas"}
- form: form_action_search
- slot{"category": "Herbal Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 5]}
* goodbye
- utter_goodbye

## story 97
* greet
- utter_greet
- utter_how_can_i_help_you
* filter{"origin": "Tanzania", "organic": "Organic", "christmas": "Not christmas"}
- slot{"origin": "Tanzania", "organic": "Organic", "christmas": "Not christmas"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": [null, "Tanzania", "Organic", "Not christmas", null, null, 0]}
- followup{"name": "form_action_search"}
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "White Teas"}
- slot{"category": "White Teas"}
- form: form_action_search
- slot{"category": "White Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["White Teas", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* details{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_details
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: details{"name": "Green Rooibos Classic"}
- slot{"name": "Green Rooibos Classic"}
- form: form_action_details
- slot{"name": "Green Rooibos Classic"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "unknown"}
- slot{"category": "unknown"}
- form_action_search
- slot{"category": null}
- slot{"requested_slot": "category"}
* form: search
- form: form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Rooibos"}
- slot{"category": "Rooibos"}
- form: form_action_search
- slot{"category": "Rooibos"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Rooibos", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* details{"name": "Violet White Tea"}
- slot{"name": "Violet White Tea"}
- form_action_details
- slot{"name": "Violet White Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* preparation
- form_action_preparation
- form{"name": "form_action_preparation"}
- slot{"name": "Violet White Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again

## story 98
* greet
- utter_greet
- utter_how_can_i_help_you
* search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability
- form: form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Slim Plus Herbal Tea"}
- slot{"name": "Slim Plus Herbal Tea"}
- form: form_action_availability
- slot{"name": "Slim Plus Herbal Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* ingredients{"name": "unknown"}
- slot{"name": "unknown"}
- form_action_ingredients
- slot{"name": null}
- slot{"requested_slot": "name"}
* form: ingredients
- form: form_action_ingredients
- form{"name": "form_action_ingredients"}
- slot{"requested_slot": "name"}
* form: ingredients{"name": "Gyokuro Green Tea"}
- slot{"name": "Gyokuro Green Tea"}
- form: form_action_ingredients
- slot{"name": "Gyokuro Green Tea"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* search{"category": "Matcha and Flower Teas"}
- slot{"category": "Matcha and Flower Teas"}
- form_action_search
- slot{"category": "Matcha and Flower Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Matcha and Flower Teas", null, null, null, null, null, 20]}
* search_deny
- utter_can_i_help_you_again
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Oolong"}
- slot{"category": "Oolong"}
- form: form_action_search
- slot{"category": "Oolong"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, null, null, 30]}
* filter{"availability": "Available", "new": "New"}
- slot{"availability": "Available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Oolong", null, null, null, "Available", "New", 30]}
* search_deny
- utter_can_i_help_you_again
* thanks_goodbye
- utter_thanks_goodbye

## story 99
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 30]}
* search_deny
- utter_can_i_help_you_again
* filter{"availability": "Not available", "new": "New"}
- slot{"availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, "Not available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, "Not available", "New", 5]}
* search_deny
- utter_can_i_help_you_again
* filter{"christmas": "Christmas", "availability": "Not available", "new": "New"}
- slot{"christmas": "Christmas", "availability": "Not available", "new": "New"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, "Christmas", "Not available", "New", 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, "Christmas", "Not available", "New", 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, "Christmas", "Not available", "New", 10]}
* search_deny
- utter_can_i_help_you_again
* goodbye
- utter_goodbye

## story 100
* greet
- utter_greet
- utter_how_can_i_help_you
* search
- form_action_search
- form{"name": "form_action_search"}
- slot{"requested_slot": "category"}
* form: search{"category": "Gold Tea Selection"}
- slot{"category": "Gold Tea Selection"}
- form: form_action_search
- slot{"category": "Gold Tea Selection"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, null, null, null, 10]}
* availability
- form_action_availability
- form{"name": "form_action_availability"}
- slot{"requested_slot": "name"}
* form: availability{"name": "Golden Nepal Maloom Black Tea Bio"}
- slot{"name": "Golden Nepal Maloom Black Tea Bio"}
- form: form_action_availability
- slot{"name": "Golden Nepal Maloom Black Tea Bio"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* details
- form_action_details
- form{"name": "form_action_details"}
- slot{"name": "Golden Nepal Maloom Black Tea Bio"}
- form{"name": null}
- slot{"requested_slot": null}
- utter_can_i_help_you_again
* filter{"christmas": "Not christmas", "availability": "Available"}
- slot{"christmas": "Not christmas", "availability": "Available"}
- action_filter
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, "Not christmas", "Available", null, 0]}
- followup{"name": "action_suggest"}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Gold Tea Selection", null, null, "Not christmas", "Available", null, 5]}
* search_deny
- utter_can_i_help_you_again
* search{"category": "Herbal Teas"}
- slot{"category": "Herbal Teas"}
- form_action_search
- slot{"category": "Herbal Teas"}
- slot{"category": null}
- slot{"origin": null}
- slot{"organic": null}
- slot{"christmas": null}
- slot{"availability": null}
- slot{"new": null}
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 0]}
- form: followup{"name": "action_suggest"}
- form{"name": null}
- slot{"requested_slot": null}
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 5]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 10]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 15]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 20]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 25]}
* search_affirm
- action_suggest
- slot{"name": null}
- slot{"unfeat_search_settings": ["Herbal Teas", null, null, null, null, null, 30]}
* goodbye
- utter_goodbye

