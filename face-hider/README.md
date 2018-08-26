# Face Hider

Finds and blurs faces in a video. Can be used to protect identity.

## Dependencies

- Dlib: For frontal face detection
- OpenCV2: For applying blurring convolution and writing frames to video
- skvideo: For reading a video frame by frame

## Usage

##### Setup
```bash
# Install the dependencies for dlib before running this
# This may take some time due to dlib and opencv
pip install -r requirements.txt
```

##### Execution
```bash
python video_frame_processor.py "video.mkv"
# Outputs the video to out_video.mkv
```


