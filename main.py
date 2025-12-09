import tkinter as tk
from player import Player
from enemy import Enemy
import random

def main():
    fight_count = 0  # Initialize fight counter

    def update_status():
        status_label.config(text=f"Player Health: {player.health} | Enemy Health: {enemy.health}")
        money_label.config(text=f"Gold nugets: {player.money}")

    def attack():
        if player.is_alive() and enemy.is_alive():
            player.attack(enemy)
            if enemy.is_alive():
                enemy.attack(player)
            else:
                player.money += 15  # Reward 15 gold for defeating the enemy
            update_status()
            check_game_over()

    def heal():
        heal_cost = 5
        if player.money >= heal_cost:
            player.money -= heal_cost
            player.heal()
            if enemy.is_alive():
                enemy.attack(player)
            update_status()
            check_game_over()
        else:
            status_label.config(text="Not enough gold nugets to heal!")
            update_status()

    def buy_damage_upgrade():
        upgrade_cost = 15  # Change cost to 15
        if player.money >= upgrade_cost:
            player.money -= upgrade_cost
            player.attack_power += 5  # Increase attack power
            status_label.config(text="Damage upgraded!")
        else:
            status_label.config(text="Not enough gold nugets!")
        update_status()

    def next_fight():
        nonlocal enemy, fight_count
        fight_count += 1
        if fight_count > 20:  # Check if the player has reached 20 fights
            status_label.config(text="Congratulations! you found the ruby trail!")
            attack_button.config(state=tk.DISABLED)
            heal_button.config(state=tk.DISABLED)
            store_button.config(state=tk.DISABLED)
            next_fight_button.config(state=tk.DISABLED)
            return

        enemy = Enemy(f"monster {random.randint(1, 100)}", 50, 10)  # Create a new enemy
        status_label.config(text=f"A new enemy appears! Fight {fight_count}/20")
        attack_button.config(state=tk.NORMAL)
        heal_button.config(state=tk.NORMAL)
        store_button.config(state=tk.NORMAL)
        next_fight_button.config(state=tk.DISABLED)
        update_status()

    def check_game_over():
        if not player.is_alive():
            status_label.config(text="Game Over")
            attack_button.config(state=tk.DISABLED)
            heal_button.config(state=tk.DISABLED)
            store_button.config(state=tk.DISABLED)
            next_fight_button.config(state=tk.DISABLED)
        elif not enemy.is_alive():
            status_label.config(text="Victory! Click 'Next' to continue.")
            attack_button.config(state=tk.DISABLED)
            heal_button.config(state=tk.DISABLED)
            store_button.config(state=tk.DISABLED)
            next_fight_button.config(state=tk.NORMAL)

    # Initialize game objects
    player = Player("player", 100, 20, 0)  # Start with 0 money
    enemy = Enemy("monster", 50, 10)

    # Create the GUI
    root = tk.Tk()
    root.title("trail of the ruby 0.0.1 indev")

    status_label = tk.Label(root, text="can you find the ruby trail", font=("Arial", 14))
    status_label.pack(pady=10)

    money_label = tk.Label(root, text="Gold nugets: 0", font=("Arial", 12))
    money_label.pack(pady=5)

    attack_button = tk.Button(root, text="Attack", command=attack, font=("Arial", 12))
    attack_button.pack(pady=5)

    heal_button = tk.Button(root, text="Heal", command=heal, font=("Arial", 12))
    heal_button.pack(pady=5)

    store_button = tk.Button(root, text="Buy Damage Upgrade (15 Gold)", command=buy_damage_upgrade, font=("Arial", 12))
    store_button.pack(pady=5)

    next_fight_button = tk.Button(root, text="Next", command=next_fight, font=("Arial", 12), state=tk.DISABLED)
    next_fight_button.pack(pady=5)

    update_status()
    root.mainloop()

if __name__ == "__main__":
    main()
