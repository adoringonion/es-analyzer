from flask import *

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"aaa": "fsdfsd"})


if __name__ == "__main__":
    app.run()
