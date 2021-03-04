from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """Home page showing Madlibs form"""
    story = silly_story
    prompts = story.prompts
    return render_template("questions.html",form_prompts = prompts)