from flask import Flask, jsonify, request
import sys
import os, datetime
from run_celery import tweets_count

app = Flask(__name__)

filelist = []
for root, dirs, files in os.walk('../data'):
    for f in files:
        filelist.append(f)

pronoun_all = {'Han': 0,
                'Hon': 0,
                'Den': 0,
                'Det': 0,
                'Denna': 0,
                'Denne': 0,
                'Hen': 0}

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/process', methods=['GET'])
def dealing_tweets():
    for tw_file in filelist:
        result = tweets_count.delay(tw_file)
        print(result)
    return "Done"
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
