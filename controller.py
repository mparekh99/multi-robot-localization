# controller.py
import keyboard
import time

control_state_1 = {"up": False, "down": False, "left": False, "right": False}
control_state_2 = {"up": False, "down": False, "left": False, "right": False}

def teleop_listener():
    while True:
        control_state_1["up"] = keyboard.is_pressed("w")
        control_state_1["down"] = keyboard.is_pressed("s")
        control_state_1["left"] = keyboard.is_pressed("a")
        control_state_1["right"] = keyboard.is_pressed("d")

        control_state_2["up"] = keyboard.is_pressed("up")
        control_state_2["down"] = keyboard.is_pressed("down")
        control_state_2["left"] = keyboard.is_pressed("left")
        control_state_2["right"] = keyboard.is_pressed("right")

        time.sleep(0.01)

def control_robot_1(robot):
    while True:
        if control_state_1["up"]:
            robot.motors.set_wheel_motors(100, 100)
        elif control_state_1["down"]:
            robot.motors.set_wheel_motors(-100, -100)
        elif control_state_1["left"]:
            robot.motors.set_wheel_motors(-50, 50)
        elif control_state_1["right"]:
            robot.motors.set_wheel_motors(50, -50)
        else:
            robot.motors.set_wheel_motors(0, 0)
        time.sleep(0.05)

def control_robot_2(robot):
    while True:
        if control_state_2["up"]:
            robot.motors.set_wheel_motors(100, 100)
        elif control_state_2["down"]:
            robot.motors.set_wheel_motors(-100, -100)
        elif control_state_2["left"]:
            robot.motors.set_wheel_motors(-50, 50)
        elif control_state_2["right"]:
            robot.motors.set_wheel_motors(50, -50)
        else:
            robot.motors.set_wheel_motors(0, 0)
        time.sleep(0.05)
