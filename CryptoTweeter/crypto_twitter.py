import os
import time
import requests
import tweepy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
CRYPTO_API_URL = os.getenv('CRYPTO_API_URL')

# Debug: Print the loaded environment variables to verify
print(f"TWITTER_API_KEY: {TWITTER_API_KEY}")
print(f"TWITTER_API_SECRET_KEY: {TWITTER_API_SECRET_KEY}")
print(f"TWITTER_ACCESS_TOKEN: {TWITTER_ACCESS_TOKEN}")
print(f"TWITTER_ACCESS_TOKEN_SECRET: {TWITTER_ACCESS_TOKEN_SECRET}")
print(f"CRYPTO_API_URL: {CRYPTO_API_URL}")

def get_crypto_price(url):
    response = requests.get(url)
    data = response.json()
    return data

def format_tweet(data):
    tweets = []
    for crypto in data:
        name = crypto.get('name', 'Unknown')
        price = crypto.get('current_price', 'N/A')
        tweets.append(f"The current price of {name} is ${price:.2f} USD.")
    return "\n".join(tweets)

def create_twitter_client():
    auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print("Error during authentication", e)
    return api

def post_tweet(api, message):
    api.update_status(message)
    print("Tweet posted:", message)

def crypto_price_tracker():
    api = create_twitter_client()
    
    while True:
        try:
            crypto_data = get_crypto_price(CRYPTO_API_URL)
            tweet = format_tweet(crypto_data)
            post_tweet(api, tweet)
        except Exception as e:
            print("Error fetching price or posting tweet:", e)
        
        time.sleep(3600)  # Wait for 1 hour before posting the next update

if __name__ == "__main__":
    crypto_price_tracker()
