import json
import requests
from flask import Flask
from flask import request
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route('/spellcheck', methods=['GET', 'POST'])
def check():
    text = request.data
    text = str(text)
    url = 'https://www.ask.com/web?q='
    rq = requests.get(url + text)
    soup = BeautifulSoup(rq.text, 'lxml')
    words = []
    for el in soup.select('a.PartialSpellCheck-link'):
        words.append(el.text)

    return json.dumps(words)


if __name__ == '__main__':
    app.run(debug=True)
