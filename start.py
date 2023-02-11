from flask import Flask, render_template
from requests import get

app = Flask(__name__)

@app.route("/")
def home():
    response = get("http://localhost:3000/blogs")
    data = response.json()
    return render_template("index.html",blogData=data)

@app.route("/about")

def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def post(num):
    response = get("http://localhost:3000/blogs")
    data = response.json()[num-1]
    print(data)
    return render_template("post.html",blogData=data)



if __name__ == "__main__":
    app.run(debug=True)