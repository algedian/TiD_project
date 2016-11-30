import os
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=True)
parser.add_argument('--framefolder', required=True)
args = vars(parser.parse_args())

filename = args['filename']
framefolder = args["framefolder"]

framefolderpath = "./" + framefolder + "/frames"
if not os.path.exists(framefolderpath):
    os.makedirs(framefolderpath)

vidcap = cv2.VideoCapture("./"+framefolder+"/"+filename + '.mp4')
success,image = vidcap.read()
# image is an array of array of [R,G,B] values

count = 0;
while success:
  success,image = vidcap.read()
  if count%12 == 0 or count%25 == 0:
      cv2.imwrite("./"+framefolder+"/frames/frame%d.jpg" % count,image)     
      # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1

# fps=30?
