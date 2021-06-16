# AI-Upscaling
This uses EDSR to upscale a video by three times

Most of the working code has been taken from the following site: https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066

I have just added the functionality of handling video

The EDSR models can be found in this repo: https://github.com/Saafke/EDSR_Tensorflow/tree/master/models

To know more about video handling using OpenCV, check this: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

For using cv2.dnn_superres, and CUDA libraries, you will have to biuld OpenCV from source, for this:
 
1) If you are using Google Colab (can be extended to Linux, with minor modifications): https://towardsdatascience.com/how-to-use-opencv-with-gpu-on-colab-25594379945f
    
2) If you want to install in Windows: https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html
    
    
Enjoy, and have a Wonderful Day 😁
