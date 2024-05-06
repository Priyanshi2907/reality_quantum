import requests
from datetime import datetime, timedelta
import pandas as pd
import spacy
import re

import pathlib
import textwrap
import google.generativeai as genai

# Pass your Gemini API key here 

GOOGLE_API_KEY= 'AIzaSyAEgGg08BmZIDyxOiCVeRlibO9OTOLxTMs'

related_keywords = [
        'gurgaon real estate',
        "real estate gurgaon news",
        'gurgaon real estate prices',
]

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
genai.configure(api_key=GOOGLE_API_KEY)

    
generation_config = {
  "candidate_count": 1,
  "max_output_tokens": 256,
  "temperature": 1.0,
  "top_p": 0.7,
}

safety_settings=[
  {
    "category": "HARM_CATEGORY_DANGEROUS",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE",
  },
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
#     generation_config=generation_config,
    safety_settings=safety_settings
)


        
def sentiment(text):
    """
    Fetches Sentiment from the given text
    """
    try:

        response = model.generate_content(f"""
  
            You are a helpful assistant that can analyze the text and analyze Sentiment 
            
            Understand and Identify the Sentiment for the following text: {text}
            
            Output should contain only 'Positive' , 'Negative' or 'Neutral'.
            
            """)

        return response.text
    
    # except:
    except Exception as e:
        print(e)
        return 'No Response'

def real_estate_influencers():
    """
    Fetches Top Related Keywords, Influencers, Authors and Hashtags for the given keyword
    """
    try:

        response = model.generate_content(f"""
  
            You are a helpful assistant that will help me in finding the Top 10 Influencers with thier clickable profile links for Real Estate in Gurgaon, India.
            
            Output should contain only Influencers names  and their social handles profile links.
            ,in a format for example ["Name of Influencer 1" : "Twitter link"] , ["Name of Influencer 2" : "Twitter link"] and so on, without numbering  and without "\" in a single line
            
            """)

        return response.text
        
    except Exception as e:
        print(e)
        return 'No Response'
        
nlp = spacy.load("en_core_web_sm")

def NER(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        if ent.label_ == "ORG":
            entities.append("ORG")
        elif ent.label_ == "PERSON":
            entities.append("PERSON")
        
    if entities:
        return entities[0]
    else:
        return "ALL"



def twitter_search(keyword):
    '''
    Searches for the Tweets with certain keyword  
    '''
    url = "https://twitter154.p.rapidapi.com/search/search"
    
    today = datetime.today()
    yesterday = today - timedelta(days=28)
    yesterday = yesterday.strftime('%Y-%m-%d')
    
    querystring = {"query": keyword,
                   "section":"latest",
                   "min_retweets":"1",
                   "min_likes":"1",
                   "limit":"20",
                   "start_date": yesterday,
                   "language":"en"}
    
    headers = {
    	"X-RapidAPI-Key":  '7f38c01ec5msh6d33265667283d1p15a502jsn52ad05aac500',  # Rapid API key
    	"X-RapidAPI-Host": "twitter154.p.rapidapi.com" 
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    #print(response.json())
      
    try: 
        data_2 = [{
            "tweet_id": tweet['tweet_id'],
            "text": tweet['text'],
            "created_at": datetime.strptime(tweet['creation_date'].replace('+0000', ''), "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d'),
            "tweet_link": tweet['expanded_url'],
            "user_screen_name": tweet['user']['username'],
            "user_location": tweet['user']['location'],
            "user_followers_count": tweet['user']['follower_count'],
            "user_friends_count": tweet['user']['following_count'],
            "retweet_count": tweet['retweet_count'],
            "favorite_count": tweet['favorite_count'],
            "lang": tweet['language'],
            "username": tweet['user']['name']
            } for tweet in response.json()['results']]

    except:
        data_2 = [{
            "tweet_id": tweet['tweet_id'],
            "text": tweet['text'],
            "created_at": datetime.strptime(tweet['creation_date'].replace('+0000', ''), "%a %b %d %H:%M:%S %Y").strftime('%Y-%m-%d'),
            "tweet_link": tweet['expanded_url'],
            "user_screen_name": tweet['user']['username'],
            "user_location": tweet['user']['location'],
            "user_followers_count": tweet['user']['follower_count'],
            "user_friends_count": tweet['user']['following_count'],
            "retweet_count": tweet['retweet_count'],
            "favorite_count": tweet['favorite_count'],
            "lang": tweet['language'],
            "username": tweet['user']['username'],
            } for tweet in response.json()['results']]

    df = pd.DataFrame(data_2)

    # display(df)
    
    hashtags_count = {}
    
    try:
        
        # for some keywords if there no tweets present 
        # empty df will be returned and when you try to calculate reach it might throw error
        # to handle it added the try except block.
        
        df['reach'] = df['user_followers_count'] + df['user_friends_count'] + df['retweet_count'] + df['favorite_count']
        # Apply the lambda function to each row of the DataFrame
        df['hashtags'] = df['text'].apply(lambda x: re.findall(r'#\w+', x))

        df['sentiment'] = df['text'].apply(sentiment)

        df['entity']=df["username"].apply(NER)

        df['user_profile_link'] = 'https://twitter.com/' + df['user_screen_name']
        
        # hashtags = [hashtag for hashtag_list in df['hashtags'] for hashtag in hashtag_list]
        
        # for i in hashtags:
        #     if i in hashtags_count:
        #         hashtags_count[i] += 1
        #     else:
        #         hashtags_count[i] = 1
        # print(hashtags_count)
    
    except Exception as e:
        # print(e)
        # print('-'*49)
        pass
    print(df)
    return df #, hashtags_count


# df, hashtags_count = twitter_search(#pass the keyword here))

#     twitter_search returns dataframe df and dictionary which contains the count of hashtags

# main_df = pd.DataFrame()

# for related_keyword in related_keywords:

#     print(related_keyword)

#     df = twitter_search(related_keyword)
#     influencers=real_estate_influencers()
#     #print (df)
#     print("influencers : ",influencers)
    
#     if not df.empty:
        
#         main_df = pd.concat([main_df, df], axis=0)
        
# main_df.reset_index(drop=True, inplace=True)      

# main_df
