from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots()
        self.create_fleet(self)

    def create_fleet(self):
        robot_one = Robot("Optimus Prime, 200, ion blast")
        robot_two = Robot("Bumblebee, 100, plasma cannon")
        robot_three = Robot("Megatron, 100, megablast")
        return[robot_one,robot_two,robot_three]