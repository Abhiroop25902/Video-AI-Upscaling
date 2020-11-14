import cv2 as cv
from cv2 import dnn_superres
import numpy as np

cap = cv.VideoCapture("network.mp4")

#these parameters depends on video and should be changed
output_video_width = 3*500
output_video_height = 3*280
video_total_frame = 121

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4',fourcc, 20.0,(output_video_width,output_video_height))

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read the desired model
path = "EDSR_x3.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)

#setting dnn to use CUDA
sr.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
sr.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

#just for verbose in terminal
frame = 0


while True:
    # Read image
    ret,image = cap.read()

    if not ret:
        break

    # Upscale the image
    result = sr.upsample(image)
    frame = frame + 1

    #verbose in terminal
    print(f"{frame}/{video_total_frame} done")

    out.write(result)

#release capture anf
cap.release()
out.release()
