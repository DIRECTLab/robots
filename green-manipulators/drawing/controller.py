import time
from Arm_Lib import Arm_Device
from threading import Lock


class Controller:
    """
    Low-level arm controls.
    Best used as a singleton; import the instance at the bottom.
    """
    arm = Arm_Device()
    __writeLock = Lock()

    def __init__(self):
        time.sleep(0.1)

    def read_all(self) -> list:
        return [
            Controller.arm.Arm_serial_servo_read(1),
            Controller.arm.Arm_serial_servo_read(2),
            Controller.arm.Arm_serial_servo_read(3),
            Controller.arm.Arm_serial_servo_read(4),
            Controller.arm.Arm_serial_servo_read(5),
            Controller.arm.Arm_serial_servo_read(6),
        ]

    def move_all(self, servos, t: int) -> bool:
        if len(servos) == 6:
            with Controller.__writeLock:
                Controller.arm.Arm_serial_servo_write6(*servos, t)
                time.sleep(t / 1000)
            return True
        return False

    def move(self, servo: int, angle: int, t: int) -> bool:
        if servo >= 1 and servo <= 6 and angle >= 0 and angle <= 180:
            with Controller.__writeLock:
                Controller.arm.Arm_serial_servo_write(servo, angle, t)
                time.sleep(t / 1000)
            return True
        return False


controller = Controller()
