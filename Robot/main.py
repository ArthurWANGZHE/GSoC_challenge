import math
import numpy as np
import random
from GUI import GUI
from HAL import HAL

def parse_laser_data(laser_data):
    laser = []
    for i in range(180):
        dist = laser_data.values[i]
        angle = math.radians(i)
        laser.append((dist, angle))
    return laser


def laser_vector(laser):
    laser_vectorized = []
    for d, a in laser:
        x = d * math.cos(a) * -1
        y = d * math.sin(a) * -1
        v = (x, y)
        laser_vectorized.append(v)

    laser_mean = np.mean(laser_vectorized, axis=0)
    return laser_mean



threshold = 0.5

while True:
    try:

        laser_data = HAL.getLaserData()
        parsed_laser_data = parse_laser_data(laser_data)
        laser_mean_vector = laser_vector(parsed_laser_data)


        if any(dist < threshold for dist, _ in parsed_laser_data):

            HAL.setV(0.0)
            # a=random.uniform(-5.0,-0.1)
            HAL.setW(-0.1)
            # HAL.setW(a)
        else:
            HAL.setV(10)
            # b = random.uniform(0.0, 5.0)
            HAL.setW(0.1)
            # HAL.setW(b)


        laser_matrix = np.random.randint(0, 128, (400, 400), dtype=np.uint8)
        GUI.showNumpy(laser_matrix)


        robot_x = HAL.getPose3d().x
        robot_y = HAL.getPose3d().y
        robot_orientation = HAL.getPose3d().yaw

    except Exception as e:
        print("An error occurred: ", e)

    finally:

        if HAL.getBumperData().state == 1:
            break
