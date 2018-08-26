import sys

import cv2
from tqdm import tqdm

from face_detect import detect_face
from face_processor import pixelate
from skvideo import io


def frame_face_blur(image, kernel_size=20):
    for face in detect_face(image):
        image[face.top() - 10:face.bottom() + 10, face.left() - 10:face.right() + 10] = pixelate(
            image[face.top() - 10:face.bottom() + 10, face.left() - 10:face.right() + 10], kernel_size=kernel_size)
    return image


def extract_frames_from_vid(vid_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    data = io.ffprobe(vid_path)['video']
    rate = int(data['@r_frame_rate'].split('/')[0])
    out = None
    for frame in tqdm(io.vreader(vid_path),unit=' frame'):
        if out is None:
            out = cv2.VideoWriter('out_' + vid_path, fourcc, rate, frame.shape[1:3][::-1])
        frame = frame_face_blur(frame)
        out.write(frame)
    out.release()


extract_frames_from_vid(sys.argv[1])
