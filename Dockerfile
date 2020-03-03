from python:3.8.1

RUN mkdir src
COPY models models/
COPY src src/

RUN apt-get update
# && apt-get install -y mecab \
# && apt-get install -y mecab-ipadic \
# && apt-get install -y libmecab-dev \
# && apt-get install -y mecab-ipadic-utf8 \
# && apt-get install -y swig

RUN pip install -r ./src/requirements.txt

EXPOSE 5000

CMD python src/app.py
