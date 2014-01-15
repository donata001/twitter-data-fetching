import tweepy
import csv
import codecs



query="apple"
input_num="100"

consumer_key='hXzoXjh6WmCYLjPfr8PmlA'
consumer_secret='tidfHCTHRUmAxD0ds39F0momqXuB7xQpERF8DENHRLY'
access_token_key='2191132039-BekGBJQTkPo5pZBefg3O4ylwquKpSgCV0apjras'
access_token_secret='r7QA13u7KXPcM2B7rsVLX6D94FzSXFC9McocZFgHViWni'

    #set up tweepy OAuth
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)
api = tweepy.API(auth)


try:
    num=int(input_num)
    temp=tweepy.Cursor(api.search,
                           q=query,
                           result_type="recent",
                           inclde_entities=True,
                           
                           lang="en").items(num)
   
    with codecs.open("result.csv",mode="w") as f:
        writer=csv.writer(f,delimiter='\t') 
        for tweet in temp:
            
            writer.writerow([tweet.created_at,tweet.text.encode('utf-8','ignore')])
            
        
except Exception,e:
    print str(e)
    
f=open("result.csv","r")
for row in f:
    print row

