from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.paladin import Paladin

def reward_player(player):
    print("\n--- Reward Time! Choose one of the following upgrades: ---")
    print("1. Restore 30 health (up to max) once during next round.")
    print("2. Gain Armor (reduce damage by 20%) during next round.")
    print("3. Unlock a unique ability (character-specific).")
    choice = input("Enter the number of your reward choice: ")
    if choice == "1":
        player.next_round_heal_available = True
        print(f"{player.name} can choose to heal 30 HP once during the next round.")
    elif choice == "2":
        player.armor_active = True
        print(f"{player.name} will take 20% less damage during the next round.")
    elif choice == "3":
        if isinstance(player, Warrior):
            player.warrior_heart_ready = True
            print(f"{player.name} unlocked the Warrior's Heart - health revives to 50 once during this round when health reaches 5.")
        elif isinstance(player, Mage):
            player.freeze_spell_ready = True
            print(f"{player.name} unlocked Freeze - temporarily stuns the enemy!")
        elif isinstance(player, Archer):
            player.poison_tip_ready = True
            print(f"{player.name} unlocked Poison Tip - adds poison damage over time!")
        elif isinstance(player, Paladin):
            player.resurrect_ready = True
            print(f"{player.name} unlocked Resurrect - Can revive once if defeated!")
        else:
            print("No special ability for this class.")
    else:
        print("Invalid choice. No reward applied.")