from django.db import models

class tweet(models.Model):
    tweet_id=models.CharField(max_length=100)
    text=models.TextField(max_length=100)
    created_at=models.CharField(max_length=100)
    tweet_link=models.URLField(blank=True, null=True)
    user_screen_name=models.CharField(max_length=100,blank=True, null=True)
    user_location=models.CharField(max_length=100 ,blank=True, null=True)
    user_followers_count=models.IntegerField(default=0)
    user_friends_count=models.IntegerField(blank=True, null=True)
    retweet_count=models.IntegerField(blank=True, null=True)
    favorite_count=models.IntegerField(blank=True, null=True)
    lang=models.CharField(max_length=40,blank=True, null=True)
    reach=models.IntegerField(blank=True, null=True)  #Reach is no. of people seen your tweet
    hashtags=models.CharField(max_length=500 ,blank=True, null=True)   #Comma separated list of Hashtags in the Tweet
    sentiment=models.CharField(max_length=500 ,blank=True, null=True)
    name=models.CharField(max_length=500 ,blank=True, null=True)
    entity=models.CharField(max_length=500 ,blank=True, null=True)
    user_profile_link=models.URLField(blank=True, null=True)


    def __str__(self):
        return f"{self.tweet_id} - {self.text[:50]}"  # Return a truncated version of the tweet text

    def to_json(self):
        return {
            "tweet_id": self.tweet_id,
            "text": self.text,
            "created_at": self.created_at,  # Serialize datetime to ISO 8601 format
            "tweet_link": self.tweet_link,
            "user_screen_name": self.user_screen_name,
            "user_location": self.user_location,
            "user_followers_count": self.user_followers_count,
            "user_friends_count": self.user_friends_count,
            "retweet_count": self.retweet_count,
            "favorite_count": self.favorite_count,
            "lang": self.lang,
            "reach": self.reach,
            "hashtags": self.hashtags,
            "sentiment":self.sentiment,
            "name":self.name,
            "entity":self.entity,
            "user_profile_link":self.user_profile_link


            
        }
    
class influencers(models.Model):
    name=models.CharField(max_length=100)
    profile=models.URLField(blank=True, null=True)

    def to_json(self):
        return {
            "name": self.name,
            "profile": self.profile,
        }

    
    
# Create your models here.



