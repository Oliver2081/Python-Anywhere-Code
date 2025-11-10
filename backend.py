import os
import json
import git
from flask import render_template, Flask, abort, request

app = Flask(__name__)
DATAPATH = '/home/o2081/website/data'

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('website')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    return "OK", 200
    
@app.route("/<pageId>")
def renderPage(pageId):
    validPages = []
    availablePages = os.listdir(DATAPATH)
    
    for page in availablePages:
        if page[-5:] == ".json":
            validPages.append(page[:-5])

    if pageId in validPages:
        with open(f"{DATAPATH}/{pageId}.json", "r") as f:
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











