import os
import json
from flask import render_template, Flask, abort

app = Flask(__name__)


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

app.run("0.0.0.0", 5000, debug=True)