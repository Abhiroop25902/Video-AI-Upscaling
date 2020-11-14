import cv2 as cv
from cv2 import dnn_superres
import numpy as np

cap = cv.VideoCapture("network.mp4")

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')
out = cv.VideoWriter('output.mp4',fourcc, 20.0, (1500,840))

# Create an SR object
sr = dnn_superres.DnnSuperResImpl_create()

# Read the desired model
path = "EDSR_x3.pb"
sr.readModel(path)

# Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 3)

sr.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
sr.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)

frame = 0

while True:
    # Read image
    ret,image = cap.read()

    if not ret:
        break

    # Upscale the image
    result = sr.upsample(image)
    frame = frame + 1

    print(f"{frame}/121 done")

    out.write(result)


cap.release()
out.release()