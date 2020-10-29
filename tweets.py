import json
import os


def isLineEmpty(line):
    return len(line.strip()) == 0

pronounDict = {'Han': 0,
                'Hon': 0,
                'Den': 0,
                'Det': 0,
                'Denna': 0,
                'Denne': 0,
                'Hen': 0}
tweets = []
with open('../../Downloads/data' + os.sep + 'fcba121d-352f-494b-86aa-a45ff1f283a3', 'r+', encoding='utf-8-sig') as datafile:
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
    print(pronounDict_json)
    pronounDict_dict = json.loads(pronounDict_json)
    print(pronounDict_dict)



