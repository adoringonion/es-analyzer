from gensim.models.doc2vec import Doc2Vec
from flask import Flask, request
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET
import json
import settings

app = Flask(__name__)
CORS(app)

model = Doc2Vec.load('models/doc2_1.model')
yahoo_url = 'https://jlp.yahooapis.jp/MAService/V1/parse'
client_id = settings.ID


@app.route("/", methods=['POST'])
def post():
    sentence = request.form['sentence']
    list = []

    data = {
        'appid': client_id,
        'results': 'ma',
        'sentence': sentence
    }

    res = requests.post(yahoo_url, data=data)

    root = ET.fromstring(res.text)

    for e in root.getiterator('{urn:yahoo:jp:jlp}surface'):
        list.append(e.text)

    conseq = model.docvecs.most_similar([model.infer_vector(list)])

    dict_data = {
        'first': conseq[0][0],
        'second': conseq[1][0],
        'third': conseq[2][0],
        'fourth': conseq[3][0],
        'fifth': conseq[4][0],
        'sixth': conseq[5][0],
        'seventh': conseq[6][0],
        'eighth': conseq[7][0],
        'ninth': conseq[8][0],
        'tenth': conseq[9][0]
    }

    json_data = json.dumps(dict_data, ensure_ascii=False, indent=2)
    print(json_data)
    return json_data


if __name__ == '__main__':
    app.run()
