from django.urls import path
from .views import *
urlpatterns = [
    path("post_tweets/",PostTweets.as_view(),name="post_tweets"),
    path("get_tweets/",RetrieveTweets.as_view(),name="get_tweets"),

    #path("influencers/",influencers.as_view(),name="influ")
]
