
## YouTube Video Downloader Microservice
The server will communicate with the client via ZeroMQ. The client's request should provide a YouTube video link and an optional local directory. If a directory is provided by the user, the service will download the video into that directory, otherwise the video will be downloaded into the same directory as video_downloader_service.py. Once the download is complete, the server will send a JSON file back to the client containing the video's information: title, description, length etc. 

## How to Request Data From Server:

```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

request = {
        "url" : url,
        "output_path" : None ## this can be None or a path to a local directory
        }
socket.send_json(request)
```

## How to Receive Data

```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# After sending a request
# response is a dictionary object
response = socket.recv_json()

# print key, value pairs in readable format
for key, value in response.items():
    print(key, ": ", value, end="\n-----------------------\n")

# print JSON string
print("Response JSON string: ")
print(json.dumps(response))

```


