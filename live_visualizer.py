import anki_vector 
import cv2 
import numpy as np
from PIL import Image 
import time
from anki_vector.util import degrees
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
from pose_manager import PoseManager
from world import Marker_World



def visualize_poses(pose_manager):
    world = Marker_World()
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(-600, 600)
    ax.set_ylim(-600,600)
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.grid(True)

    while True:
        ax.clear()
        ax.set_xlim(-600,600)
        ax.set_ylim(-600, 600)

        for marker_id, marker_data in world.marker_transforms.items():
            x, y, _ = marker_data["pos"]
            ax.plot(x, y, 'ro')
            ax.text(x + 5, y + 5, f"Marker {marker_id}", color='red', fontsize=8)


        poses = pose_manager.get_pose()
        for serial, (x,y,theta) in poses.items():
            ax.plot(x, y, 'bo')
            ax.text(x + 10, y + 10, f"Robot {serial[:4]}'", color='blue')

            # Draw heading 
            length = 40
            dx = length * math.cos(theta)
            dy = length * math.sin(theta)
            ax.arrow(x, y, dx, dy, head_width=15, fc='blue', ec='blue')

        plt.pause(0.05)