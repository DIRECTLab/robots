# Blue Yahboom Tanks
Inventory as of 9/8/22:
- All 5 tanks have working motors and sonar.

Capabilities:
- Motor control for right and left tracks
- Sonar
- Camera is controlled through USB
- If you figure out how to use other capabilities, let us know!

How to use:
1. Turn the tank on and wait for it to beep.
2. Connect to Yahboom_Tank WiFi.
4. From the command line, run `./deploy.sh`.
    - Ensure the code you want to use is in `src/`. This command will send the directory `src/` to the tank.
    - Password is `yahboom`.
5. `ssh` into the tank as instructed.
6. Your code can be found in `python/src`. Run the python scripts to execute their code (e.g. `python demo.py`).
    - Basic commands are in `yahboom_tank.py`. See `demo.py ` and `test.py` for basic usage.
7. Exit SSH with `exit`. Turn off the robot and disconnect the battery.
