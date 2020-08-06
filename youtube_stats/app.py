from flask import Flask
from flask import jsonify, request, render_template
import json

from firebase_client import FirebaseClient

app = Flask(__name__)

firebase = FirebaseClient()

database = firebase.getDatabase()

@app.route('/')
def google_pie_chart():
    data = getTopTags()
    data1 = getLikesVsDislikes()
    return render_template('pie-chart.html', data=data, data1=data1)


def getTopTags():
    dataArray = database.child("data").get()
    list = dataArray.val()
    tagsList = []

    for item in list:
        for video in item["items"]:
            if "tags" in video:
                tags = video["tags"]
                for tag in tags:
                    tagsList.append(tag)

    word_counter = {}
    for word in tagsList:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key=word_counter.get, reverse=True)

    topTen = popular_words[:10]

    data = {'Tags': 'Count'}

    for word in topTen:
        count = word_counter[word]
        data[word] = count
    return data


def getLikesVsDislikes():
    dataArray = database.child("data").get()
    list = dataArray.val()

    dict = list[0]
    items = dict["items"]
    videos = items[:40]

    likesVsDislikes = []

    data = {'Likes': 'Dislikes'}

    for video in videos:
        title = video["title"]
        dislikeCount = video["dislikeCount"]
        likeCount = video["likeCount"]

        data[int(likeCount)] = int(dislikeCount)
    return data


if __name__ == "__main__":
    app.run()
