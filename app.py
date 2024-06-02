from flask import Flask, render_template #Render template allows http interaction
import requests 
import json
app = Flask(__name__)



def get_meme(): #GET method function to recieve img
    url = "https://meme-api.com/gimme"   #API refference link
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit


@app.route("/") #Routes data to the app, aka website
def index():
    meme_pic,subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=5000)