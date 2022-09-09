from yahboom_tank import YahboomTank
import time

tank = YahboomTank()

try:
  while True:
    dist = tank.get_sonar_distance()
    print(dist)
    if dist > 65:
      tank.set_motor_ratios(0.25, 0.25)
    else:
      tank.set_motor_ratios(-0.25, -0.25)
    time.sleep(1)


except KeyboardInterrupt:
  pass

tank.destroy()