import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health

    def attack(self, opponent):
        if hasattr(opponent, "should_evade") and callable(opponent.should_evade):
            if opponent.should_evade():
                print(f"{opponent.name} evaded the attack!")
                return
        if hasattr(opponent, "teleport") and callable(opponent.teleport):
            if opponent.teleport():
                print(f"{self.name}'s attack missed because {opponent.name} has teleported!")
                return
        if hasattr(opponent, "has_sheild") and opponent.has_sheild():
            print(f"{opponent.name}'s shield has blocked the attack!")
            return
        min_damage = max(1, self.attack_power - 5)
        max_damage = self.attack_power + 5
        damage = random.randint(min_damage, max_damage)
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        print(f"{self.name} attacks {opponent.name} for {damage} damage.")
        if opponent.health <= 0:
            print(f"Congratulations,{opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} has {opponent.health} health left.")

    def heal(self, amount):
        if self.health == self.max_health:
            print(f"{self.name} is at full health!")
        else:
            previous_health = self.health
            self.health += amount
            if self.health > self.max_health:
                self.health = self.max_health
            healed_amount = self.health - previous_health
            print(f"{self.name} heals for {healed_amount} points and now has {self.health} health.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
