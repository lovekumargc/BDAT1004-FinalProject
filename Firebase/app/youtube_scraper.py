import os
import requests

from app.youtube_video_model import YoutubeVideoModel


class YoutubeClient:
    countryCode = "CA"
    youtubeApiKey = ""
    maximumResults = 50
    chart = "mostPopular"

    def __init__(self):
        pass

    def getTrendingVideos(self, pageToken="&"):
        global countryCode
        global youtubeApiKey
        global maximumResults
        global chart

        request_url = f"https://www.googleapis.com/youtube/v3/videos?part=id,statistics,snippet{pageToken}chart={self.chart}&regionCode={self.countryCode}&maxResults={self.maximumResults}&key={self.youtubeApiKey}"

        request = requests.get(request_url)
        if request.status_code == 200:
            return self.parse(request.json())

    def parse(self, json):

        print(json)

        items = json["items"]
        models = []

        for item in items:

            videoId = item["id"]
            snippet = item["snippet"]
            channelId = snippet["channelId"]
            if "tags" in snippet and len(snippet["tags"]) != 0:
                tags = snippet["tags"]
            channelTitle = snippet["channelTitle"]
            publishedAt = snippet["publishedAt"]
            localized = snippet["localized"]
            title = localized["title"]
            description = localized["description"]
            statistics = item["statistics"]

            viewCount = ""
            likeCount = ""
            dislikeCount = ""
            favoriteCount = ""
            commentCount = ""

            if "viewCount" in statistics:
                viewCount = statistics["viewCount"]

            if "likeCount" in statistics:
                likeCount = statistics["likeCount"]

            if "dislikeCount" in statistics:
                dislikeCount = statistics["dislikeCount"]

            if "favoriteCount" in statistics:
                favoriteCount = statistics["favoriteCount"]

            if "commentCount" in statistics:
                commentCount = statistics["commentCount"]

            model = YoutubeVideoModel(videoId, channelId, tags, channelTitle, publishedAt, title, description,
                                      viewCount, likeCount, dislikeCount, favoriteCount, commentCount)
            models.append(model)

        return models
