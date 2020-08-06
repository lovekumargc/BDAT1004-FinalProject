import flask
from firebase_client import FirebaseClient

app = flask.Flask(__name__)
firebaseClient = FirebaseClient()
database = firebaseClient.getDatabase()
dataArray = database.child("data").get()
datalist = dataArray.val()


@app.route('/', methods=['GET'])
def homepage():
    return "please provide the complete url path"


# get all  youtube vedio stats data stored in data base

@app.route('/youtubedata', methods=['GET'])
def home():
    if len(datalist) == 0:
        return flask.jsonify(datalist)
    else:
        return flask.jsonify(datalist)


# get range of  all youtube vedio titles matching  to the channelTitle specified in URL

@app.route('/youtubedata/<string:name>', methods=['GET'])
def get_one(name):
    titleList = []
    for item in datalist:
        for video in item["items"]:
            if name in video["channelTitle"]:
                tags = video["title"]
                titleList.append(tags)
    return flask.jsonify(titleList)


# get youtube vedio stats data according to the ID specified in URL

@app.route('/youtubedata/id=<int:x>', methods=['GET'])
def get_id(x):
    IdList = []
    for item in datalist:
        for video in item["items"]:
            IdList.append(video)
        return flask.jsonify(IdList[x])
    else:
        return []
