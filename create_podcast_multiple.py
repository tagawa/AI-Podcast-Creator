import json
from dotenv import load_dotenv
import feedparser
import openai
import os
import requests

# Make sure you've added your API keys to the .env environment variables file.
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

# Uncomment or add your preferred feeds here.
news_feed1 = "https://feeds.npr.org/1001/rss.xml" # NPR News
news_feed2 = "http://feeds.bbci.co.uk/news/rss.xml?edition=int" # BBC News
news_feed3 = "https://www.japantimes.co.jp/news_category/national/feed/" # Japan Times News


print("## Getting RSS feed content…")

feeds = [news_feed1, news_feed2, news_feed3]
stories = ""
stories_limit_per_feed = 5 # The maximum number of news stories to include per feed.

# Loop through each feed
for feed_url in feeds:
    feed = feedparser.parse(feed_url)
    
    # Loop through each item in the RSS feed and append each title and description to the "stories" string.
    for item in feed.entries[:stories_limit_per_feed]:
        stories = stories + " News Story: " + item.title + ". " + item.description

print(stories)


print("## Generating ChatGPT output…")

# See also OpenAI's ChatGPT API guide: https://platform.openai.com/docs/guides/chat
chat_output = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  messages = [{
    "role": "user",
    "content": "Please rewrite the following news headlines and summaries in a discussion way, as though someone is talking about them one by one on a one-off podcast in a non-judgemental way and with no follow-on discussion, although there should be a final closing greeting: " + stories
  }]
)
chat_content = chat_output.choices[0].message.content

print(chat_content)


print("## Generating audio output…")

# See also the ElevenLabs API docs: https://api.elevenlabs.io/docs
voice_id = "21m00Tcm4TlvDq8ikWAM" # The voice ID for "Rachel"
audio_output = requests.post(
  "https://api.elevenlabs.io/v1/text-to-speech/" + voice_id,
  data = json.dumps({
    "text": chat_content,
    "voice_settings": {
      "stability": 0.2, # The lower the number, the more expressive the voice.
      "similarity_boost": 0
    }
  }),
  headers = {
    "Content-Type": "application/json",
    "xi-api-key": elevenlabs_api_key,
    "accept": "audio/mpeg"
  },
)

# Check for a valid audio output, otherwise print the error message.
if audio_output.status_code == 200:
  with open('test.mp3', 'wb') as output_file:
    output_file.write(audio_output.content)
else:
  print(audio_output.text)

print("## All processing complete.")
