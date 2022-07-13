import os
import tweepy
import requests
from dotenv import load_dotenv

load_dotenv()

# Constants
api_key = os.getenv('api_key')
api_secret_key = os.getenv('api_secret_key')
bearer_token = os.getenv('bearer_token')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

client = tweepy.Client(
                        bearer_token=bearer_token,
                        consumer_key=api_key,
                        consumer_secret=api_secret_key,
                        access_token=access_token,
                        access_token_secret=access_token_secret,
                        return_type=requests.Response(),
                        wait_on_rate_limit=True
                        )

query = '#100daysofcode (pandas OR python) -is:retweet'

tweets = client.search_recent_tweets(query=query,
                                    tweet_fields=['author_id','created_at','lang'],
                                    max_results=100
                                    )

