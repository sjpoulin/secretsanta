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

# Sorts names with helper function and routes to page matching givers and recipients
## Route to error page if there are zero or one names inputted
@app.route("/sorted")
def sorted():
    new_names = shuffle_list(names)
    if len(names) < 2:
        return render_template("error.html")
    else:
        return render_template("sorted.html", names=names, new_names=new_names)


# Routes to about page
@app.route("/about")
def about():
    return render_template("about.html")

# Clear names lists and displays confirmation
@app.route("/clear")
def clear():
    names.clear()
    new_names.clear()
    return render_template("clear.html")