from flask import Flask

app = Flask(__name__)

@app.route("/")
def downloads_organiser():
    return "<p>Downloads Folder Has Been Organised</p>"