from .character import Character

class Archer(Character):
    def __init__(self,name,):
        super().__init__(name, health=120, attack_power=20)
        self.arrows = 10

    def range_attack(self, opponent):
        if self.arrows <= 0:
            print(f"{self.name} doesn't have any arrows left!")
            return
        damage = self.attack_power + 10
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        self.arrows -= 1
        print(f"{self.name} fires an arrow at {opponent.name} and delivers {damage} damage!")
        if opponent.health <= 0:
            print(f"Congratulations, {opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} has {opponent.health} health left.")
            
    def quick_shot(self, opponent):
        if self.arrows < 2:
            print(f"{self.name} doesn't have enough arrowrs for a Quick Shot.")
            return
        total_damage = (self.attack_power + 5) * 2
        opponent.health -= total_damage
        opponent.health = max(opponent.health, 0)
        self.arrows -= 2
        print(f"{self.name} uses Quick Shot for {total_damage} total damage!")
        
    def evade(self):
        self.evade_active = True
        print(f"{self.name} prepares to evade the next incoming attack!")
        
    def should_evade(self):
        if self.evade_active:
            self.evade_active = False
            return True

    def replenish_arrows(self, amount=5):
        self.arrows = min(self.arrows + amount, 10)
        print(f"The Archer,{self.name}, replenished {amount} arrows! Now {self.name} has {self.arrows} arrows.")

    def display_stats(self):
        super().display_stats()
        print(f"Arrows: {self.arrows}")