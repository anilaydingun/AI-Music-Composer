from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def init():
    return render_template("/templates/index.html")

@app.route("/test", methods=["POST"])
def ff():
    data = request.json
    print(data["dataUsername"])

if __name__ == "__main__":
    app.run()