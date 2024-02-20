from flask import Flask, render_template
import requests


response = requests.get("https://api.npoint.io/d0e2841e92b1e2d1249d")

dictionary_response = response.json()
print(dictionary_response)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=dictionary_response)


@app.route("/post/<int:number>")
def show_post(number):
    return render_template("post.html", posts=dictionary_response, number=number)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
