import random
from .character import Character

class Mage(Character):
    def __init__(self,name,):
        super().__init__(name, health=100, attack_power=35)
        self.mana = 120
        self.max_mana = 120
        self.teleport_chance = 0.3
        self.shield_active = False

    def fireball(self, opponent):
        if self.mana < 30:
            print(f"{self.name} doesn't have enough mana to cast a Fireball!")
            return
        damage = self.attack_power + 15
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        self.mana -= 30
        print(f"{self.name} casts Fireball and deals {damage} damage to {opponent.name}!")
        if opponent.health <= 0:
            print(f"Congratulations, {opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} has {opponent.health} health left.")

    def teleport(self):
        success = random.random() < self.teleport_chance
        if success:
            print(f"{self.name} teleported and avoids the next attack!")
            return success
        else:
            return False
        
    def mana_shield(self):
        if self.mana < 25:
            print(f"{self.name} doesn't have enough mana for Mana Shield!")
            return
        self.shield_active = True
        self.mana -= 25
        print(f"{self.name} casts a Mana Shield to block the next attack!")
        
    def has_shield(self):
        if self.shield_active:
            self.sheild_active = False
            return True
        return False

    def regenerate_mana(self, amount=10):
        self.mana = min(self.mana + amount, self.max_mana)

    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}/{self.max_mana}")