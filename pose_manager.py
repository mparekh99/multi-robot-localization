import threading

class PoseManager:

    def __init__(self):
        self.lock = threading.Lock()
        self.robot_poses = {} 

    def update_pose(self, serial, x, y, theta):
        with self.lock:
            self.robot_poses[serial] =  (x, y, theta)

    def get_pose(self):
        with self.lock:
            return self.robot_poses.copy()
        
    