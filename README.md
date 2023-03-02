# AI-Podcast-Creator
A Python script to generate an audio podcast episode using APIs from OpenAI (ChatGPT) and ElevenLabs.

Note that AI APIs are at an early stage and may change over time.

The Python file uses the Japan Times RSS feed but others should work too, e.g. NPR, BBC News, etc.

## Requirements
* OpenAI account and API key: https://platform.openai.com/account/api-keys
* ElevenLabs account and API key: https://beta.elevenlabs.io

## Installation
1. Download the files in this repository to a local directory.
2. Make a proper copy of the example environment variables file:
```
$ cp .env.example .env
```
3. Edit the new `.env` file to add your API keys, for example:
```
$ nano .env
```
4. Install any requirements using pip and the `requirements.txt` file. You may need to use `pip3` instead of `pip`.
```
$ pip install -r requirements.txt
```
5. Run the script and wait for it to generate an MP3 file. You may need to use `python3` instead of `python`.
```
$ python create_podcast.py
```
6. Hopefully it worked! If not, check you have enough credits for OpenAI and/or ElevenLabs.
