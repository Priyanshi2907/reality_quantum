from rest_framework import serializers
from . models import tweet,influencers

class TweetSerializers(serializers.ModelSerializer):
    class Meta:
        model=tweet
        fields='__all__'

class InfluSerializers(serializers.ModelSerializer):
    class Meta:
        model=influencers
        fields='__all__'
        
class RetrieveTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = tweet
        fields = '__all__'