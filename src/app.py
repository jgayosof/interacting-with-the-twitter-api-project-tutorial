import os
import tweepy
import requests
#from dotenv import load_dotenv

# Constants
userkey = 'UZAXZQqEtla469WNmAj'
keysecret = 'RwXren3h8VRnKv1Ss04w8yIAKYFeDDrajvFvhmE8gQKYADLF4y'
bearertoken = 'AAAAAAAAAAAAAAAAAAAAADqGdwEAAAAA7NZBVDtY3NEYAExMTFs82eZdOmw%3D2EbV3U01PufquuECWLK32TobOeU7gLeOAM3yfHK2UfXAwra13t'

api_key = 'rlAcKXUZAXZQqEtla469WNmAj'
api_secret_key = 'RwXren3h8VRnKv1Ss04w8yIAKYFeDDrajvFvhmE8gQKYADLF4y'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAADqGdwEAAAAA7NZBVDtY3NEYAExMTFs82eZdOmw%3D2EbV3U01PufquuECWLK32TobOeU7gLeOAM3yfHK2UfXAwra13t'
access_token = '1537937734836187136-uG3LND2R6kyhZowu7TsfPbJkaKFNAo'
access_token_secret = 'UIH9hwJNWmqJAyRgsLE5KsTdzdbFrN8tb5dAMqVPe6WcT'

# load the .env file variables
#load_dotenv()

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

"""
import tweepy
import requests

userkey = "mOpvOOLNUw60UOELhaZXi7GYX"
keysecret = "dEF8kH755DFetPnAlbmKQxXS30AnMRlvzFtL8rKgWUEuRT9cbE"
bearertoken = "AAAAAAAAAAAAAAAAAAAAACCGdwEAAAAAeFVrFPHC9stE%2FMKgKvXorDGXoIk%3DSuVBXEOqhluiOUM73lKmba7YmsF2kppL3j6wLcMDooDoXmHfCq"

client = tweepy.Client(bearer_token=bearertoken,
consumer_key="MRN0czOUV05gdIYPG6VGO3Zf0f6gLQYSTvsT3qB2yNqxM",
consumer_secret="AAAAAAAAAAAAAAAAAAAAACCGdwEAAAAAeFVrFPHC9stE%2FMKgKvXorDGXoIk%3DSuVBXEOqhluiOUM73lKmba7YmsF2kppL3j6wLcMDooDoXmHfCq",
access_token="1344770233442193409-FE91Cu5J5P2oUIRGozq8UwySXMh7jH",
access_token_secret="1344770233442193409-FE91Cu5J5P2oUIRGozq8UwySXMh7jH",
return_type=requests.Response,
wait_on_rate_limit=True
)
query = '#100daysofcode (pandas OR python) -is:retweet'
"""
