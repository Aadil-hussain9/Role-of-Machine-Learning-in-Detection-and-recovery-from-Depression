from ast import keyword
import configparser
from itertools import count
from numpy import column_stack
import tweepy
# from server import twitterUsername
# import server
import pandas as pd
import nltk
import pickle
import string
import numpy as np
import re
import pandas as pd
# import seaborn as sns
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


conf = configparser.ConfigParser()
conf.read('config (1).ini')

api_key = conf['twitter']['api_key']
api_key_secret = conf['twitter']['api_key_secret']

access_token = conf['twitter']['access_key']
access_token_secret = conf['twitter']['access_key_secret']

#authentication

autho = tweepy.OAuth1UserHandler(api_key,api_key_secret)
autho.set_access_token(access_token,access_token_secret)

api = tweepy.API(autho)
#particular user tweets

# user = server.twitterUsername
# user = 'hellome639'
# # user = input('Enter User name of Twitter')
# # limit = 10
#
# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
#
# #dataframe
#
# colums = ['Tweet']
# data = []
#
# for tweet in tweets:
#      data.append([tweet.full_text])
#
# df = pd.DataFrame(data, columns=colums)
# # print(df.values)
# listToStr = ' '.join([str(elem) for elem in df.values])
# print(listToStr)

# username = 'narendramodi'
def extracttweet(username):
    try:
        api.get_user(screen_name=username)
        tweets = api.user_timeline(screen_name=username, count=10, tweet_mode='extended')

        colums = ['Tweet']
        data = []
        for tweet in tweets:
         data.append([tweet.full_text])
        df = pd.DataFrame(data, columns=colums)
        listToStr = ' '.join([str(elem) for elem in df.values])
        return listToStr
    except:
        return 404


# user = api.get_user('narendramodi')
# try:
#   user = api.get_user(screen_name='narendramodi')
#   print(user.name)
# except:
#   print("An exception occurred")


# if __name__ == "__main__":
#     user = 'dshkhi'
#     str = extracttweet(user)
#     print(str)
#     if (len(str) == 0):
#         print("Yes emoty")
#     else:
#         print("No")


















# print(df.shape)
# df.to_csv('tweets.csv')

# content = df.Tweet
# message = content.values

# string.punctuation

#---------------------------------
# def remove_punct(text):
#   text = "".join([char for char in text if char not in string.punctuation])
#   text = re.sub('[0-9]+', '', text)
#   return text
# dfr = df['Tweet'].apply(lambda x: remove_punct(x))
# # print(dfr)
#
# #------------------------------------
#
# def tokenization(text):
#   text = " ".join(re.split('\W+', text))
#   return text
# Tokenised_tweet = df['Tweet'].apply(lambda x: tokenization(x))
# # print(Tokenised_tweet.shape)
# flat_array1 = Tokenised_tweet.values
# flat_array = flat_array1.flatten()
# # print(flat_array)
# #
# listToStr = ' '.join([str(elem) for elem in flat_array])
# print(listToStr)
# #--------------------------------------
# stopword = nltk.corpus.stopwords.words('english')
# def remove_stopwords(text):
#   text = "".join([word for word in text if not word.lower() in stopword])
#   return text
#
#
# dfer = df['listToStr'].apply(lambda x: remove_stopwords(x))