# AI-UpScaling
This uses EDSR to upscale a video by three times

Most of the working code has been taken from the following site: https://towardsdatascience.com/deep-learning-based-super-resolution-with-opencv-4fd736678066

I have just added the functionality of handling video

I have also implemented this all in Google Colab where you have to just provide your video of choice

If you want to setup this in local you need the following things:
-   The EDSR models: https://github.com/Saafke/EDSR_Tensorflow/tree/master/models
-   OpenCV CUDA Support
    -   If you want to install in Linux: https://gist.github.com/raulqf/f42c718a658cddc16f9df07ecc627be7
    -   If you want to install in Windows: https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html

To know more about video handling using OpenCV, check this: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
    
Enjoy, and have a Wonderful Day 😁

Additional Info: As of now, the precompiled source of opencv-gpu has been deleted from my drive, follow [this](https://towardsdatascience.com/how-to-use-opencv-with-gpu-on-colab-25594379945f) to make your own precompiled opencv-gpu
