from app.firebase_client import FirebaseClient
from app.youtube_scraper import YoutubeClient
from datetime import datetime

youtube = YoutubeClient()
firebase = FirebaseClient()
database = firebase.getDatabase()

videos = youtube.getTrendingVideos()
# If there are no videos put empty entry into the database for the day
if videos is None:
    now = datetime.now()
    timestamp = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'
    dataArray = database.child("data").get()
    dataList = dataArray.val()
    if dataList is None:
        dataList = []
    database.child("data").set(dataList)

else:
    jsonArray = []

    for video in videos:
        json = {
            "id": video.videoId,
            "channelId": video.channelId,
            "tags": video.tags,
            "channelTitle": video.channelTitle,
            "publishedAt": video.publishedAt,
            "title": video.title,
            "viewCount": video.viewCount,
            "likeCount": video.likeCount,
            "dislikeCount": video.dislikeCount,
            "favoriteCount": video.favoriteCount,
            "commentCount": video.commentCount
        }
        jsonArray.append(json)

    now = datetime.now()
    timestamp = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'

    json = {
        "time": timestamp,
        "items": jsonArray
    }

    dataArray = database.child("data").get()
    dataList = dataArray.val()
    if dataList is None:
        dataList = []
    dataList.append(json)

    database.child("data").set(dataList)
