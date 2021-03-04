from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

story_list = {"excited_story":stories.excited_story, "silly_story":stories.silly_story} 

@app.route('/')
def index():
    """Home page showing Madlibs form"""
    return render_template("base.html")

@app.route('/<story_id>')
def questions(story_id):
    """Change questions based on story selected"""
    story = story_list[story_id]
    print(story_list[story_id])
    prompts = story.prompts
    return render_template("questions.html",form_prompts = prompts)


@app.route("/results")
def result_display():
    """Page showing Madlibs story"""
    #["place", "noun", "verb", "adjective", "plural_noun"],
    answers = request.args
    text = story.generate(answers)
    return render_template("story.html", story_content = text)

