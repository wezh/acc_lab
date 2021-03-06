from flask import Flask, jsonify, request
import sys
import os, datetime
from run_celery import tweets_count
from celery.result import AsyncResult
from celery.result import ResultSet
from celery.result import GroupResult

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

results = []
result_status = []

@app.route('/process', methods=['GET'])
def dealing_tweets():
    rs = ResultSet([])
    for tw_file in filelist:
        result = tweets_count.delay(tw_file)
        # result = result.get()
        # print(result.get())
        # res = AsyncResult(result.id)
        rs.add(result)
        # result_status.append(result.status)
        # pronoun_all['Han'] += result['Han']
        # pronoun_all['Hon'] += result['Hon']
        # pronoun_all['Den'] += result['Den']
        # pronoun_all['Det'] += result['Det']
        # pronoun_all['Denna'] += result['Denna']
        # pronoun_all['Denne'] += result['Denne']
        # pronoun_all['Hen'] += result['Hen']

    for item in rs:
        i = item.get()
        results.append(i)
    return 'Processing the result'

@app.route('/result', methods=['GET'])
def get_result():
    for r in results:
        pronoun_all['Han'] += r['Han']
        pronoun_all['Hon'] += r['Hon']
        pronoun_all['Den'] += r['Den']
        pronoun_all['Det'] += r['Det']
        pronoun_all['Denna'] += r['Denna']
        pronoun_all['Denne'] += r['Denne']
        pronoun_all['Hen'] += r['Hen']
    return "Han: " + str(pronoun_all['Han']) + '\n' + 'Hon: ' +str(pronoun_all['Hon']) + '\n' + 'Den: ' + str(pronoun_all['Den']) + '\n' + 'Det: ' +str(pronoun_all['Det']) + '\n' + 'Denna: ' +str(pronoun_all['Denna']) + '\n' + 'Denne: ' +str(pronoun_all['Denne']) + '\n' + "Hen: " + str(pronoun_all['Hen'])
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
