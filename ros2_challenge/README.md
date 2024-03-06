# ROS2 Hello World

This repository contains a simple ROS2 (Robot Operating System 2) package named `hello_ros2`. The package includes two nodes: a publisher node and a subscriber node. The publisher node publishes messages, and the subscriber node listens to these messages.


## Setup and Build

1. Create a new ROS2 workspace and navigate into it:

    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ```

2. Create a new ROS2 package named `hello_ros2` with `rclcpp` as a dependency:

    ```bash
    ros2 pkg create --build-type ament_cmake hello_ros2 --dependencies rclcpp
    ```

3. Create two C++ source files (`publisher_node.cpp` and `subscriber_node.cpp`) in the `src` directory of the `hello_ros2` package.

4. Open the `CMakeLists.txt` file in the `hello_ros2` package directory and add the following lines to define the build instructions for the two nodes:

    ```cmake
    cmake_minimum_required(VERSION 3.5)
    project(hello_ros2)

    find_package(rclcpp REQUIRED)
    find_package(std_msgs REQUIRED)

    add_executable(publisher_node src/publisher_node.cpp)
    ament_target_dependencies(publisher_node rclcpp std_msgs)

    add_executable(subscriber_node src/subscriber_node.cpp)
    ament_target_dependencies(subscriber_node rclcpp std_msgs)

    install(TARGETS
      publisher_node
      subscriber_node
      DESTINATION lib/${PROJECT_NAME}
    )

    ament_package()
    ```

5. Build the `hello_ros2` package:

    ```bash
    cd ~/ros2_ws/
    colcon build --packages-select hello_ros2
    source install/setup.bash
    ```

## Running the Nodes

1. In the first terminal, run the publisher node:

    ```bash
    ros2 run hello_ros2 publisher_node
    ```

2. In a second terminal, run the subscriber node:

    ```bash
    source ~/ros2_ws/install/setup.bash
    ros2 run hello_ros2 subscriber_node
    ```

## Demo
https://www.youtube.com/watch?v=zywZc0RT6pw


