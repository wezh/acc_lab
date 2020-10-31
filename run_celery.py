from celery import Celery
import json
import os

def isLineEmpty(line):
    return len(line.strip()) == 0

def count_tweets(tweet_datafile):

    pronounDict = {'Han': 0,
                    'Hon': 0,
                    'Den': 0,
                    'Det': 0,
                    'Denna': 0,
                    'Denne': 0,
                    'Hen': 0}
    
    tweets = []

    with open("../data" + os.sep + tweet_datafile, 'r+', encoding='utf-8-sig') as datafile:
        for line in datafile.readlines():
            if not isLineEmpty(line):
                data = json.dumps(line)
                js = json.loads(data)
                tweets.append(js)

    for j in tweets:
        jj = json.loads(j)
        if jj['text'].lower().find('han') != -1:
            pronounDict['Han'] += 1
        elif jj['text'].lower().find('hon') != -1:
            pronounDict['Hon'] += 1
        elif jj['text'].lower().find('den') != -1:
            pronounDict['Den'] += 1
        elif jj['text'].lower().find('det') != -1:
            pronounDict['Det'] += 1
        elif jj['text'].lower().find('denna') != -1:
            pronounDict['Denna'] += 1
        elif jj['text'].lower().find('denne') != -1:
            pronounDict['Denne'] += 1
        elif jj['text'].lower().find('hen') != -1:
            pronounDict['Hen'] += 1

    pronounDict_json = json.dumps(pronounDict)
    pronounDict_dict = json.loads(pronounDict_json)

    return pronounDict_dict

celery = Celery('acc_lab3', backend='rpc://', broker='pyamqp://')

celery.conf.update(
    result_expires=3600,
)

@celery.task
def tweets_count(tweetfile):
    tweet_file_local = tweetfile
    single_file_result = count_tweets(tweet_file_local)
    return single_file_result
