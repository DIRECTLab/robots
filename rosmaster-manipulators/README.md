# Yahboom Rosmaster X3 Plus
Inventory as of 5/15/23:
- Rosmaster 1 servo 1 isn't working. Based on my tests (plugging the other robot's servo into this one), this is a hardware issue on the servo. Everything else seems to work well.
- Rasmaster 2 is in good condition.


## Capabilities
- Swedish wheels
- Manipulator
- Nice camera mounted on the body
- Another camera mounted on the manipulator
- Lidar
- Speaker
- Microphones


## How to Use
Documentation and tutorials for this robot can be found [here](http://www.yahboom.net/study/ROSMASTER-X3-PLUS).

To avoid accidental damage and avoid unnecessary power consumption, I recommend keeping the monitor unplugged when not in use.

### Via `ssh`
1. Turn the robot on and wait for it to beep.
    - The switch is on the robot's left side near the battery connection.
1. Connect your computer to the robot's WiFi ( `yahboom` or `ROSMASTER`).
    - Security key is `12345678`.
1. Run `ssh pi@yahboom` or a similar command.
    - Password is `yahboom`.
    - SSH tunneling (eg. `ssh pi@yahboom -L 8080:yahboom:8888`) can be useful, especially for running Jupyter Notebooks.
1. Run commands as desired.
    - Some useful Jupyter Notebooks can be found under `Rosmaster/samples/`.
        - Please don't change these files - make a copy before editing.
        - To prevent injuries to the robot, understand the code before running it, and make necessary precautions.
        - These notebooks are explained in section 5 of the documentation link above.
1. When finished: 
    1. `exit` SSH.
    2. Turn the robot off.

### Via phone app
There is a phone in the cupboard with the robots that has the app installed for controlling the robots. While using the app, beware that tilting the phone may cause the robot to move forward, backward or sideways.

Instructions for connecting the phone can be found under section 3.1 in the documentation.

### Via remote control
See section 3.3 in the documentation. Make sure the controller is turned on. 

The phone only displays the manipulator camera view in this mode and has no other functionality.

Note that the beep that means the controller is ready does not stop. Feel free to fix the code for that! Pressing R2 seems to make it stop. 

### Voice commands
The wakeup command is "Hi, Yahboom." For more info, see 14.1 in the documentation.


## Troubleshooting

### Python throws exception while logging / Other storage issues
The remote control program creates large log files. They eat up space on the SD card, so they need to be deleted from time to time.
1. `cd ~/.ros/log/`
2. Delete the large directories that look like gibberish (large sequnces of hex numbers).
