import webapp2
import tweepy,csv,codecs
import smtplib

html="""
<!doctype html>
<html>
    <head>
        <title> Twitter data fetching web app</title>
    </head>
    <body>
        <h2>Twitter data fetching web app</h2>
            <style>
            h2 {
            font: bold 330%/100% "Lucida Grande";
            position: relative;
            color: #CCCFFF;
            }
            body {
            background-image: url(../css/bg.jpg); no-repeat center center fixed;
            }
            lable {
            font:bold 110% "Lucida Grande";
            position:relative;
            color:#FFCCFF;
            }
            p {
            font:bold 150%"Lucida Grande";
            position:relative;
            color:white;
            }
            #submit {
            width: 180px;
            height: 60px;
	    background-color: grey;
	    color: #FFFFFF;
	    border-radius: 5px;
	    border: 4px solid #FA6900;
	    font-family: Verdana, Arial, Sans-Serif;
	    font-size: 1em;
	    font-weight: bold;
	    text-align: center;
	    box-shadow: 5px 5px 5px #888;
	    display: inline-block;
	    margin-right: 20px;
            }
            #intro {
            width:420px;
            height:330%;
            color:white;
            font:bold 110%; 
            font-size:1.5em;
            display:inline-block;
            position:relative;
            margin-left:40px;
            }
            </style>
        <script type="text/javascript">
            
                    function error_check(){
                    
                    var query=document.getElementsByName('query')[0].value;
                    var input_num=document.getElementsByName('input_num')[0].value   
                    var flag;
                    if (query===""||query.length>100) {
                        alert ("please put a key word with length less than 100!");
                        window.location="http://twitter-data-fetching.appspot.com/"
                        flag=false;
                    }
                    else if ((input_num==="")||isNaN(input_num)||parseInt(input_num)<1) {
                        alert("please enter a valid count number!");
                        window.location="http://twitter-data-fetching.appspot.com/"
                        flag=false;
                    }
                    else if (parseInt(input_num)>1000) {
                        alert ("please enter a smaller count number!");
                        window.location="http://twitter-data-fetching.appspot.com/"
                        flag=false;
                    }
                    else {
                    flag=true;
                    }
                
                return flag;
                }
            </script>
            
        <form method="post", onSubmit="return error_check();">
            <lable for="key word">Key word:</lable><br>
            <input name="query", type="text"><br>  
            <br>
            <lable for="count">Count:</lable><br>
            <input name="input_num", type="text"><br>                  <br>
            <input type="submit", ID="submit", value="submit query">
            <div ID="intro"><i>This app will find you the tweets you are interested in with the specific count number you entered, the result will be saved in a csv file, you can use excel to view the data.<i></div>  
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

api = tweepy.API(auth)

    #set up key word and count for most current tweets


class MainPage(webapp2.RequestHandler):
        
    def get(self):
        self.response.write(html)
            
    def post(self):
        query=self.request.get("query")
        input_num=self.request.get("input_num")        
        self.response.write("Your key word is: "+query+" with count of "+input_num)       
        self.response.write("the related tweets are as follows: "+ "\n")        

        try:
            num=int(input_num)
        
            for tweet in tweepy.Cursor(api.search,
                                       q=query,
                                       result_type="recent",
                                       inclde_entities=True,                           
                                       lang="en").items(num):        
                self.response.headers['Content-Type']='application/csv'
                writer=csv.writer(self.response.out,delimiter='\t')
                writer.writerow([tweet.created_at,tweet.text.encode('ascii','ignore')])
        except Exception,e:
            self.response.write(str(e))


   


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
                 

