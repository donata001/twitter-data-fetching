iimport webapp2
import tweepy 

html="""
<!doctype html>
<html>
    <head>
        <title> Twitter data fetching web app</title>
    </head>
    <body>
        <h2>Twitter data fetching web app</h2>
        <form method="post">
            <lable for="key word">Key word:</lable>
            <input name="query", type="text", value=""><br>
           
            <lable for="count">Count:</lable>
            <input name="input_num", type="text", value=""><br>
            <input type="submit" value="submit query"><br>
        </form>
    </body>
</html>
"""

    #set up all 4 keys
consumer_key='hXzoXjh6WmCYLjPfr8PmlA'
consumer_secret='tidfHCTHRUmAxD0ds39F0momqXuB7xQpERF8DENHRLY'
access_token_key='2191132039-BekGBJQTkPo5pZBefg3O4ylwquKpSgCV0apjras'
access_token_secret='r7QA13u7KXPcM2B7rsVLX6D94FzSXFC9McocZFgHViWni'

    #set up tweepy OAuth
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api = tweepy.API(auth,monitor_rate_limit=True,wait_on_rate_limit=True)

    #set up key word and count for most current tweets


'''while True:
    input_num=raw_input("please input the count you want.Maximum 1000.")
    if not input_num.isdigit()or int(input_num)<1:
        print "not a valid number, please enter again"
        
    elif int(input_num)>1000:
        print "maximum count reached!please enter again"
        
    else:
        num=int(input_num)
        break
'''
class MainPage(webapp2.RequestHandler):
        
    def get(self):
        self.response.write(html)
            
    def post(self):
        query=self.request.get("query")
        input_num=self.request.get("input_num")
        self.response.write("Your key word is:"+query+"with count of "+input_num)
        self.response.write("Your query result is:"+"<html><br></html>")
        num=int(input_num)
        try:
            for tweet in tweepy.Cursor(api.search,
                           q=query,
                           result_type="recent",
                           inclde_entities=True,
                           lang="en").items(num):
        
                self.response.write(str(tweet.created_at)+tweet.text+"<html><br></html>")

        except Exception,e:
            self.response.write(str(e))
            
   


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
                 

