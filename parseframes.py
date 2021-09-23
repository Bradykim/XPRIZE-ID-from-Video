import io
import os
import cv2
import glob
import requests

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# fps of video to frames
fps = 0.5

# Threshold of frame score
threshold = 0.9

# Read all videos
path = 'input'
vidnum = 0
for video in glob.glob(os.path.join(path, '*.[mM][pP]4')):
    # Path to video file
    vidObj = cv2.VideoCapture(video)

    # Used as counter variable
    count = 0

    # Checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        if not success:
            break

        if count * fps % 60 == 0:
            # Saves the frames with num
            num = count * fps / 60
            cv2.imwrite("output/video" + str(vidnum) +
                        "frame%d.jpg" % num, image)

        count += 1

    vidnum += 1

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Read all frames
path = 'output'
for frame in glob.glob(os.path.join(path, '*.jpg')):
    # The name of the image file to annotate
    file_name = os.path.abspath(frame)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
  
#Step 1
    # Remove unqualified frames
    score = 0
    for label in labels:
            score = label.score
    print("Score for " + frame + ": " + str(score))
    if score < threshold:
        os.remove(frame)

   
#Step 2
    #Checks similarity of two images to each other
    r = requests.post(
    "https://api.deepai.org/api/image-similarity",
    files={
        'image1': open('/path/to/your/file.jpg', 'rb'),
        'image2': open('/path/to/your/file.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json())
    
        

