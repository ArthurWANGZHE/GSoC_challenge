import math
import numpy as np
import random
from GUI import GUI
from HAL import HAL


# Function to parse laser data
def parse_laser_data(laser_data):
    laser = []
    for i in range(180):
        dist = laser_data.values[i]
        angle = math.radians(i)
        laser.append((dist, angle))
    return laser


# Function to convert laser data to a vector
def laser_vector(laser):
    laser_vectorized = []
    for d, a in laser:
        x = d * math.cos(a) * -1
        y = d * math.sin(a) * -1
        v = (x, y)
        laser_vectorized.append(v)

    laser_mean = np.mean(laser_vectorized, axis=0)
    return laser_mean


# Main loop for the robot
threshold = 0.5  # Define the threshold distance for obstacle detection

while True:
    try:
        # Get laser data
        laser_data = HAL.getLaserData()

        # Parse and convert laser data
        parsed_laser_data = parse_laser_data(laser_data)
        laser_mean_vector = laser_vector(parsed_laser_data)

        # Perform obstacle avoidance logic
        if any(dist < threshold for dist, _ in parsed_laser_data):
            # Obstacle detected, implement avoidance logic
            HAL.setV(0.0)  # Stop the robot
            #          a=random.uniform(-5.0,-0.1)
            HAL.setW(-0.1)  # Rotate the robot to avoid the obstacle
        else:
            # No obstacles detected, continue normal operation
            HAL.setV(10)  # Set linear speed
            b = random.uniform(0.0, 5.0)
            HAL.setW(b)  # Set angular velocity

        # Display the laser data on the GUI
        laser_matrix = np.random.randint(0, 128, (400, 400), dtype=np.uint8)
        GUI.showNumpy(laser_matrix)

        # Get the position and orientation of the robot
        robot_x = HAL.getPose3d().x
        robot_y = HAL.getPose3d().y
        robot_orientation = HAL.getPose3d().yaw

    except Exception as e:
        print("An error occurred: ", e)

    finally:
        # Check if the robot has collided
        if HAL.getBumperData().state == 1:
    #