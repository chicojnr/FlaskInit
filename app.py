from flask import Flask, request, jsonify
from pytube import YouTube
import json

app = Flask(__name__)


@app.route('/')
def index():
    try:
        video = YouTube('https://www.youtube.com/watch?v=' + request.args.get('id'))
        title = video.title
        thumb = video.thumbnail_url
        publish_date = video.publish_date
        views = video.views
        channel_title = video.author
        duration = video.length

        data = {
            "video": {
                "title": title,
                "publish_date": publish_date,
                "views": views,
                "channel_title": channel_title,
                "thumb": thumb,
                "duration": duration
            }
        }
        return jsonify(data)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
