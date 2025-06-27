from game.battle import battle
from game.rewards import reward_player

def conclude_round_and_show_score(player, wizard, player_wins, wizard_wins, round_number):
    print(f"--- End of Round {round_number} ---")
    print(f"Current Score: {player.name} {player_wins} - {wizard.name} {wizard_wins}")
    print(f"\n Score: {player.name} {player_wins} - {wizard.name} {wizard_wins}")
    
def show_final_result(player, wizard, player_wins, wizard_wins):
    print(f"\n FINAL RESULT: ")
    if player_wins > wizard_wins:
        print(f" {player.name} wins the best of 3 rounds in this battle!")
    else:
        print(f" {wizard.name} wins the best of 3 rounds in this battle!")

def best_of_three_battle(player, wizard):
    player_wins = 0
    wizard_wins = 0
    round_number = 1
    
    for attr in [
        "next_round_heal_available", "armor_active",
        "warrior_heart_ready", "freeze_spell_ready",
        "poison_tip_ready", "resurrect_ready"]:
        
        if hasattr(player, attr):
            delattr(player, attr)

    while player_wins < 2 and wizard_wins < 2:
        print(f"\n Round {round_number}")

        player.health = player.max_health
        if hasattr(player, "mana"):
            player.mana = player.max_mana
        if hasattr(player, "arrows"):
            player.arrows = 10
        if hasattr(player, "dark_spell_cooldown"):
            player.dark_spell_cooldown = 0

        wizard.health = wizard.max_health
        if hasattr(wizard, "mana"):
            wizard.mana = wizard.max_mana
        if hasattr(wizard, "dark_spell_cooldown"):
            wizard.dark_spell_cooldown = 0

        allow_rewards = player_wins > 0
        winner = battle(player, wizard, allow_rewards=allow_rewards)

        if winner == "player":
            player_wins += 1
            print(f"Good job, you won round number {round_number}!")
            if player_wins < 2 and wizard_wins < 2:
                reward_player(player)
        else:
            wizard_wins += 1
            print(f" {wizard.name} won round number {round_number}.")

        conclude_round_and_show_score(player, wizard, player_wins, wizard_wins, round_number)
        round_number += 1

    show_final_result(player, wizard, player_wins, wizard_wins)
    return player_wins
