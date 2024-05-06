from django.urls import path
from .views import *
urlpatterns = [
    path("real_tweets/",SearchTweets.as_view(),name="real_tweets"),
    #path("influencers/",influencers.as_view(),name="influ")
]
