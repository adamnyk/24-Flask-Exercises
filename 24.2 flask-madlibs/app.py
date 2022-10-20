from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story, stories

app = Flask(__name__)

app.config["SECRET_KEY"] = "app_key"
debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    """Shows hompage with empty madlibs form"""
    return render_template("home.html", stories=stories)


@app.route("/form")
def show_form():
    """Shows form for chosen Madlib story."""
    
    story_id = request.args.get("story_id")
            
    chosen_story = stories.get(int(story_id))
            
    return render_template("form.html", story = chosen_story, story_id=story_id)


@app.route("/story")
def make_story():
    """Shows completed madlib story."""
    story_id = request.args.get("story_id")
    chosen_story = stories.get(int(story_id))
    
    completed_story = chosen_story.generate(request.args)

    return render_template("story.html", story=completed_story) 
