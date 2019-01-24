from rest_framework import serializers
from sentiment_analysis import models

class SentimentPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SentimentPrediction
        fields = ('naive_bayes', 'pattern_analyzer', 'rnn_word2vec', 'rnn_gloVe')
        
class TweetSerializer(serializers.ModelSerializer):
    sentiment_prediction = SentimentPredictionSerializer()
    class Meta:
        model = models.Tweet
        fields = ('id', 'text', 'user_location', 'created_at', 'source', 'sentiment_prediction')


class SearchedTweetSerializer(serializers.ModelSerializer):
    tweets = TweetSerializer(many=True, read_only=True)
    class Meta:
        model = models.SearchedTweet
        fields = ('id', 'query', 'tweets')


        