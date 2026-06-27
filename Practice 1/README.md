# Practice 1: Create a ROS2 Workspace Package 

In this practice, you will learn how to create a ROS 2 workspace and a basic package. You will set up the folder structure, build the package using colcon, and run simple ROS 2 commands. This is the first step to start developing projects in ROS 2 using either Python or C++.

## Learning Outcomes
By the end of this practice, users will:
- Create a ROS2 workspace and understand its folder structure
- Set up and configure the workspace environment
- Create ROS2 packages (in C++ or Python)
- Understand ROS2 package metadata file (package.xml)
- Build packages using colcon
- Source the workspace and run basic ROS2 commands
- Learn basic project organization in ROS2

## Mandatory Exercises:

Complete this section to achieve the core learning objectives ROS2 workspace and ROS 2 packages.

1. **Practice 1A: Creating a Workspace**
   - [1A.1: Creating a ROS 2 Workspace](#1a1-creating-a-workspace)  

2. **Practice 1B: Creating a ROS 2 Package**
   - [1B.1: Creating a ROS2 Python Package](#1b1-creating-ros2-python-packages)  
   - [1B.2: Creating a ROS2 C++ Package](#1b2-creating-ros2-cmake-package)
   - [1B.3: Building ROS2 Packages](#1b3-building-ros2-packages)
   - [1B.4: Sourcing and Verifying your ROS2 Packages](#1b4-sourcing-and-verifying-your-ros2-package)

## Additional Exercises (Optional):

Do these if you want to go further or explore more features related to ROS2 workspaces and packages.

3. **Practice 1C: Additional Arguments for ROS2 Package Creation**
   - [1C.1: Creating a ROS2 Package with Additional Arguments](#1c1-creating-a-ros2-package-with-additional-arguments)  

4. **Practice 1D: Setting up .bashrc File to source ROS2**
   - [1D.1: Setting up .bashrc File](#1d1-setting-up-bashrc-file-to-source-ros2)  

## 1A.1: Creating a Workspace
1. Open a terminal by pressing `ctrl` + `alt` + `T` on your keyboard.

2. In your Linux terminal , enter the following command:
```bash
mkdir training
cd training
mkdir new_workspace
cd new_workspace
mkdir src
cd src
```

**Explanation**
- `mkdir training`: This command creates a folder called `training` in the current directory.
- `cd training`: Changes the current directory to the `training` folder.
- `mkdir new_workspace`: This command creates a folder called `new_workspace` in the current directory.
- `cd new_workspace` : Changes the current directory to the `new_workspace` folder.
- `mkdir src`: This command creates a folder called `src` in the current directory.
   - Please remember that the ROS 2 packages must always be located in the src folder of the workspace.
- `cd src` : Changes the current directory to the `src` folder.

After running the above commands, you will have a folder named `training` that contains your ROS 2 workspace called `new_workspace`.

**Note:** Inside the `new_workspace` directory, the `src` folder serves as the source directory and will contain all your ROS 2 packages. This is where you create or clone individual packages, whether they're written in Python or C++. They can be built and managed together within the workspace.

## 1B.1: Creating ROS2 Python Packages

ROS 2 fully supports developing packages in Python, making it easy to write, run, and manage robotic applications using a high-level programming language.

1. Make sure you're currently inside the `src` folder. your current directory should be `~/training/new_workspace/src`

In your Linux terminal, run the following command:

```bash 
source /opt/ros/humble/setup.bash
ros2 pkg create --build-type ament_python my_python_package
```

**Explanation**
- `source /opt/ros/humble/setup.bash`: Configures your terminal to use ROS 2 Humble by setting up the necessary environment variables. You must run this command in every new terminal session unless you add it to your `.bashrc` file for automatic setup.
- `ros2 pkg create`: ROS2 command that creates a new ROS 2 package.
- `--build-type ament_python`: To specify the type of package to be created. In this case, it is a Python package.
- `my_python_package`: Name of the packaged to be created.

The following output below is expected: 

```bash
going to create a new package
package name: my_python_package
destination directory: /home/johnaa/training/new_workspace/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['johnaa <john_abogado@artc.a-star.edu.sg>']
licenses: ['TODO: License declaration']
build type: ament_python
dependencies: []
creating folder ./my_python_package
creating ./my_python_package/package.xml
creating source folder
creating folder ./my_python_package/my_python_package
creating ./my_python_package/setup.py
creating ./my_python_package/setup.cfg
creating folder ./my_python_package/resource
creating ./my_python_package/resource/my_python_package
creating ./my_python_package/my_python_package/__init__.py
creating folder ./my_python_package/test
creating ./my_python_package/test/test_copyright.py
creating ./my_python_package/test/test_flake8.py
creating ./my_python_package/test/test_pep257.py
```

You may notice a warning about an unknown license: `[WARNING]: Unknown license 'TODO: License declaration'.`
This warning simply means that a valid license hasn't been specified yet in the package.xml. This is okay for now!

2. A ROS 2 package named `my_python_package` will be created, and your directory structure should now look like this:

```bash
new_workspace/                      # This is the ROS2 workspace
├── src/                            
│   └── my_python_package/          # This is the Python ROS2 package
│       ├── my_python_package/      # Python module directory
│       │   └── __init__.py
│       ├── package.xml             # Package metadata
│       ├── setup.py                # Python build script
│       ├── setup.cfg               # Build config
│       └── resource/
│           └── my_python_package   # Ament resource index

```
**Inside my_python_package**

<img src="./Image/cmakepackage.png"  width="50%" height="50%">  
<br> 

## 1B.2: Creating ROS 2 CMake Package

ROS 2 has robust support for C++, making it the go-to language for performance-critical robotics applications such as real-time control, sensor processing, and embedded systems.

1. Make sure you're currently inside the src folder. your current directory should be `~/training/new_workspace/src`

In your Linux terminal, enter the following command

```linux
source /opt/ros/humble/setup.bash
ros2 pkg create --build-type ament_cmake my_cmake_package
```

**Explanation**
- `source /opt/ros/humble/setup.bash`: Configures your terminal to use ROS 2 Humble by setting up the necessary environment variables. You must run this command in every new terminal session unless you add it to your `.bashrc` file for automatic setup.
- `ros2 pkg create`: ROS2 command that creates a new ROS 2 package.
- `--build-type ament_cmake`: The purpose of this part is to specify the type of package to be created. In this case, it’s a CMake package.
- `my_cmake_package`: Name given to package. 

The following output below is expected:

```bash
going to create a new package
package name: my_cmake_package
destination directory: /home/johnaa/training/new_workspace/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['johnaa <john_abogado@artc.a-star.edu.sg>']
licenses: ['TODO: License declaration']
build type: ament_cmake
dependencies: []
creating folder ./my_cmake_package
creating ./my_cmake_package/package.xml
creating source and include folder
creating folder ./my_cmake_package/src
creating folder ./my_cmake_package/include/my_cmake_package
creating ./my_cmake_package/CMakeLists.txt
```
You may notice a warning about an unknown license: [WARNING]: Unknown license 'TODO: License declaration'. This warning simply means that a valid license hasn't been specified yet in the package.xml. This is okay for now!

2. A ROS 2 package named `my_cmake_package` will be created, and your directory structure should now look like this:

```bash
new_workspace/                      # This is the ROS2 workspace
├── src/
│   └── my_cmake_package/           # This is the C++ ROS2 package
│       ├── CMakeLists.txt          # Build instructions (CMake)
│       ├── package.xml             # Package metadata
│       ├── include/
│       │   └── my_cmake_package/   # Header files go here
│       └── src/                    # C++ source (.cpp) files go here
```

**Inside ROS2 CMake Package**

<img src="./Image/pythonpackage.png"  width="50%" height="50%">  
<br> 

## 1B.3: Building ROS2 Packages

1. In your Linux terminal, enter the following command to build all the packages inside your workspaces.

Make sure you're in the `~/training/new_workspace` directory, then run the following command to build your workspace.
```bash 
cd ~/training/new_workspace
colcon build
```
It compiles C++ code and prepares Python packages for use.
It generates the necessary build and install files so ROS 2 can find and execute your packages.
Ensures all dependencies are correctly handled before running any ROS 2 nodes.

After a succesful build, you should see the following output from the terminal:

<img src="./Image/successful_build_output.png"  width="50%" height="50%">  
<br> 

A popup will also show up (shown below):

<img src="./Image/build_successful.png"  width="%" height="50%">  
<br> 


2. To build a specific package(s) inside the workspace:

```bash 
colcon build --packages-select <package_name_1> <package_name_2>
```
Why build specific packages?
- **Faster builds:** When working on large workspaces, building only the packages you're actively modifying saves time.
- **Focused debugging:** Helps isolate issues by compiling only relevant packages.
- **Avoid unnecessary rebuilds:** Skips rebuilding unchanged or unrelated packages, improving development efficiency.
- **Better resource usage:** Reduces CPU and memory load during the build process, especially helpful on limited systems.

3. To build all packages inside the workspace except a package(s):

```bash 
colcon build --packages-ignore <package_name_1> <package_name_2>
```

## 1B.4: Sourcing and Verifying Your ROS2 Package
1. Ensure that your workspace are correct, after colcon build command, three files will be created (as shown below)

```bash
new_workspace/                      # This is the ROS 2 workspace
├── src/                            
│   ├── my_python_package/          # Python ROS 2 package
│   │   ├── my_python_package/      # Python module directory
│   │   │   └── __init__.py
│   │   ├── package.xml             # Package metadata
│   │   ├── setup.py                # Python build script
│   │   ├── setup.cfg               # Build config
│   │   └── resource/
│   │       └── my_python_package   # Ament resource index
│   └── my_cmake_package/           # C++ ROS 2 package
│       ├── CMakeLists.txt          # Build instructions (CMake)
│       ├── package.xml             # Package metadata
│       ├── include/
│       │   └── my_cmake_package/   # Header files
│       └── src/                    # C++ source files
├── build/                          # Created after colcon build
├── install/                        # Created after colcon build
└── log/                            # Created after colcon build
```

**Explanation**

 - `build`: Contains temporary build files and intermediate outputs. Each package gets its own subdirectory here. It's mainly used during the compilation and linking process.
- `install`: Contains the final, usable version of your built packages. ROS 2 uses this directory to run nodes, source setup scripts, and manage environment paths.
- `log`: Stores logs from the build process, such as errors, warnings, and other output messages. Useful for troubleshooting build issues.

2. After successfully building your ROS2 packages, you need to source it to make your ROS 2 packages available for use.

Make sure you're in the `~/training/new_workspace` directory, then run the following command to source your workspace.

```bash 
source install/setup.bash
```

Now that you have sourced your workspace, your terminal session is aware of the packages and environment set up within that workspace. This means you can run ROS 2 commands that interact with the packages you’ve created or built, such as listing packages, launching nodes, or running executables from your workspace.

2. In your Linux terminal,  enter the following command to list all ROS2 packages available.

```bash 
ros2 pkg list
```
You may notice that your ROS 2 installation includes many pre-installed packages by default, which can make it difficult to easily locate your own package in the list.

3. To find your package, enter the following command

```bash 
ros2 pkg list | grep my_python_package
```
The command `ros2 pkg list | grep my_python_package` lists all available ROS 2 packages and filters the output to show only those that include the name my_python_package.

4. To view your package details (XML format), enter the following command

```bash 
ros2 pkg xml my_python_package
```
The command `ros2 pkg xml my_python_package` is used to display the contents of the package.xml file for the specified ROS 2 package. This file contains important metadata such as the package name, version, description, maintainer information, license, and dependencies.

5. To view your package executables

```bash 
ros2 pkg executables my_python_package
```
The command `ros2 pkg executables my_python_package` lists all executable entry points (nodes or scripts) defined within the `my_python_package`. For now, there are no executables in the package, but they will be created in the next lesson.

## 1C.1: Creating a ROS2 Package with Additional Arguments

1. To create a ROS2 package with nodes (C++)

```bash 
ros2 pkg create --build-type ament_cmake --node-name cmake_node my_cmake_package_new
```

2. To create a ROS2 package with nodes (Python)

```bash 
ros2 pkg create --build-type ament_python --node-name python_node my_python_package_new
```
Build and source your workspace! Now check for `my_cmake_package_new`and `my_python_package_new` executables.

3. To view brief description of additional arguments of ros2 pkg create command, enter the following command:

```bash 
ros2 pkg create -h
```

**Challenge**

1. Create your own package (C++ or Python) with the following added dependencies. 
    - `rclcpp`
    - `std_msgs`

## 1D.1: Setting up .bashrc File to source ROS2

Sourcing ROS 2 manually every time you open a new terminal can be tedious. To make ROS 2 commands like `ros2 pkg create` and `ros2 pkg list` available automatically, you can add the source command to your .bashrc file. This way, ROS 2 will be sourced each time you open a terminal session, saving you from having to do it manually.

```linux 
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
Now, ROS 2 will be ready to use every time you open a terminal!

Warning!!! modifying .bashrc should be done with caution, as incorrect changes can cause issues with your terminal environment.





