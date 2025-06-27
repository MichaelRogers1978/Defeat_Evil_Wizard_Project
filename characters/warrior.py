import random
from .character import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.power_attack_cooldown = 0
        self.energy = 100
        self.cry_active = False

    def power_attack(self, opponent):
        if self.power_attack_cooldown > 0:
            print(f"{self.name}'s power attack is on cooldown for {self.power_attack_cooldown} more turn(s).")
            return

        if self.energy < 20:
            print(f"{self.name} doesn't have enough energy to perfom a power attack yet.")
            return

        if random.random() < 0.2:
            print(f"{self.name} attempted a Power Attack but missed!")
            self.energy -= 10
            self.power_attack_cooldown = 3
            return

        damage = self.attack_power * 2
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        self.energy -= 20
        self.power_attack_cooldown = 2
        print(f"{self.name} uses a POWER ATTACK on {opponent.name} for {damage} amount of damage!")
        if opponent.health <= 0:
            print(f"Congratulations, {opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} still has {opponent.health} health left.")
            
    def battle_cry(self):
        self.cry_active = True
        print(f"{self.name} lets out a Battle Cry! Next attack will deal extra damage!")
        
    def boosted_attack(self):
        if self.cry_active:
            self.cry_active = False
            return self.attack_power + 15
        return self.attack_power

    def reduce_cooldowns(self):
        if self.power_attack_cooldown > 0:
            self.power_attack_cooldown -= 1

    def regenerate_energy(self, amount=5):
        self.energy = min(self.energy + amount, 100)

    def display_stats(self):
        super().display_stats()
        print(f"Energy: {self.energy}, Power Attack cooldown: {self.power_attack_cooldown}")
