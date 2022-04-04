class Robot:

    def __init__(self,health,active_weapon):
        self.name = 'Optimus'
        self.health = 150
        self.active_weapon = 'ion blaster, sword, hydra cannon'

    
    def attack(self,dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon
        print(dinosaur.health)