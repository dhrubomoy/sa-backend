import tweepy, json, re, random
from sentiment_analysis import models
from nltk.tokenize import word_tokenize
from .sentiment_analysis_utils.textblob_algorithms import NaiveBayesAlg, PatternLibAlg
from .sentiment_analysis_utils.rnn_model import RnnWord2Vec, RnnGloVe


class TwitterAnalysisUtil():

    def __init__(self):
        self.api = self.get_api()
        self.nba = NaiveBayesAlg()
        self.pattern = PatternLibAlg()
        self.rnn_w2v = RnnWord2Vec()
        self.rnn_gloVe = RnnGloVe()

    def get_api(self):
        # TODO: Use environment variable instead of hardcoding values 
        # consumer_key = 'YOUR CONSUMER KEY'
        # consumer_secret = 'YOUR CONSUMER SECRET'
        # access_token = 'YOUR ACCESS TOKEN'
        # access_token_secret = 'YOUR ACCESS TOKEN SECRET'
        consumer_key = 'SE2fGPkDDLdGCENDGhHVjXvQM'
        consumer_secret = '60lIjikPSdLVeOmuXWoLOox1xwG2nT23aweejH3YBcpzlT42kj'
        access_token = '1012363633-Q1MQWhXnTCROIhdDnmhlUytvLLN8vRNkfVLyqsu'
        access_token_secret = 'yYtpaoGmkjB2imLj2i4hrxwRqzjTU84r3dbSB66x6Ghol'
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        return api

    def get_search_result(self, query):
        all_data = []
        for tweet in tweepy.Cursor(
                self.api.search, 
                q=query,
                tweet_mode='extended', 
                lang="en"
            ).items(20):     # Number of tweets, TODO: increase the number
            all_data.append(tweet._json)
        return all_data

    def clean_tweet(self, tweet):
        tweet = ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)', ' ', tweet).split())
        tweet = tweet.strip().lower()
        return ' '.join(word_tokenize(tweet))

    def get_sentiment_prediction(self, text):
        nba_pred = self.nba.get_sentiment_prediction(text)
        pattern_pred = self.pattern.get_sentiment_prediction(text)
        rnn_word2vec_pred = self.rnn_w2v.get_sentiment_prediction(text)
        rnn_gloVe_pred = self.rnn_gloVe.get_sentiment_prediction(text)
        sp = models.SentimentPrediction(
            naive_bayes=nba_pred,
            pattern_analyzer=pattern_pred,
            rnn_word2vec=rnn_word2vec_pred,
            rnn_gloVe=rnn_gloVe_pred
        )
        return sp

    def get_searched_tweet_instance(self, query_):
        """
        Function that creates instance of a SearchedTweet model and saves it to database

        @param query_: query on which the search was made
        @param standard_search_result: Result that we get by Twitter's standard search API

        @return: Object of a SearchedTweet model that was created and saved
        """
        standard_search_result = self.get_search_result(query_)
        st = models.SearchedTweet(query=query_)
        st.save()
        for result in standard_search_result:
            clean_text = self.clean_tweet(result['full_text'])
            sp = self.get_sentiment_prediction(clean_text)
            sp.save()
            tweet = models.Tweet(
                text = result['full_text'],
                user_location = result['user']['location'],
                created_at = result['created_at'],
                sentiment_prediction = sp
            )
            tweet.save()
            st.tweets.add(tweet)
        return st