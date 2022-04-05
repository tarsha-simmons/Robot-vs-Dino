from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots()
        self.create_fleet(self)

    def create_fleet(self):
        robot_one = Robot("Optimus Prime")
        robot_two = Robot("Bumblebee")
        robot_three = Robot("Megatron")