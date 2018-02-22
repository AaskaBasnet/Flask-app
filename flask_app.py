from flask import Flask
from flask import render_template
# A very simple Flask Hello World app for you to get started with...

app = Flask(__name__)

#@app.route('/science')
#def hello_world():
 #   return 'Hello from Flask!'

@app.route('/', methods=["GET"])
def index():
    return render_template("main_page.html")