from flask import Flask, request, jsonify
from chat_downloader import ChatDownloader
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



        chat = ChatDownloader().get_chat("https://www.youtube.com/watch?v=" + request.args.get('id'), message_groups=['messages', 'superchat'])
        chat_data = []
        for message in chat:
            message["author"]["images"] = message["author"]["images"][2]["url"]

            if "badges" in message["author"]:
                message["author"]["badges"] = message["author"]["badges"][0]["title"]

            chat_data.append(message)
            
        data = {
            "video": {
                "title": title,
                "publish_date": publish_date,
                "views": views,
                "channel_title": channel_title,
                "thumb": thumb,
                "duration": duration
            },
            "chat": chat_data
        }
        return jsonify(data)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
