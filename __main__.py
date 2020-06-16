#!/usr/bin/python3
import sys
import os
import argparsea

asjdhfkm

;hsadhfkasjdf

VIDEO_NAME = args.input
OUTPUT_NAME = args.output

try:
    import cv2 as cv
except ImportError:
    print("PLEASE install opencv, or I won't work :(")
    quit()

import numpy as np


if __name__=='__main__':
    video_input = cv.VideoCapture(VIDEO_NAME)
    width =int( video_input.get(cv.CAP_PROP_FRAME_WIDTH))
    height =int( video_input.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps =int( video_input.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter_fourcc(*"MP4V")
    frames =int( video_input.get(cv.CAP_PROP_FRAME_COUNT))

    print(f"width: {width}, height {height}, fps {fps}, fourcc {fourcc}, frames {frames}")
    video_output = cv.VideoWriter(OUTPUT_NAME, fourcc, int(fps), (width, height))

    last_frame = np.zeros((200, 200, 3))
    for i in range(frames):
        is_frame_ok, frame = video_input.read()

        # Only looks at every 4th frame
        if i % 4 != 0:
            continue

        if is_frame_ok:
            print(f"Processing frame {i+1}/{frames}")
            mini_frame = cv.resize(frame, (200, 200))

            # Only accepts image that have at least 10000 of difference
            if np.sum(mini_frame-last_frame) > 10000:
                video_output.write(frame)

            last_frame = mini_frame

        else:
            print ("Sorry, but I think your file is corrupted")
            break  # Something has gone wrong

    video_input.release()
    video_output.release()

