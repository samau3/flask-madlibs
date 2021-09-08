from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def questions():
    """Return render of question form with story prompt fields generated"""

    story_prompts = silly_story.prompts

    return render_template('questions.html', story_prompts = story_prompts)

@app.get('/story')
def story():
    """Return render of story page with 
        a story generated from the form inputs"""

    # previous attempt before realizing request.args was already returning a dict
    # [noun, verb, place, adjective, plural_noun] = [request.args[arg] for arg in request.args]
    # words_for_story = {arg:request.args[arg] for arg in request.args}
    # new_story = silly_story.generate(words_for_story)

    new_story = silly_story.generate(request.args)

    return render_template('story.html', story = new_story)