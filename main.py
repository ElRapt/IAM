import json
import tweepy
import asyncio
import logging
import threading

logging.basicConfig(level=logging.INFO)

async def main():
    credentials = json.load(open("credentials.json"))
    dictionary = json.load(open("dictionary.json"))

    counter = 0
    counter_lock = threading.Lock()

    consumer_key = credentials["api_key"]
    consumer_secret = credentials["api_key_secret"]
    access_token = credentials["access_token"]
    access_token_secret = credentials["access_token_secret"]
    bearer_token = credentials["bearer_token"]

    client = tweepy.Client(
        bearer_token=bearer_token,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    while counter < len(dictionary):
        message = "I am " + dictionary[counter]

        try:
            client.create_tweet(text=message)
            logging.info(f"Successfully tweeted: {message}")
        except tweepy.TweepError as e:
            logging.error(f"Error while sending tweet: {e}")
            await asyncio.sleep(60)  # Wait 1 minute before trying again

        with counter_lock:
            counter += 1

        await asyncio.sleep(30 * 60)  # Wait 30 minutes before sending the next tweet

if __name__ == '__main__':
    asyncio.run(main())
