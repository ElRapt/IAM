import json
import asyncio
import logging
from typing import Any
from tweepy import Client

logging.basicConfig(level=logging.INFO)

async def tweet_word(client: Client, dictionary: list[str], counter: int) -> None:
    """Tweet a word from the dictionary."""
    try:
        word = dictionary[counter]
        logging.info(f"Tweeting the word: {word}")
        # Assume tweet() is an async method
        await client.tweet(word)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

async def main():
    credentials = json.load(open("credentials.json"))
    dictionary = json.load(open("dictionary.json"))
    counter = 0

    client = Client(
        bearer_token=credentials["bearer_token"],
        consumer_key=credentials["api_key"],
        consumer_secret=credentials["api_key_secret"],
        access_token=credentials["access_token"],
        access_token_secret=credentials["access_token_secret"],
    )

    while True:
        await tweet_word(client, dictionary, counter)
        counter = (counter + 1) % len(dictionary)
        await asyncio.sleep(60)  # Sleep for 60 seconds

if __name__ == '__main__':
    asyncio.run(main())
