# Blue Yahboom Tanks
Current inventory as of 9/8/22:
- 5 tanks in total

Capabilities:
- Motor control for right and left tracks
- Sonar

How to use:
1. Turn the tank on and wait for it to beep.
2. Connect to Yahboom_Tank WiFi.
4. From the command line, run `./deploy.sh`.
    - Ensure the code you want to use is in `src/`. This command will send the directory `src/` to the tank.
    - Password is `yahboom`.
5. `ssh` into the tank as instructed.
6. Your code can be found in `python/src`. Run the python scripts to execute their code (e.g. `python demo.py`).
7. Exit SSH with `exit`. Turn off the robot and disconnect the battery.
