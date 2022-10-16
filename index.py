from flask import Flask, render_template, request, jsonify, send_file
from markupsafe import escape
import pytube
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/data_video", methods=["POST"])
def data_video():
    url = request.form["url"]
    video = pytube.YouTube(url)
    imagen = video.thumbnail_url
    title = video.title
    lista = video.streams.first()
    return render_template("index.html", title=title,  url=url, thumbail_url=imagen)

@app.route("/video", methods=["POST"])
def get_video():
    url = request.form["url"]
    return send_file(pytube.YouTube(url).streams.first().download(), as_attachment=True)
