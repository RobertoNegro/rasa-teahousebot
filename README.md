# Commands

- Compile NLU dataset: \
`cd data/chatette && python -m chatette -a rasa-md main.chatette && cd ../.. # /data/chatette/output/train/output.md -> /data/nlu.md`

- Compile stories: \
`python story_generator.py`\
`mv stories.txt data/stories.md`

- Run docker-composer: \
`sudo docker-compose up -d`

- Stop docker-composer: \
`sudo docker-compose down`

- Build action server (if version change, must be changed on \etc\rasa files as well): \
`docker build . -t teahouseactions:1.0`

- ngrok start: \
`ngrok http 5005`

- Google Assistant: \
`# update ngrok address on action.json` \
`gactions update --action_package action.json --project tea-house-bot` \
`gactions test --action_package action.json --project tea-house-bot`

- Alexa: \
`# update address on https://developer.amazon.com/alexa/console/ask`


