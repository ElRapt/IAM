import json
import tweepy
import time

credentials = json.load(open("credentials.json"))
dictionary = json.load(open("dictionary.json"))


counter = 0

# Loading API keys
consumer_key = credentials["api_key"]
consumer_secret = credentials["api_key_secret"]
access_token = credentials["access_token"]
access_token_secret = credentials["access_token_secret"]
bearer_token = credentials["bearer_token"]

# Creating client with necessary tokens
client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

# Creating tweet
#response = client.create_tweet(text="Hello, Twitter!")

# Printing response
#print(response)

while counter < len(dictionary):
    message = "I am " + dictionary[counter]
    try:
        client.create_tweet(text=message)
    except tweepy.TweepError as e:
        print("Erreur lors de l'envoi du tweet :", e)
        time.sleep(60)  # Attend 1 minute avant de réessayer

    counter +=1
    time.sleep(10)  # Attend 30 minutes avant d'envoyer le prochain tweet
