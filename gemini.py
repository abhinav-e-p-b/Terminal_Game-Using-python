import time
import sys
import random

# --- Configuration & Utilities ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def slow_print(text, delay=0.03):
    """Simulates a retro terminal typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_choice(options):
    """Handles user input validation."""
    while True:
        print(f"\n{Colors.HEADER}Choose an action:{Colors.ENDC}")
        for key, value in options.items():
            print(f"[{key}] {value}")
        
        choice = input(f"\n{Colors.BLUE}>> {Colors.ENDC}").upper().strip()
        
        if choice in options:
            return choice
        else:
            print(f"{Colors.FAIL}Invalid command. Protocol mismatch.{Colors.ENDC}")

# --- Player Class ---
class Player:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100
        self.inventory = []
        self.has_keycard = False

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
        slow_print(f"{Colors.GREEN}Health restored. Current HP: {self.hp}{Colors.ENDC}")

    def take_damage(self, amount):
        self.hp -= amount
        slow_print(f"{Colors.FAIL}WARNING: Hull integrity compromised. -{amount} HP (Current: {self.hp}){Colors.ENDC}")
        if self.hp <= 0:
            game_over("Vital signs ceased. Mission Failed.")

    def add_item(self, item):
        self.inventory.append(item)
        slow_print(f"{Colors.GREEN}Acquired: {item}{Colors.ENDC}")

# --- Game Scenes ---

def game_over(reason):
    print("\n" + "="*30)
    slow_print(f"{Colors.FAIL}{reason}{Colors.ENDC}", 0.1)
    print("="*30)
    sys.exit()

def combat_encounter(player):
    """Mini-RPG combat loop"""
    enemy_hp = 50
    slow_print(f"\n{Colors.WARNING}!!! ALERT: VOID CRAWLER DETECTED !!!{Colors.ENDC}")
    
    while enemy_hp > 0 and player.hp > 0:
        print(f"\nPlayer HP: {player.hp} | Enemy HP: {enemy_hp}")
        action = get_choice({"A": "Attack with Plasma Wrench", "H": "Heal (+30 HP)", "R": "Run Away"})

        if action == "A":
            dmg = random.randint(10, 25)
            enemy_hp -= dmg
            slow_print(f"You struck the creature! It screeches. (-{dmg} HP)")
        elif action == "H":
            player.heal(30)
        elif action == "R":
            chance = random.randint(1, 10)
            if chance > 5:
                slow_print("You scrambled into the vent! You escaped, but took damage doing so.")
                player.take_damage(15)
                return "escaped"
            else:
                slow_print("Escape failed! The creature blocks the path.")

        # Enemy Turn
        if enemy_hp > 0:
            enemy_dmg = random.randint(5, 15)
            slow_print(f"The Void Crawler swipes at you!")
            player.take_damage(enemy_dmg)

    if player.hp > 0:
        slow_print(f"{Colors.GREEN}Target eliminated.{Colors.ENDC}")
        player.add_item("Alien Sludge (Trophy)")
        return "victory"

def scene_escape_pods(player):
    slow_print("\n--- SECTOR 9: ESCAPE PODS ---")
    slow_print("You reach the escape pods. One is active.")
    
    if "Navigation Chip" in player.inventory:
        slow_print("You insert the Navigation Chip. The pod coordinates lock onto Earth.")
        options = {"L": "Launch Pod"}
    else:
        slow_print(f"{Colors.WARNING}WARNING: Navigation Drive Missing.{Colors.ENDC}")
        slow_print("Launching now will result in random hyperspace trajectory.")
        options = {"L": "Launch Anyway (50% Survival Chance)", "R": "Return to search ship"}

    choice = get_choice(options)

    if choice == "L":
        if "Navigation Chip" in player.inventory:
            slow_print("Pod launched. Trajectory stable. You are going home.")
            slow_print(f"{Colors.GREEN}MISSION SUCCESS.{Colors.ENDC}")
        else:
            if random.random() > 0.5:
                slow_print("By some miracle, you found a trade route. You survived.")
                slow_print(f"{Colors.GREEN}MISSION SUCCESS (Barely).{Colors.ENDC}")
            else:
                game_over("The pod drifts into a black hole. No signal remains.")
    elif choice == "R":
        scene_hub(player)

def scene_bridge(player):
    slow_print("\n--- SECTOR 1: THE BRIDGE ---")
    slow_print("The Captain's chair is empty. A console blinks amber.")
    
    if player.has_keycard:
        slow_print("You use the keycard to unlock the secure safe.")
        if "Navigation Chip" not in player.inventory:
            player.add_item("Navigation Chip")
        else:
            slow_print("Empty. You already looted this.")
    else:
        slow_print("There is a secure safe here. It requires a BLUE KEYCARD.")

    choice = get_choice({"B": "Back to Hub"})
    if choice == "B":
        scene_hub(player)

def scene_armory(player):
    slow_print("\n--- SECTOR 4: ARMORY ---")
    slow_print("It's dark. Something is moving in the shadows.")
    
    result = combat_encounter(player)
    
    if result == "victory":
        slow_print("Searching the room, you find a corpse clutching a pass.")
        player.has_keycard = True
        slow_print(f"{Colors.GREEN}Acquired: BLUE KEYCARD{Colors.ENDC}")
    
    choice = get_choice({"B": "Back to Hub"})
    if choice == "B":
        scene_hub(player)

def scene_hub(player):
    slow_print("\n--- CENTRAL HUB ---")
    slow_print("You stand in the flickering light of the central corridor.")
    slow_print("To the LEFT is the Bridge (Control).")
    slow_print("To the RIGHT is the Armory (Danger detected).")
    slow_print("FORWARD leads to Escape Pods.")

    choice = get_choice({
        "L": "Go to Bridge",
        "R": "Go to Armory",
        "F": "Go to Escape Pods",
        "I": "Check Inventory/Status"
    })

    if choice == "L":
        scene_bridge(player)
    elif choice == "R":
        scene_armory(player)
    elif choice == "F":
        scene_escape_pods(player)
    elif choice == "I":
        print(f"\nHP: {player.hp}/{player.max_hp}")
        print(f"Inventory: {player.inventory}")
        scene_hub(player)

def intro():
    slow_print(f"{Colors.BOLD}INITIALIZING PROTOCOL: ABYSS...{Colors.ENDC}")
    time.sleep(1)
    slow_print("You wake up. The air is cold.")
    slow_print("The siren is blaring: 'CRITICAL FAILURE. EVACUATE.'")
    
    player = Player()
    scene_hub(player)

# --- Main Entry Point ---
if __name__ == "__main__":
    try:
        intro()
    except KeyboardInterrupt:
        print("\n\nGame terminated by user.")