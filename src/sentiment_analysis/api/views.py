from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from sentiment_analysis.models import SearchedTweet, Tweet
# from .serializers import SearchedTweetSerializer, TweetSerializer, SentimentPredictionSerializer
from . import serializers
from rest_framework.response import Response
from sentiment_analysis.utils.twitter_analysis_utils import TwitterAnalysisUtil

class ListSearchedTweets(viewsets.ModelViewSet):
    queryset = SearchedTweet.objects.all()
    serializer_class = serializers.SearchedTweetSerializer

class DestroySearchedTweets(generics.DestroyAPIView):
    queryset = SearchedTweet.objects.all()
    serializer_class = serializers.SearchedTweetSerializer


twitter_util = TwitterAnalysisUtil()

class CreateSearchedTweets(APIView):

    def post(self,request):
        serializer = serializers.SearchedTweetSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.data['query']
            searched_tweet = twitter_util.get_searched_tweet_instance(query)
            search_tweet_serializer = serializers.SearchedTweetSerializer(searched_tweet)
            return Response(search_tweet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PredictSentiment(APIView):

    def post(self,request):
        text = request.data['text']
        predictions = twitter_util.get_sentiment_prediction(text)
        predictions_serializer = serializers.SentimentPredictionSerializer(predictions)
        return Response(predictions_serializer.data, status=status.HTTP_201_CREATED)
        # return Response("Key 'text' does not exist", status=status.HTTP_400_BAD_REQUEST)



        



