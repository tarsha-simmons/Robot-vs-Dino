class Robot:

    def __init__(self,health,active_weapon):
        self.name = 'Optimus'
        self.health = 150
        self.active_weapon = 'ion blaster, sword, hydra cannon'

    
    def attack(self,dino):
        dino.damage = dino.health - self.active_weapon
        dino.health = dino.damage
        print(f'{dino.damage} is dino Health!')