from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    resp = requests.get(
        url='http://127.0.0.1:9080/crawl.json?start_requests=true&spider_name=articles'
    ).json()

    items = resp.get('items')
    return render_template('index.html', articles=items)


@app.route('/show')
def show_template():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
