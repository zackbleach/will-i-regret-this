import random

from flask import render_template
from app import app
from quote import get_quote


@app.route('/')
@app.route('/index')
def index():
    decision = ['Almost Certainly',
                'Extremely unlikely',
                'Without doubt',
                "It's Doubtful",
                'Most Probably',
                'Only you can know',
                'Only time will tell',
                "It's hard to tell",
                'Who knows',
                'Je ne sais pas',
                'Yes',
                'NO #YOLO']
    decision = random.choice(decision)
    quote_and_author = get_quote().split(":::")
    quote = quote_and_author[1]
    author = quote_and_author[0]
    print quote
    return render_template("index.html",
                           decision=decision,
                           author=author,
                           quote=quote)
