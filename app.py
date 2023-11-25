from flask import Flask, render_template, request, redirect

app = Flask(__name__)

names = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        names.append(name)
        return redirect("/")
    else:
        return render_template("index.html", names=names)

@app.route("/about")
def about():
    return render_template("about.html")