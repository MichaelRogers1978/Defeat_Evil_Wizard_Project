from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.paladin import Paladin

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice:")
    name = input("Enter your character's name:")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. You are now a Warrior.")
        return Warrior(name)

