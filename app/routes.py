from flask import Flask
from flask import render_template  # from flask module import Flask class

# Instantiate the Flask class into the app variable [object]
app = Flask(__name__)

# @app.get("/") # decorator that allows us to map routes to "view functions"
# def index(): # Flask calls these "view functions"
#     return "<h1>Hello World</h1>" # return statement


@app.route("/")
def index():
    return render_template('index.html')


@app.get("/about")
def about():
    me = {
        "first_name": "Sebastian",
        "last_name": "Lopez-Wells",
        "hobbies": "Baseball, literature, Programming",
        "bio": "My name is Sebastian Lopez Wells and I am a student in ITT and SDGKU's online courses."
    }
    return render_template('about.html', about_dict=me)


@app.get("/objects")
def objects():
    return render_template('objects.html')


@app.get("/classes")
def classes():
    return render_template('classes.html')
