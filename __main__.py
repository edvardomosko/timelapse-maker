#!/usr/bin/python3
import sys
import os
import argparse

MY_PATH = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--output", default="output.mp4")
parser.add_argument("input")

args = parser.parse_args()

VIDEO_NAME = args.input
OUTPUT_NAME = args.output

try:
    import cv2 as cv
except ImportError:
    print("PLEASE install opencv, or I won't work :(")
    quit()


if __name__=='__main__':
    video_input = cv.VideoCapture(VIDEO_NAME)
    width =int( video_input.get(cv.CAP_PROP_FRAME_WIDTH))
    height =int( video_input.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps =int( video_input.get(cv.CAP_PROP_FPS))
    fourcc = cv.VideoWriter_fourcc(*"MP4V")
    frames =int( video_input.get(cv.CAP_PROP_FRAME_COUNT))

    print(f"width: {width}, height {height}, fps {fps}, fourcc {fourcc}, frames {frames}")
    video_output = cv.VideoWriter(OUTPUT_NAME, fourcc, int(fps), (width, height))

    last_frame = None
    for i in range(frames):
        is_frame_ok, frame = video_input.read()

        # For starters, I only wanna save a frame if it's different from the last
        # and also only one in every 4 frames or so
        if is_frame_ok and (i%4)==0:
            print(f"Processing frame {i+1}/{frames}")

            mini_frame = cv.resize(frame, (200, 200))

            if (mini_frame != last_frame).any():
                video_output.write(frame)

            last_frame = mini_frame

        else:
            pass
            #print ("Sorry, but I think your file is corrupted")
            #break  # Something has gone wrong

    video_input.release()
    video_output.release()

