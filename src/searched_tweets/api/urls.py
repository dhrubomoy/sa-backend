from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('searched_tweets/', views.ListSearchedTweets.as_view({'get': 'list'})),
    path('searched_tweets/<pk>/delete/', views.DestroySearchedTweets.as_view()),
    path('searched_tweets/create/', views.CreateSearchedTweets.as_view())
]
