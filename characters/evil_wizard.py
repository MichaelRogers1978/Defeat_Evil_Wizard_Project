import random
from .character import Character

class EvilWizard(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
        self.mana = 100
        self.max_mana = 100
        self.dark_spell_cooldown = 1

    def attack(self, opponent):
        if hasattr(opponent, "teleport") and callable(opponent.teleport):
            if opponent.teleport():
                print(f"{self.name}'s attack missed because {opponent.name} has teleported!")
                return
            if random.random() < 0.1:
                print(f"{self.name} taunts: 'you cannot defeat me, {opponent.name}!")
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage.")
        if opponent.health <= 0:
            print(f"Congratulations, {opponent.name} has been defeated")
        else:
            print(f"{opponent.name} has {opponent.health} health left.")
        self.health = min(self.health + 2, self.max_health)
        print(f"{self.name} regenerates 2 health after attacking! Now at {self.health}/{self.max_health} health.")

    def dark_spell(self, opponent):
        if self.dark_spell_cooldown > 1:
            print(f"{self.name}'s Dark Spell is recharging for {self.dark_spell_cooldown} more turn(s).")
            return
        if self.mana < 30:
            print(f"{self.name} doesn't have enough mana to cast a Dark Spell.")
            return

        damage = self.attack_power * 3
        opponent.health -= damage
        self.mana -= 40
        self.dark_spell_cooldown = 5

        print(f"{self.name} cast a Dark Spell! {opponent.name} takes {damage} of damage!")

        damage = 10
        heal_amount = 15

        opponent.health -= damage
        self.health += heal_amount
        self.health = min(self.health, self.max_health)
        self.mana -= 25

        print(f"{self.name} drains life from {opponent.name}, dealing {damage} damage and healing {heal_amount} in health!")
        self.evil_laugh()

    def evil_laugh(self):
        print(f"{self.name} lets out spine-chilling, soul-crushing, deep, dark, evil laugh... gggrrrahahahah!")

    def reduce_cooldowns(self):
        if self.dark_spell_cooldown > 0:
            self.dark_spell_cooldown -= 1

    def regenerate_mana(self, amount=10):
        self.mana = min(self.mana + amount, self.max_mana)

    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}/{self.max_mana}, Dark Spell Cooldown: {self.dark_spell_cooldown}")