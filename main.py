from game.selection import create_character
from game.match import best_of_three_battle
from game.rewards import reward_player
from characters.evil_wizard import EvilWizard

def main():
    print("=== Welcome to the 'Defeat the Evil Wizard game'! ===")
    while True:
        player = create_character()
        print(f"\nYou chose: {player.name}\n")
        print("Prepare for battle against the Evil Wizard....Best of three wins!\n")
        wizard = EvilWizard("The Dark Wizard", 150, 15)
        player_wins = best_of_three_battle(player, wizard)
        if player_wins >= 1:
            print("\nCongratulations! You earned a reward for your victory.")
        else:
            print("\nYou lost the battle. No rewards earned this time.")
        play_again = input("\nWould you like to play another game? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break
        print("\nRestarting the game....\n")

if __name__ == "__main__":
    main()
