from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from searched_tweets.models import SearchedTweet, Tweet
from .serializers import SearchedTweetSerializer, TweetSerializer
from rest_framework.response import Response
from searched_tweets.utils.twitter_analysis_utils import TwitterAnalysisUtil

class ListSearchedTweets(viewsets.ModelViewSet):
    queryset = SearchedTweet.objects.all()
    serializer_class = SearchedTweetSerializer

class DestroySearchedTweets(generics.DestroyAPIView):
    queryset = SearchedTweet.objects.all()
    serializer_class = SearchedTweetSerializer


twitter_util = TwitterAnalysisUtil()
class CreateSearchedTweets(APIView):

    def post(self,request):
        serializer = SearchedTweetSerializer(data=request.data)
        if serializer.is_valid():
            query = serializer.data['query']
            searched_tweet = twitter_util.get_searched_tweet_instance(query)
            search_tweet_serializer = SearchedTweetSerializer(searched_tweet)
            return Response(search_tweet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



