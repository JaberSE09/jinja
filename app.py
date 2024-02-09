from flask import Flask,render_template,request
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app=Flask(__name__)
app.config['SECRET_KEY'] = "secret"

Debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    return render_template('home.html', prompts=story.prompts)
                           
@app.route('/story')
def storyRoute():
    return render_template('story.html', text=story.generate(request.args))