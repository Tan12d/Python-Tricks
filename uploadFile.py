from flask import Flask, request, jsonify
from os import path

app = Flask("playground")

@app.post("/upload-file")
def upload_file():
    img = request.files["image"]

    img.save(path.abspath("0.png"))

    return jsonify({
        "success":True
    })

app.run()