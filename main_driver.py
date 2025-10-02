import anki_vector
from pose_tracker import PoseTracker
from pose_manager import PoseManager
import threading
from live_visualizer import visualize_poses
from localize import run_vector_localization

# Import your controller module
import controller

def main():
    serials = ["00806b78", "00603f86"]
    pose_manager = PoseManager()

    robots = {}
    for serial in serials:
        robots[serial] = anki_vector.Robot(serial)
        robots[serial].connect()

    # Start the teleop listener thread once
    threading.Thread(target=controller.teleop_listener, daemon=True).start()

    # Start localization threads
    for serial in serials:
        threading.Thread(target=run_vector_localization, args=(serial, pose_manager), daemon=True).start()

    # Start control threads using your existing controller functions
    threading.Thread(target=controller.control_robot_1, args=(robots["00806b78"],), daemon=True).start()
    threading.Thread(target=controller.control_robot_2, args=(robots["00603f86"],), daemon=True).start()

    try:
        visualize_poses(pose_manager)
    except KeyboardInterrupt:
        print("EXITTING!!!")
    finally:
        for robot in robots.values():
            robot.disconnect()

if __name__ == "__main__":
    main()
