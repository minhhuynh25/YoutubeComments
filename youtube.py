from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
	topComment = 'this is the top comment'
	topResponse = 'this is the top response'
    render_template("index.html", topComment, topResponse)
    # return 'this doesnt work'

# @app.route("/", methods=['POST'])
# def hello():
#     if request.method == 'POST':
#         populate_comments()

if __name__ == "__main__":
    app.run()