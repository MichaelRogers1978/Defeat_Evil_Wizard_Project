from characters.warrior import Warrior
from characters.mage import Mage
from characters.archer import Archer
from characters.paladin import Paladin
from characters.evil_wizard import EvilWizard


def conclude_round_and_show_score(player, wizard, player_wins, wizard_wins, round_number):
    print(f"--- End of Round {round_number} ---")
    print(f"Current Score: {player.name} {player_wins} - {wizard.name} {wizard_wins}\n")
    print(f"\n Score: {player.name} {player_wins} - {wizard.name} {wizard_wins}")

def show_final_result(player, wizard, player_wins, wizard_wins):
    print(f"\n FINAL RESULT:")
    if player_wins > wizard_wins:
        print(f" {player.name} wins the best of 3 rounds in this battle!")
    else:
        print(f" {wizard.name} wins the best of 3 rounds in this battle!")

def battle(player, wizard, allow_rewards=False):
    turn = 0
    heal_used_this_round = False
    poison_turns = 0
    freeze_turns = 0
    wizard_used_dark_spell = False

    while player.health > 0 and wizard.health > 0:
        print("\n--- Current Stats ---")
        player.display_stats()
        wizard.display_stats()
        print("------------------\n")

        if turn % 2 == 0:
            print("Your turn! Choose your action:")
            actions = ["Attack"]
            if hasattr(player, "heal"):
                actions.append("Heal")
            if isinstance(player, Warrior):
                actions.append("Power Attack")
                actions.append("Battle Cry")
            if isinstance(player, Mage):
                actions.append("Fireball")
                actions.append("Mana Shield")
            if isinstance(player, Archer):
                actions.append("Range Attack")
                actions.append("Replenish Arrows")
            if isinstance(player, Paladin):
                actions.append("Holy Strike")
                actions.append("Divine Heal")
            if allow_rewards and getattr(player, "next_round_heal_available", False) and not heal_used_this_round:
                actions.append("Use Reward Heal")

            for i, action in enumerate(actions, 1):
                print(f"{i}. {action}")

            choice = input("Enter the number of your action: ")
            try:
                choice = int(choice)
                action = actions[choice - 1]
            except (ValueError, IndexError):
                print("Invalid choice, defaulting to Attack.")
                action = "Attack"

            if action == "Attack":
                if isinstance(player, Warrior):
                    damage = player.boosted_attack()
                    wizard.health -= damage
                    wizard.health = max(wizard.health, 0)
                    print(f"{player.name} attacks The Dark Wizard with boosted damage of {damage}!")
                else:
                    player.attack(wizard)
            elif action == "Battle Cry":
                player.battle_cry()
            elif action == "Heal":
                player.heal(20)
            elif action == "Power Attack":
                player.power_attack(wizard)
            elif action == "Fireball":
                player.fireball(wizard)
            elif action == "Range Attack":
                player.range_attack(wizard)
            elif action == "Replenish Arrows":
                player.replenish_arrows()
            elif action == "Holy Strike":
                player.holy_strike(wizard)
            elif action == "Mana Shield":
                player.mana_shield()
            elif action == "Divine Heal":
                player.divine_heal()
            elif action == "Use Reward Heal":
                player.health = min(player.health + 30, player.max_health)
                print(f"{player.name} uses their reward to heal 30 HP! Now at {player.health}/{player.max_health}.")
                player.next_round_heal_available = False
                heal_used_this_round = True
        else:
            print(f"{wizard.name}'s turn!")
            if allow_rewards and getattr(player, "freeze_spell_ready", False) and freeze_turns < 1:
                print(f"{player.name}'s Freeze reward stuns the wizard for 1 turn!")
                freeze_turns += 1
            else:
                if allow_rewards and getattr(player, "poison_tip_ready", False) and poison_turns < 3:
                    poison_damage = 8
                    wizard.health -= poison_damage
                    wizard.health = max(wizard.health, 0)
                    print(f"Poison tip deals {poison_damage} damage to The Dark Wizard!")
                    poison_turns += 1

                if not wizard_used_dark_spell and wizard.dark_spell_cooldown <= 1 and wizard.mana >= 30:
                    wizard.dark_spell(player)
                    wizard_used_dark_spell = True
                elif allow_rewards and getattr(player, "armor_active", False):
                    orig_health = player.health
                    wizard.attack(player)
                    reduced = int((orig_health - player.health) * 0.2)
                    player.health += reduced
                    print(f"Armor reduces damage by {reduced}!")
                else:
                    wizard.attack(player)

                if allow_rewards and getattr(player, "next_round_heal_available", False) and not heal_used_this_round and player.health > 0:
                    use_heal = input("Do you want to use your reward heal now? (y/n): ").strip().lower()
                    if use_heal == "y":
                        player.health = min(player.health + 30, player.max_health)
                        print(f"{player.name} uses their reward to heal 30 HP! Now at {player.health}/{player.max_health}.")
                        player.next_round_heal_available = False
                        heal_used_this_round = True

                if allow_rewards and getattr(player, "warrior_heart_ready", False) and player.health <= 5:
                    player.health = 50
                    player.warrior_heart_ready = False
                    print(f"{player.name}'s Warrior's Heart revives them to 50 health!")

                if allow_rewards and getattr(player, "resurrect_ready", False) and player.health <= 0:
                    player.health = player.max_health // 2
                    player.resurrect_ready = False
                    print(f"{player.name} is resurrected with {player.health} health!")

        if hasattr(player, "reduce_cooldowns"):
            player.reduce_cooldowns()
        if hasattr(wizard, "reduce_cooldowns"):
            wizard.reduce_cooldowns()

        turn += 1

    return "player" if player.health > 0 else "wizard"


