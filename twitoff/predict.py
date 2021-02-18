#from sklearn.Linear_models import LogisticRegression
from models import User
import numpy as np
from twitter import vectorize_tweet

def predict_user(user1_handle, user2_handle, tweet_text):
    user1 = User.query.filter(User.name == user1_handle).one()
    user2 = User.query.filter(User.name == user2_handle).one()
    ## List comprehension to build a list of vector attributes for user 1
    user1_vectors = np.array([tweet.vect for tweet in user1.tweets])
    user2_vectors = np.array([tweet.vect for tweet in user2.tweets])

    #combine into a one two dimensional array
    vects_X = np.vstack([user1_vectors, user2_vectors])
    labels_y = np.concatenate([np.zeros(len(user1.tweets)), np.ones(len(user2.tweets))])
    model = LogisticRegression()
    model.fit(vects_X, labels_y)
    y_pred = model.predict(vectorize_tweet(tweet_text))
    return y_pred

