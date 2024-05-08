from django.urls import path
from .views import *
urlpatterns = [
    path("post_tweets/",PostTweets.as_view(),name="post_tweets"),
    #retrieve
   # path("get_tweets/",RetrieveTweets.as_view(),name="get_tweets"),
    path("tweets_by_sent/<str:sentiment>/",RetrieveTweets.as_view(),name="get_tweets_by_sentiment"),


    path("influencers/",get_influ.as_view(),name="influ")
]
