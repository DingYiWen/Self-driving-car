env_name = "Car\Car"  # Name of the Unity environment binary to launch
train_mode = True  # Whether to run the environment in training or inference mode

import matplotlib.pyplot as plt
import numpy as np
import sys
import cv2
import tensorflow as tf
from numpy import newaxis
from sklearn.utils import shuffle
from unityagents import UnityEnvironment
import yolo as yl
from PIL import Image


print("Python version:")
print(sys.version)

yolo=yl.YOLO()

# check Python version
if (sys.version_info[0] < 3):
    raise Exception("ERROR: ML-Agents Toolkit (v0.3 onwards) requires Python 3")

env = UnityEnvironment(file_name=env_name)

# Examine environment parameters
print(str(env))

# Set the default brain to work with
default_brain = env.brain_names[0]
brain = env.brains[default_brain]

env_info = env.reset(train_mode=train_mode)[default_brain]

for episode in range(300):
    # Reset the environment
    img1=env_info.visual_observations[0][0]*255
    image=Image.fromarray(img1.astype(np.uint8))
    r_image,action = yolo.detect_image(image)
    env_info = env.step([action])[default_brain]
    env_info = env.step([action])[default_brain]
    env_info = env.step([action])[default_brain]
    #r_image.show()
    r_image.save(str(episode)+".jpg")

env.close()
yolo.close_session()



