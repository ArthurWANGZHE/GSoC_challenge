```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_cmake hello_ros2 --dependencies rclcpp
```

Create 2 cpp files in `hello_ros2`
Under `~/ros2_ws/src/hello_ros2/src` create `publisher_node.cpp` and `subscriber_node.cpp`
Under `~/ros2_ws/src/hello_ros2`open CMakeLists.txt and add following lines:
```cmake

```cmake
cmake
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


Terminal 1
```bash
cd ~/ros2_ws/
colcon build --packages-select hello_ros2
source install/setup.bash
ros2 run hello_ros2 publisher_node
```


Terminal 2
```bash
source ~/ros2_ws/install/setup.bash
ros2 run hello_ros2 subscriber_node
```


