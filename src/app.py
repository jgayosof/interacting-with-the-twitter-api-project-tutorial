import os
import re
import tweepy
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

# Constants
api_key = os.getenv('api_key')
api_secret_key = os.getenv('api_secret_key')
bearer_token = os.getenv('bearer_token')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

client = tweepy.Client(bearer_token=bearer_token,
                        consumer_key=api_key,
                        consumer_secret=api_secret_key,
                        access_token=access_token,
                        access_token_secret=access_token_secret,
                        return_type=requests.Response,
                        wait_on_rate_limit=True)

query = '#100daysofcode (pandas OR python) -is:retweet'

tweets = client.search_recent_tweets(query=query,
                                    tweet_fields=['author_id','created_at','lang'],
                                    max_results=100)

# Dict of Tweets:
tweets_dic = tweets.json()

# Tweets Data
tweets_data = tweets_dic['data']

# Tweets Data to df
df = pd.json_normalize(tweets_data)

# df to .csv
df.to_csv('Tweets.csv')

def word_in_text(word, text) :
    word = word.lower()
    text = text.lower()
    return (word in text)

counter_py = counter_pd = 0
for index, row in df.iterrows() :
    text = row['text']
    if word_in_text('Python', row['text']) :
        counter_py += 1
    if word_in_text('Pandas', row['text']) :
        counter_pd += 1
    
print(f'#Python: {counter_py}, #Pandas: {counter_pd} ')


# Seaborn Style
sns.set_theme(style="ticks", color_codes=True)

words = ['Python','Pandas']

ax = sns.barplot(words, [counter_py, counter_pd])
ax.set(ylabel='Count',title='Python and pandas tweets')
plt.show()