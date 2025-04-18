import os
import pytest
from pyh264.encoder import H264Encoder



def test_video_encoder():
    encoder = H264Encoder()
    encoder.encode("assets/pdf.mov", "assets/test_video.mp4")

    assert os.path.exists("assets/test_video.mp4")
    assert os.path.getsize("assets/test_video.mp4") > 0


def test_image_encoder():
    encoder = H264Encoder()
    # Convert image to video
    # duration is optional, default is 5 seconds
    encoder.encode("assets/img.png", "assets/test_img.mp4", is_image=True, duration=15) 

    assert os.path.exists("assets/test_img.mp4")
    assert os.path.getsize("assets/test_img.mp4") > 0

