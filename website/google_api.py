from googleapiclient.discovery import build

youtube_api = "AIzaSyDsrTcxaoyZyItuRRew6IFjvlAX2wnScYc"

def get_song_info(song_name):
    result = {}
    youtube = build('youtube', 'v3', developerKey=youtube_api)

    request = youtube.search().list(part='snippet', maxResults=1, q=f"{song_name}", type='video')

    response = request.execute()
    videoId = dict(response.items())['items'][0]['id']['videoId']
    title = dict(response.items())['items'][0]['snippet']['title']
    date = dict(response.items())['items'][0]['snippet']['publishedAt']
    description = dict(response.items())['items'][0]['snippet']['description']
    result.update({'title': title, 'date': date, 'desc': description, 'id': videoId})
    return result