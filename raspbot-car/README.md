# Yahboom Raspbot Cars
Inventory as of 11/1/22:
- 3 cars are built
- 2 more are still in boxes


## Capabilities
- Skid steering
- Buzzer
- Camera with 2 servos for camera control
- Sonar
- Infrared sensors


## How to Use
1. Turn the robot on and wait for it to beep.
2. SSH into the robot.
    1. Ensure the robot and the computer are connected to the same WIFI.
    2. On your computer, run `ssh [username]@[ip.address]` or a similar command.
        - The default username is `pi`. You can confirm this by opening a terminal on the pi.
        - Get the robot's IP address by opening a terminal on the pi and running `hostname -I`.
        - Password is `yahboom`.
        - SSH tunneling (eg. `ssh [username]@[ip.address] -L 8080:[ip.address]:8888`) can be useful, especially for running Jupyter Notebooks.
3. Run commands as desired.
    - Useful documentation for controlling the robot can be found [here](http://www.yahboom.net/study/Raspbot). See especially `5.Hardware Control Course`.
    - Some tutorials (Jupyter Notebook files) can be found under `Yahboom_project/Raspbot/`. They go along with the manual above.
        - Please don't change these files - make a copy before editing.
        - To prevent injuries to the robot, understand the code before running it, and make necessary precautions. For example, I recommend setting up some sort of bumper when trying `Ultrasonic avoid`.
    - `Yahboom_project/Raspbot/raspbot/YB_Pcb_Car.py` helps with lots of the motor controls.
        - Please don't change this file - make a copy of it before editing.
4. When finished, turn the robot off and disconnect the battery.
