from flask import Flask, render_template
import random

app = Flask(__name__)

# list of container images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/14/enhanced-buzz-8423-1381861722-1.jpg?downsize=715:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/15/enhanced-buzz-24732-1381864258-19.jpg?downsize=715:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/13/enhanced-buzz-24812-1381858809-8.jpg?downsize=715:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/15/enhanced-buzz-24745-1381864635-20.jpg?downsize=715:*&output-format=auto&output-quality=auto",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/15/enhanced-buzz-orig-17356-1381866444-13.jpg?downsize=715:*&output-format=auto&output-quality=auto"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
