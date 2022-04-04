class Dino:

    def __init__(self,name,health,attack_power):
     self.name = 'Grimlock'
     self.health = 175
     self.attack_power = 75

     def attack(self,robot):
         robot.health = robot.health - self.attack_power
         print(f'{robot.health} is health!')