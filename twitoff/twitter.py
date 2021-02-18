import tweepy
from models import DB, Tweet, User
import spacy
#to access enviroment variables
import os
twitter_key= os.environ["TWITTER_API_KEY"]
twitter_key_secret = os.environ["TWITTER_API_KEY_SECRET"]
twitter_auth = tweepy.OAuthHandler(twitter_key, twitter_key_secret)
twitter = tweepy.API(twitter_auth)

nlp = spacy.load("en_core_web_sm")

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).vector

def add_or_update_users(handle):
    try:
        twitter_user = twitter.get_user(handle)
        db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id, name=handle)
        DB.session.add(db_user)


        tweets = twitter_user.timeline(
            count=200, exclude_replies=True, include_rts=False, tweet_mode="extended"
        )

        for tweet in tweets:
            vectorize_tweet = vectorize_tweet(tweet.full_text)
            db_tweet = Tweet(id=tweet.id, text= tweet.full_text, vect= vectorize_tweet)
            db_user.twwets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print(e)
    
    else:
        DB.session.commit()
