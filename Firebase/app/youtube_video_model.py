class YoutubeVideoModel:

    def __init__(self, videoId, channelId, tags, channelTitle, publishedAt, title, description,
                 viewCount, likeCount, dislikeCount, favoriteCount, commentCount):
        self.videoId = videoId
        self.channelId = channelId
        self.tags = tags
        self.channelTitle = channelTitle
        self.publishedAt = publishedAt
        self.title = title
        self.description = description
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.favoriteCount = favoriteCount
        self.commentCount = commentCount
