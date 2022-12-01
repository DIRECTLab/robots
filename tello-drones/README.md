# Tello EDU Drones
Inventory as of 11/4/22:
- Nine drones connect and fly.
    - One of these is checked out to P.A.S.E. with 3 batteries.
    - Another checked out to Michael with 2 batteries.
- Two drones (the ones in the drawer) connect, but return errors on takeoff.
- Some batteries don't work. Others only charge in the drones.
    - Blinking blue: Charging
    - Solid blue: Charged


## Capabilities
- Navigation
- Camera


## How to Use
- See https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf
    - Note that this didn't work on WSL for me, but it did work on Git Bash.
- When you turn on the drone, it should flash through the rainbow, then flash orange.
    - Solid red indicates low battery.
- Once the command `command` is sent, the light should change colors.

Common problems:
- Drone connects, but `takeoff` command returns `error`:
    1. Try `end`ing the program and running it again.
    2. Try switching batteries.
