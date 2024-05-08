from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework import status
from .models import tweet,influencers
from .serializers import TweetSerializers,InfluSerializers,RetrieveTweetSerializer
from .scraper import *  # Import your scraping function
from .influencer_scraper import *


class  PostTweets(APIView):
    def get(self,request):
        related_keywords = [
                'gurgaon real estate',
                "real estate gurgaon news",
                'gurgaon real estate prices',
        ]
        saved_tweets = []
        for related_keyword in related_keywords:
            print("rlkey: ",related_keyword)
            # Scrape tweets using the keyword
            scraped_tweets = twitter_search(related_keyword)
            print(type(scraped_tweets))
            if scraped_tweets is None:
                return Response("Failed to scrape tweets", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            # Save the scraped tweets to the database
           
            for i, tweet_data in scraped_tweets.iterrows():
    
                # Extract the count value from the pandas Series object
                #print("i",i)
                print("tweet data : ",tweet_data)
                
                print(" i m here")
                tweet_obj = tweet(
                    tweet_id=tweet_data['tweet_id'],
                    text=tweet_data['text'],
                    created_at=tweet_data['created_at'],
                    tweet_link=tweet_data['tweet_link'],
                    user_screen_name=tweet_data['user_screen_name'],
                    user_location=tweet_data['user_location'],
                    user_followers_count = tweet_data['user_followers_count'],
                    user_friends_count = tweet_data['user_friends_count'],
                    retweet_count = tweet_data['retweet_count'],
                    favorite_count = tweet_data['favorite_count'],
                    lang=tweet_data['lang'],
                    reach = tweet_data['reach'],
                    hashtags=tweet_data['hashtags'],
                    sentiment=tweet_data['sentiment'],
                    name=tweet_data['username'],
                    entity=tweet_data['entity'],
                    user_profile_link=tweet_data['user_profile_link']
    
                    
                )
                print("not here")
                tweet_obj.save()
                print("again here")
                saved_tweets.append(tweet_obj)        
        
        # Serialize the saved tweets
        serializer = TweetSerializers(saved_tweets, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
class RetrieveTweets(APIView):
    
    # def get(self,request):
    #    tweet_obj= tweet.objects.all()
    #    tweet_serializer=RetrieveTweetSerializer(tweet_obj,many=True)
    #    return Response(tweet_serializer.data)
    def get(self,request,sentiment):
        tweet_obj_sent=tweet.objects.filter(sentiment=sentiment)

        serializer=RetrieveTweetSerializer(tweet_obj_sent,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)



class get_influ(APIView):
    def get(self,request):
        influencers=real_estate_influencers()
        if influencers is None:
            return Response("failed to scrap influencers",status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        data={'influencers': influencers}
        return Response(data)
# class influencers(APIView):
#      def get(self,request):
#         influ_str=real_estate_influencers()
        
#         influ_list=influ_str.split(",")
#         print(type(influ_list))
#         for i in range(len(influ_list)):

#             print(type(influ_list[i]))
#             print((influ_list[i]))

#             #print(influ_list[i].replace("[",""))

#         if influ_str is None :
#                 return Response("Failed to scrape Data", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         data={"Influencers":influ_str}        
#         return Response(data)
     
