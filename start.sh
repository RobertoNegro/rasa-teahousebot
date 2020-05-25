rasa run actions
rasa run -m models --enable-api --endpoints endpoints.yml
ngrok http 5005

# Google
# update ngrok address on action.json
gactions update --action_package action.json --project tea-house-bot
gactions test --action_package action.json --project tea-house-bot

# Alexa
# update address on https://developer.amazon.com/alexa/console/ask