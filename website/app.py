from flask import Flask, request, render_template, send_file
from pytube import YouTube
from google_api import get_song_info

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    song_name = request.form["song_name"]
    # Search for the song on the internet and get the details
    song_details = get_song_details(song_name)
    return render_template("search.html", song_details=song_details)

def get_song_details(song_name):
    res = get_song_info(song_name=song_name)
    return res

@app.route("/download", methods=["POST"])
def download_video():
    video_id = request.form.get('video_id')
    yt_obj = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        file_path = yt_obj.download()
    except:
        return "Something went wrong!!!"
    return send_file(file_path, as_attachment=True, download_name=yt_obj.default_filename)
    # return "<cc style='font-weight: bold; font-family: -apple-system;font-weight: bold; font-size: 40px;'>Video Downloaded Successfully!</cc>"


if __name__ == "__main__":
    app.run(debug=False)
