import json
import tweepy

credentials = json.load(open("credentials.json"))

# Remplacez les valeurs suivantes par vos propres clés d'API Twitter
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# Authentification avec les clés d'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Création de l'objet API
api = tweepy.API(auth)

# Exemple d'utilisation : publier un tweet
tweet_text = "Hello, Twitter!"
api.update_status(tweet_text)
