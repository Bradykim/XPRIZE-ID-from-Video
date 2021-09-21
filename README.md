# XPRIZE-ID-from-Video

`python 2.7`
The goal of this project is to provide a dataset for plant and animal rainforest research that is streamlined and easy-to-use. Hence, the potential users of this work include researchers interested in performing work on rainforest plant and animal data.

There is over 1 terabyte of video data taken, much of which is repetitive between frames. This enormous amount of data makes it very difficult to run identification efficiently through iNaturalist, or to train the Data+ model efficiently on a dataset that is high quality enough to lead to an accuracy greater than average. Hence, filtering repetitive or similar photos between videos will also be a substantial improvement on the previous year’s work.

We will aim to  cropping the images used as data. Cropped images will clearly show what plant needs to be identified, instead of a much larger image with several objects. This will help in improving the accuracy of species identification. For this reason, cropping images will be a substantial improvement on the previous year’s work.



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
python parseframes.py
```
