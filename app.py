from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    fileData = 0
    with open('database.json', 'r') as f:
        fileData = json.load(f)
        f.close()
    return render_template("index.html", fileData = fileData)

@app.route("/about", methods=["POST", "GET"])
def about():
    return render_template("about.html")

@app.route("/blog", methods=["POST", "GET"])
def blog():
    return render_template("blog.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    return render_template("contact.html")

@app.route("/detail", methods=["POST", "GET"])
def detail():
    return render_template("detail.html")

@app.route("/feature", methods=["POST", "GET"])
def feature():
    return render_template("feature.html")

@app.route("/price", methods=["POST", "GET"])
def price():
    return render_template("price.html")

@app.route("/quote", methods=["POST", "GET"])
def quote():
    return render_template("quote.html")

@app.route("/service", methods=["POST", "GET"])
def service():
    return render_template("service.html")

@app.route("/team", methods=["POST", "GET"])
def team():
    return render_template("team.html")

@app.route("/testimoni", methods=["POST", "GET"])
def testimoni():
    return render_template("testimonial.html")

if __name__ == "__main__":
  app.run()