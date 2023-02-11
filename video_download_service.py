import zmq
from pytube import YouTube

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("Video Download Service running...")

while True:
    try:
        # receive string and parse into dictionary
        request = socket.recv_json()
        print(f"received request: {request}")

        # instantiate a YouTube object that corresponds to the YouTube video
        yt = YouTube(request["url"])
        yt.check_availability()
        stream = yt.streams.filter(progressive=True, file_extension='mp4')[-1]

        # download the video
        if request.get("output_path", None) is None:
            file_location = stream.download()
        else:
            file_location = stream.download(output_path = request["output_path"])
        print(f"Video downloaded to: {file_location}")

        video_data = {
            "title" : yt.title,
            "channel_id" : yt.channel_id,
            "length" : yt.length,
            "rating": yt.rating,
            "description": yt.description,
            "keywords" : yt.keywords,
            "publish_date" : str(yt.publish_date),  ## converted to string, because datetime type is not json serializable. 
            "views": yt.views,
            "thumbnail_url": yt.thumbnail_url,
            "file_location": file_location
        }
        socket.send_json(video_data)
    except Exception as e:
        err_dict = {"error": str(e)}
        print(err_dict)
        socket.send_json(err_dict)