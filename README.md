# XPRIZE-ID-from-Video

`python 2.7`

This program extracts frames containing plants from video footage.

## Configuration

To set up Google Cloud Vision API please follow the guidance: https://cloud.google.com/vision/docs/setup. Save your credential json file as `credential.json` in current directory.

## Parameters

Set the following parameters in recognize.py:

1. fps  
   fps refers to how many frames to process in one second of footage. Higher fps produces more frames but may lead to multiple frames of the same plant.
2. threshold  
   threshold refers to how likely should a frame contain plants (0 - 1). Frames with likelihood lower than the threshold will be dropped. Higher threshold produces fewer but higher quality frames.

## Input and Output

1. input  
   Store all mp4 footages in the input folder.
2. output  
   The frames will be stored as jpg in the output folder.


## Command

```py
export GOOGLE_APPLICATION_CREDENTIALS=./credential.json
virtualenv -p=/usr/bin/python2.7 .
source ./bin/activate
pip install -r requirements.txt
python recognize.py
```
