# Practical 8: Creating ROS2 Custom Service Interface and Service Server

In this practical, participants will learn how to define, build, and use a custom service interface within a ROS 2 package for handling camera feedback and retrieving object pose information. This scenario reflects a common robotics use case where a node (e.g., a perception system) processes camera data and another node requests the pose of a detected object. By implementing a custom service, participants will learn how to structure both the request (e.g., object ID or type) and the response (e.g., position and orientation of the object) to enable efficient and clear communication between nodes.

## Learning Outcomes

By the end of this practical, learners will be able to:
- Understand the structure and syntax of ROS 2 custom service (.srv) files
- Define a custom service interface with specific request and response fields
- Configure and build a ROS 2 package to include the custom service definition
- Implement a ROS 2 service server that processes custom service requests and returns appropriate responses
- Use ROS 2 CLI tools such as ros2 service call and ros2 interface show to test and debug custom services
- Integrate the custom service into a larger ROS 2 system with publishers or subscribers

## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS 2 Custom Services.

1. **Practice 8A: Creating a Custom Service Interface**

   - [8A.1: Creating a Custom Service Interface](#8a1-creating-a-custom-service-interface)
   - [8A.2: Verifying your Custom Service Interface](#8a2-verifying-your-custom-service-interface)

2. **Practice 8B: Creating a Service Server**

   - [8B.3: Creating a Service Server](#8b3-creating-a-service-server)
   - [8B.4: Verifying your Service Server](#8b4-verifying-your-service-server)

3. **Practice 8C: Creating a Service Client**

   - [8B.5: Creating a Service Client](#8b5-creating-a-service-client)
   - [8B.6: Verifying your Service Client](#8b6-verifying-your-service-client)

## 8A.1: Creating a Custom Service Interface

1. Create an interface package called `perception_msgs` in `ros2_ws` workspace

2. In the `perception_msgs` package, create a directory named`srv`

3. In the `perception_msgs/srv` directory, Add a service interface `GetObjectLocation.srv` that contains:
    - An empty service **request** field 
    - A service **result** that contains:
        - a **bool** type field named `result`,
        - a **geometry_msgs/Pose** type field named `object_pose`

4. Inside your CMakelist.txt, include the necessary dependencies below `# find_package(<dependency> REQUIRED)`

```
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
rosidl_generate_interfaces(${PROJECT_NAME}
    "srv/GetObjectLocation.srv"
  DEPENDENCIES geometry_msgs
)
```
5. Inside your `package.xml` file , include the following dependecies within the `<package>` element of `package.xml` file.

```
<buildtool_depend>rosidl_default_generators</buildtool_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
6. Build your `perception_msgs` package. 
## 8A.2: Verifying your Custom Service Interface

Before doing this. **REMEMBER TO BUILD AND SOURCE YOUR WORKSPACE**

To check if your solution works, run the following 

1. Querying Information about ROS2 Interfaces

In another terminal within your VM, ensure that you have **SOURCED YOUR ROS DISTRO AND YOUR WORKSPACE AND EXPORTED THE `ROS_DOMAIN_ID` IN YOUR ENVIRONMENT**, then run the following command:

```bash
ros2 interface list

or 

ros2 interface list | grep GetObjectLocation          ## to specifically look for GetObjectLocation
```

You should be able to see `perception_msgs/srv/GetObjectLocation` as one of the interfaces under `Services`

```bash
    johnaa@johnaa-aftershock:~/ros2_ws$ ros2 interface list | grep GetObjectLocation
        perception_msgs/srv/GetObjectLocation
```

2.  To view details of a ROS2 service interface


```bash
    ros2 interface show <service message>
    
    # To view perception_msgs/srv/GetObjectLocation
    ros2 interface show perception_msgs/srv/GetObjectLocation
```
## 8B.3: Creating a Service Server

1. Create a ROS 2 package named `camera_service`

2. Create a ROS 2 executable in this package named `aruco_detection_node`

    You may use the provided `aruco_detection_node.py` and `transformations.py` as a starting point for your code. **Both files are provided in this practice's `student copy/` folder in the repository — copy both of them into your package's `camera_service/camera_service/` directory.** The file `aruco_detection_node.py` contains:
    1. The `ArucoDetection` class to be used for image detection. 
    2. A subscriber that processes and stores the object coordinates detected by the perception system

    Do not edit the `transformations.py` ! 


3. Navigate to the `ros2_ws/src/camera_service/camera_service` directory and store the `ArucoDetection` file there.

    - Inside the `ArucoDetection` file . Do the following 
        - Create a ROS 2 Service **Server** named `find_objects` that returns the stored coordinates to the client requesting for this service.
        - Note that in this exercise, you will need to add a **callback group** to your service. 
        - Dont worry! for this exercise all you need to do is to add another parameter `callback_group = server_cb_group` as the last parameter when calling the `create_service` function

        - Use the GetObjectLocation service type as the type for this Server.

## 8B.4: Verifying your Service Server

Before doing this. **REMEMBER TO BUILD AND SOURCE YOUR WORKSPACE**

To check if your solution works, run the following 

1. Run the camera driver on the turtlebot3
Before running the camera driver, ensure that you have **CONNECTED TO THE SAME NETWORK AS YOUR TURTLEBOT AND EXPORTED THE `ROS_DOMAIN_ID` IN YOUR ENVIRONMENT**

```bash
ssh ubuntu@<ip_address>

ros2 launch camera_calibration_pkg camera_calibration.launch.py 
```

2. Run your image viewer node

```bash
ros2 run camera_service aruco_detection_node
```
<img src="./images/object_detection.png"  width="80%" height="80%">
<br>

2 If you do not have a physical Aruco Marker, you can go to this website and generate an one!

Ensure that the Aruco marker dictionary is 5x5 (50, 100, 250, 1000)

Go to this link: 
[aruco_marker_generator](https://chev.me/arucogen/)

3. Run a service client via the command line

```bash
ros2 service call /find_objects perception_msgs/srv/GetObjectLocation "{}"
```

3. Expected Output 

<img src="./images/service_call_screenshot.png"  width="80%" height="80%">
<br>
