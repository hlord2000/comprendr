from flask import Flask, request, render_template
from app import return_timestamps
from link_parse import link_parse
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    timestamps = return_timestamps(text)
    print(timestamps)
    return render_template('results.html', video_id=link_parse(text), speeds=timestamps)


if __name__ == '__main__':
    app.run()