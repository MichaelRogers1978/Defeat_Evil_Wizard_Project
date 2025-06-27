from .character import Character

class Paladin(Character):
    def __init__(self,name,):
        super().__init__(name, health=160, attack_power=15)
        self.mana = 50
        self.max_mana = 50
        self.shield_active = False

    def holy_strike(self, opponent):
        if self.mana < 20:
            print(f"{self.name} doesn't have enough mana for a Holy Strike!")
            return
        damage = self.attack_power * 2
        opponent.health -= damage
        opponent.health = max(opponent.health, 0)
        self.mana -= 20
        print(f"{self.name} performs a Holy Strike on {opponent.name}, delivering {damage} damage!")
        if opponent.health <= 0:
            print(f"Congratulations, {opponent.name} has been defeated!")
        else:
            print(f"{opponent.name} has {opponent.health} health left.")
            
    def divine_shield(self):
        if self.mana < 15:
            print(f"{self.name} doesn't have enough mana for Divine Shield!")
            return
        self.shield_active = True
        self.mana -= 15
        print(f"{self.name} activates thier Divine Shield to block the next attack!")
        
    def has_shield(self):
        if self.shield_active:
            self.shield_active = False
            return True
        return False

    def divine_heal(self):
        if self.mana < 15:
            print(f"{self.name} doesn't have enough mana to heal!")
            return
        self.health += 30
        self.health = min(self.health, self.max_health)
        self.mana -= 15
        print(f"{self.name} uses Divine Heal and restores health to {self.health}/{self.max_health}.")

    def regenerate_mana(self, amount=5):
        self.mana = min(self.mana + amount, self.max_mana)

    def display_stats(self):
        super().display_stats()
        print(f"Mana: {self.mana}/{self.max_mana}")