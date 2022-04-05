class Dino:

    def __init__(self,name,health,attack_power):
     self.name = name
     self.health = attack_power
     self.attack_power = health

     def attack(self,robot):
         attack_names = ['ion blast','sword slash', 'canon blast']
         robot.health = robot.health - self.attack_power
         print(f'{robot.health} is health!')