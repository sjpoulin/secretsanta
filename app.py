from flask import Flask, render_template, request, redirect
from helpers import shuffle_list

app = Flask(__name__)

names = []
new_names = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        names.append(name)
        return redirect("/")
    else:
        return render_template("index.html", names=names)

# TODO: Update with functionality 
@app.route("/sorted")
def sorted():
    new_names = shuffle_list(names)
    return render_template("sorted.html", names=names, new_names=new_names)


@app.route("/about")
def about():
    return render_template("about.html")

# Clear names lists and displays confirmation
@app.route("/clear")
def clear():
    names.clear()
    new_names.clear()
    return render_template("clear.html")