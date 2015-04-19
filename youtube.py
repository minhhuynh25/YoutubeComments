from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)



@app.route('/')
def topic_post():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def render_comments():
	topComment = '1'
	topResponse = '2'
	topic = request.form['text']
	return render_template('comments.html', topComment = topComment, topResponse = topResponse, topic = topic)
   


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