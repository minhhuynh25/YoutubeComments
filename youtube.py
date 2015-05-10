from flask import Flask
from flask import request
from flask import render_template

import urllib
from xml.dom import minidom

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# from search import get_youtube_id

app = Flask(__name__)



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

# DEVELOPER_KEY = ''
DEVELOPER_KEY = "AIzaSyBgCRUmElr3G9YqKwUIKaea51gIcg56WGs"

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  # channels = []
  # playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append(search_result["id"]["videoId"])

  return videos[0]

  # for search_result in search_response.get("items", []):
  #   if search_result["id"]["kind"] == "youtube#video":
  #     videos.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                search_result["id"]["videoId"]))
  #   elif search_result["id"]["kind"] == "youtube#channel":
  #     channels.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                  search_result["id"]["channelId"]))
  #   elif search_result["id"]["kind"] == "youtube#playlist":
  #     playlists.append("%s (%s)" % (search_result["snippet"]["title"],
  #                                   search_result["id"]["playlistId"]))

  # print "Videos:\n", "\n".join(videos), "\n"
  # print "Channels:\n", "\n".join(channels), "\n"
  # print "Playlists:\n", "\n".join(playlists), "\n"


def get_youtube_id(query):
	if __name__ == "__main__":
	  argparser.add_argument("--q", help="Search term", default=query)
	  argparser.add_argument("--max-results", help="Max results", default=25)
	  args = argparser.parse_args()

	  try:
	    return youtube_search(args)
	  except HttpError, e:
	    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


# print get_youtube_id('coldplay')




@app.route('/')
def topic_post():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def render_comments():
	
	topic = request.form['text']
	video_id = get_youtube_id(topic)
	topComment = getFirstComment(video_id)
	# topComment = 'top comment here'

	return render_template('comments.html', topComment = topComment, topic = topic)
   

# https://gdata.youtube.com/feeds/api/videos/w4mKtIjiKZU/comments
def getFirstComment(videoCode):
	url = 'https://gdata.youtube.com/feeds/api/videos/' + str(videoCode) + '/comments'
	xmldoc = minidom.parse(urllib.urlopen(url))
	contentlist = xmldoc.getElementsByTagName('content')
	bestComment = contentlist[0].firstChild.nodeValue
	if bestComment:
		return bestComment
	else:
		return 'Comments are disabled for this video'


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