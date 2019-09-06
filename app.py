import flask
import os
import random 
import requests
import json
import requests_oauthlib

app = flask.Flask(__name__)
#function
@app.route('/')
def index():
    r = random.randint(0,9)
    url = \
        "https://api.genius.com/search?q=Young%20Thug"
    my_headers = {
        "Authorization": "Bearer -toMMprL_By7zXAuDZ-eyrXP1QduUCTJ917TIb2DHnJOgjrinheRfjQYIJvnDn6w"
    }
    
    response = requests.get(url, headers=my_headers)
    json_body = response.json()
    primary_artist = json_body["response"]["hits"][r]["result"]["primary_artist"]["name"]
    song_title = json_body["response"]["hits"][r]["result"]["full_title"]
    song_image = json_body["response"]["hits"][r]["result"]["header_image_thumbnail_url"]
    primary_artist_image = json_body["response"]["hits"][r]["result"]["primary_artist"]["header_image_url"]
    artist_link = json_body["response"]["hits"][r]["result"]["primary_artist"]["url"]
    
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%3A youngthug"    
    
    oauth = requests_oauthlib.OAuth1(
        "U1RNMerEP5b6BDmRQLDliMxQl",
        "vlBM2z3oyPr9sBEoJQbMkrnKwHIoEFKMo0Qyd9mpZTXpwHjRpr",
        "471512920-67SZ6JLUx36ZlBUPnh2YzsZN3BcTAZ4cCzXj7TKE",
        "fvMw3m9XCxSADw8jIqNtvJnWHVF75f6r2zsQEO8QkctBU"
    )
    
    twitter_response = requests.get(url, auth=oauth)
    twitter_response_body = twitter_response.json()
    twitter_text = twitter_response_body["statuses"][r]["text"]
    
    # print(twitter_response.json())
        
    return flask.render_template("index.html", random_num = r, artist = primary_artist, image = song_image, title = song_title, artist_image = primary_artist_image, twitter_json = twitter_response_body, link = artist_link, tweet = twitter_text)
    


app.run(
    port = int(os.getenv("PORT", 8080)),
    host = os.getenv('IP', '0.0.0.0'),
    debug = True
    )
    

# print(json.dumps(json_body, indent=2))
#