from flask import Flask
from flask import request
from flask import render_template

import urllib
from xml.dom import minidom

app = Flask(__name__)



@app.route('/')
def topic_post():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def render_comments():
	topComment = 'test : this will be the most recent comment'
	topic = request.form['text']
	return render_template('comments.html', topComment = topComment, topic = topic)
   

# https://gdata.youtube.com/feeds/api/videos/w4mKtIjiKZU/comments
def getAllComments(videoCode):
	url = 'https://gdata.youtube.com/feeds/api/videos/' + videoCode + '/comments'
	xmldoc = minidom.parse(urllib.urlopen(url))
	contentlist = xmldoc.getElementsByTagName('content')
	return contentlist[0].firstChild.nodeValue



# @app.route("/")
# def render_comments():
# 	topComment = '1'
# 	topResponse = '2'
# 	return render_template('index.html', topComment = topComment, topResponse = topResponse)


# @app.route("/", methods=['POST'])
# def hello():
#     if request.method == 'POST':
#         populate_comments()

if __name__ == "__main__":
    app.run()