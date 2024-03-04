# Autonomous Robot Navigation

This Python program uses the HAL (Hardware Abstraction Layer) and GUI (Graphical User Interface) modules to control an autonomous robot. The robot uses laser data to navigate its environment, stopping and changing direction when it gets too close to an obstacle.

## Description

The program continuously reads the robot's laser data. If the robot is too close to an obstacle (determined by a threshold), it stops and changes direction. Otherwise, it continues moving forward. The robot's laser data is visualized using the `GUI.showNumpy` function. The robot's position and orientation are continuously updated.

## Features

- Autonomous navigation: The robot can navigate its environment without human intervention.
- Obstacle avoidance: The robot uses laser data to detect and avoid obstacles.
- Real-time visualization: The robot's laser data is visualized in real-time.

