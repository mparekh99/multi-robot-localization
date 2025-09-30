import anki_vector 
import cv2 
import numpy as np
from PIL import Image 
import time
from anki_vector.util import degrees
from scipy.spatial.transform import Rotation as R
import pickle
import keyboard
import threading
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from enum import Enum
import matplotlib.pyplot as plt
import math
from utils import rotation_matrix_x, rotation_matrix_y, rotation_matrix_z
from world import Marker_World
from pose_tracker import PoseTracker
from pose_manager import PoseManager




def run_vector_localization(serial, pose_manager):
    robot = anki_vector.Robot(serial)
    robot.connect()

    robot.behavior.set_head_angle(degrees(7.0))
    robot.behavior.set_lift_height(0.0)
    robot.camera.init_camera_feed()

    pose_tracker = PoseTracker()

    try:
        while True:
            print("HELLO")
            frame_pil = robot.camera.latest_image.raw_image
            x,y,theta = pose_tracker.update_pose(frame_pil, robot)
            print(x, y, theta)
            pose_manager.update_pose(serial, x, y, theta)
        
    except KeyboardInterrupt:
        pass

    except Exception as e:
        print(f"Exception in loop: {e}")
    finally:
        robot.disconnect()