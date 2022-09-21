# Green Yahboom Manipulators
Inventory as of 9/16/22:
- Working camera, RGB light, speaker and servos on jetson platform
- The raspberry pi one is having several problems:
    - The raspberry pi is not receiving power (or sufficient power) from the Arduino
    - When the raspberry pi is powered separately, any attempt at at communicating with the servos results in an "I2C error"
    - Some sort of connection problem?
        - Using the wire ribbon from the other manipulator did not help


Capabilities:
- Read and write angles of all six servos
- RGB light and beeping noise
- USB Camera


How to use:
1. Connect a monitor, keyboard and mouse to the robot.
2. Turn the manipulator on and open a terminal.
3. Run the desired Python code.
    - Be careful not to ask the robot to do something that might break it or strain the wires.
    - http://www.yahboom.net/study/Dofbot-Jetson_nano (Jetson) and http://www.yahboom.net/study/Dofbot-Pi (Raspberry Pi) explain the API for these robots. See section 6 (starting at `Introduction of API`), which should work without any extra installation.
