from controller import Controller


class Artist(Controller):
    """
    High-level drawing controls. Assumes standard Expo marker, no cap.
    Best used as a singleton; import the instance at the bottom.
    """
    default_t = 2000

    def __init__(self):
        super().__init__()

    def draw(self, forward: float, rotate=None, t: int=default_t) -> bool:
        """
        Moves the arm to a drawing position.
        `amount`: 0 is closest to the base. 1 is furthest from it.
        `rotate`: The angle to rotate the base to (if desired).
        Gripper and "wrist" angles are maintained (if readable).
        """
        if forward < 0 or forward > 1:
            return False

        min2 = 120
        max2 = 34 #40
        min3 = 0
        max3 = 48
        min4 = 0
        max4 = 70 #48

        diff2 = max2 - min2
        diff3 = max3 - min3
        diff4 = max4 - min4

        set1 = Controller.arm.Arm_serial_servo_read(1) if rotate is None else rotate
        set2 = min2 + round(diff2 * forward)
        set3 = min3 + round(diff3 * forward)
        set4 = min4 + round(diff4 * forward)
        set5 = Controller.arm.Arm_serial_servo_read(5)
        set6 = Controller.arm.Arm_serial_servo_read(6)
        new_positions = [set1, set2, set3, set4, set5, set6]
        for idx, pos in enumerate(new_positions):
            if pos is None:
                new_positions[idx] = 90

        return self.move_all(new_positions, t)

    def rotate(self, angle: int, t: int=default_t) -> bool:
        """
        Rotates the arm, same as move(1, angle, t).
        """
        return self.move(1, angle, t)

    def up(self, t: int=default_t) -> bool:
        """
        Returns the arm to an upright position.
        Gripper and rotation angles are maintained (if readable).
        """
        set1 = Controller.arm.Arm_serial_servo_read(1)
        set2 = 90
        set3 = 90
        set4 = 90
        set5 = Controller.arm.Arm_serial_servo_read(5)
        set6 = Controller.arm.Arm_serial_servo_read(6)
        new_positions = [set1, set2, set3, set4, set5, set6]
        for idx, pos in enumerate(new_positions):
            if pos is None:
                new_positions[idx] = 90

        return self.move_all(new_positions, t)

    def out(self, t:int=default_t) -> bool:
        """
        Returns the arm to a right angle.
        Gripper and "wrist" angles are maintained (if readable).
        """
        set1 = 90
        set2 = 90
        set3 = 90
        set4 = 0
        set5 = Controller.arm.Arm_serial_servo_read(5)
        set6 = Controller.arm.Arm_serial_servo_read(6)
        new_positions = [set1, set2, set3, set4, set5, set6]
        for idx, pos in enumerate(new_positions):
            if pos is None:
                new_positions[idx] = 90

        return self.move_all(new_positions, t)
    

artist = Artist()
