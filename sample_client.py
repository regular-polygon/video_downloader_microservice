import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
print("Connected to test server...")

# Construct a request dictionary and send it to the video download service.
# If output path is None, the video will be downloaded to the same directory as the video download service.
# remember to escape \ characters in file path or use a raw string
request = {
    "url" : "https://www.youtube.com/watch?v=-MTRxRO5SRA",
    "output_path" : "C:\\Users\\WC (Student)\\Desktop"
}
socket.send_json(request)
response = socket.recv_json()  ## type(response) == dict

# debug print statements
print(f"Request: {request}")
for key, value in response.items():
    print(key, ": ", value, end="\n-----------------------\n")
print("Response JSON string: ")
print(json.dumps(response))

