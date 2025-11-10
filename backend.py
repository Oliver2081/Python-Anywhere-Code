import os
import json
import git
from flask import render_template, Flask, abort, requests

app = Flask(__name__)

@app.route('/update_server', methods=['POST'])
    def webhook():
        if request.method == 'POST':
            repo = git.Repo('https://github.com/Oliver2081/Geography-Website.git')
            origin = repo.remotes.origin
origin.pull()
return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<pageId>")
def renderPage(pageId):
    validPages = []
    availablePages = os.listdir("./data")
    
    for page in availablePages:
        if page[-5:] == ".json":
            validPages.append(page[:-5])

    if pageId in validPages:
        with open(f"./data/{pageId}.json", "r") as f:
            pageData = json.load(f)

            TITLE = pageData.get("title")
            SPECREF = pageData.get("specRef")
            SECTIONS = []
            
            for section in pageData.get("sections"):
                SECTIONS.append(section)

        return render_template("page.html", title=TITLE, specRef=SPECREF, sections=SECTIONS)
    
    else:
        return render_template("404.html"), 404

@app.errorhandler(404)
def pageNotfound(error):
    return render_template('404.html'), 404


