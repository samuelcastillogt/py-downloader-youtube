from flask import Flask, render_template, request, jsonify, send_file
import pytube
app = Flask(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/adios", methods=["GET", "POST"])
def adios():
    content = request.json
    video = pytube.YouTube(content["url"])
    imagen = video.thumbnail_url
    title = video.title
    lista = video.streams.first()
    data = {
        "imagen": imagen,
        "title": title,
    }
    print(lista)
    descarga = video.streams.first().download()
    # descarga = video.streams.first()
    # return jsonify(data) 
    return send_file(descarga)