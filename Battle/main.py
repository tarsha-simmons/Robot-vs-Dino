#5 points): As a developer, I want to make a class for each of the following: Robot, Dinosaur, Weapon, Battlefield.
#(10 points): As a developer, I want a Dinosaur to have a name, health, and attack power.
#(10 points): As a developer, I want a Robot to have a name, health, and active_weapon.
#(10 points): As a developer, I want a Weapon to have a name and attack_power.
#(10 points): As a developer, I want a Dinosaur to have the ability to attack a Robot on a Battlefield. This attack method should lower a Robot’s health by the value of the Dinosaur’s attack_power.
#(10 points): As a developer, I want a Robot to have the ability to attack a Dinosaur on a Battlefield. This attack method should lower the Dinosaur’s health by the attack_power of the Robot’s active_weapon.
#(10 points): As a developer, I want the battle to conclude once either the robot or the dinosaur has its health points reduced to zero.
#Bonus points:
#(5 points): As a developer, I want to choose from a list of 3 possible weapons before a robot makes an attack.
#(5 points): As a developer, I want to create Fleet and Herd classes, allowing for a list of 3 Robots to battle against a list of 3 Dinosaurs.

from battlefield import Battlefield

battlefield = Battlefield()
battlefield.run_game()
