from gensim.models.doc2vec import Doc2Vec
from flask import Flask, request
app = Flask(__name__)

model = Doc2Vec.load('models/doc2_1.model')


@app.route('/')
def index():
    return 'hello world'


@app.route("/post", methods=['POST'])
def post():
    hoge = request.form['hoge']

    return model.docvecs.most_similar(hoge, topn=10)[0][0]


if __name__ == '__main__':
    # http://localhost:5000/ でアクセスできるよう起動
    app.run()
