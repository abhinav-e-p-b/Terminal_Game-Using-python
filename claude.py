import random
import time
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.energy = 50
        self.inventory = []
        self.crew_members = []
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            
    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

def slow_print(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_stats(player):
    """Display player stats"""
    print(f"\n{'='*50}")
    print(f"Captain {player.name} | HP: {player.hp}/{player.max_hp} | Energy: {player.energy}")
    if player.inventory:
        print(f"Inventory: {', '.join(player.inventory)}")
    if player.crew_members:
        print(f"Crew: {', '.join(player.crew_members)}")
    print(f"{'='*50}\n")

def get_choice(num_options):
    """Get valid player choice"""
    while True:
        try:
            choice = int(input("\nYour choice: "))
            if 1 <= choice <= num_options:
                return choice
            print(f"Please enter a number between 1 and {num_options}")
        except ValueError:
            print("Please enter a valid number")

def intro():
    """Game introduction"""
    slow_print("\n" + "="*50)
    slow_print("STARSHIP ODYSSEY: The Lost Sector")
    slow_print("="*50 + "\n")
    time.sleep(0.5)
    
    slow_print("Year 2347. Humanity has reached the stars...")
    slow_print("Your ship, the USS Wanderer, has detected a mysterious signal")
    slow_print("from Sector X-9, a region marked as 'Lost' on all star charts.\n")
    time.sleep(0.5)
    
    name = input("Enter your captain's name: ")
    return Player(name)

def distress_signal(player):
    """First choice scene"""
    print_stats(player)
    slow_print("Your sensors pick up a distress signal from a nearby ship.")
    slow_print("Scans reveal it's damaged but might contain survivors... or danger.")
    
    print("\nWhat do you do?")
    print("1. Dock with the ship and investigate")
    print("2. Send a probe to scan first")
    print("3. Ignore it and continue to the signal source")
    
    choice = get_choice(3)
    
    if choice == 1:
        return investigate_ship(player)
    elif choice == 2:
        return probe_scan(player)
    else:
        return ignore_ship(player)

def investigate_ship(player):
    """Direct investigation path"""
    slow_print("\nYou dock with the damaged vessel. The airlock hisses open...")
    slow_print("Inside, emergency lights flicker. You hear movement ahead.")
    time.sleep(0.5)
    
    print("\nWhat do you do?")
    print("1. Call out to identify yourself")
    print("2. Proceed cautiously with weapon drawn")
    print("3. Check the ship's computer first")
    
    choice = get_choice(3)
    
    if choice == 1:
        slow_print("\nA figure emerges - it's Dr. Sarah Chen, a xenobiologist!")
        slow_print("'Thank the stars! Our ship was attacked by unknown hostiles.'")
        player.crew_members.append("Dr. Chen")
        player.energy += 10
        return ancient_artifact(player)
    elif choice == 2:
        slow_print("\nYou round a corner and face a malfunctioning security droid!")
        return combat_droid(player)
    else:
        slow_print("\nYou access the computer. Logs show they found something...")
        slow_print("An artifact of unknown origin. It's still aboard!")
        player.inventory.append("Ancient Map")
        return ancient_artifact(player)

def probe_scan(player):
    """Probe scanning path"""
    slow_print("\nYou launch a probe. Scans reveal organic life signs...")
    slow_print("And something else - an energy signature unlike anything known.")
    player.energy -= 5
    
    print("\nWhat do you do?")
    print("1. Dock with the ship now that you know more")
    print("2. Call for backup from the nearest station")
    print("3. Proceed directly to the main signal source")
    
    choice = get_choice(3)
    
    if choice == 1:
        return investigate_ship(player)
    elif choice == 2:
        slow_print("\nBackup is 6 hours away. You wait safely...")
        slow_print("But the mysterious signal suddenly vanishes!")
        return backup_ending(player)
    else:
        return signal_source(player)

def ignore_ship(player):
    """Ignoring the distress signal"""
    slow_print("\nYou continue toward the main signal. Your crew looks uneasy.")
    slow_print("Suddenly, your ship shudders - you're caught in a tractor beam!")
    player.hp -= 20
    
    slow_print("\nAn alien vessel appears. They're scanning you...")
    return alien_encounter(player)

def combat_droid(player):
    """Combat encounter"""
    droid_hp = 50
    slow_print("\nCOMBAT INITIATED!")
    slow_print("The droid's weapons charge up!\n")
    
    while droid_hp > 0 and player.hp > 0:
        print(f"Droid HP: {droid_hp} | Your HP: {player.hp}")
        print("\n1. Attack (20-30 damage)")
        print("2. Defend (Reduce incoming damage)")
        print("3. Use med-kit (Heal 25 HP)")
        
        choice = get_choice(3)
        
        if choice == 1:
            damage = random.randint(20, 30)
            droid_hp -= damage
            slow_print(f"\nYou attack for {damage} damage!")
        elif choice == 2:
            slow_print("\nYou take a defensive stance!")
            incoming = random.randint(5, 10)
            player.take_damage(incoming)
            slow_print(f"Droid attacks for {incoming} damage (reduced)!")
            continue
        else:
            player.heal(25)
            slow_print("\nYou use a med-kit and heal 25 HP!")
        
        if droid_hp > 0:
            incoming = random.randint(15, 25)
            player.take_damage(incoming)
            slow_print(f"Droid attacks for {incoming} damage!")
        
        time.sleep(1)
    
    if player.hp > 0:
        slow_print("\n✓ Droid defeated!")
        slow_print("You find a power cell in the wreckage.")
        player.inventory.append("Power Cell")
        return ancient_artifact(player)
    else:
        return game_over(player, "The droid overwhelmed you...")

def ancient_artifact(player):
    """Artifact discovery scene"""
    print_stats(player)
    slow_print("You discover the ship's cargo bay. Inside...")
    slow_print("A crystalline artifact pulses with otherworldly energy!")
    
    print("\nWhat do you do?")
    print("1. Take the artifact")
    print("2. Leave it and report your findings")
    print("3. Study it first with your scanner")
    
    choice = get_choice(3)
    
    if choice == 1:
        slow_print("\nAs you touch it, visions flood your mind!")
        slow_print("You see the location of an ancient alien gateway...")
        player.inventory.append("Crystalline Artifact")
        return gateway_choice(player)
    elif choice == 2:
        slow_print("\nYou report to command. They send a science team.")
        return safe_ending(player)
    else:
        slow_print("\nScans reveal it's a key of some kind...")
        slow_print("The main signal source - it's a lock mechanism!")
        player.inventory.append("Crystalline Key")
        return signal_source(player)

def alien_encounter(player):
    """Alien contact scene"""
    print_stats(player)
    slow_print("A voice speaks in perfect English:")
    slow_print("'We are the Keepers. You have found what was lost.'")
    
    print("\nHow do you respond?")
    print("1. 'We come in peace' (Diplomatic)")
    print("2. 'Release us immediately!' (Aggressive)")
    print("3. 'What is this place?' (Curious)")
    
    choice = get_choice(3)
    
    if choice == 1:
        slow_print("\n'Your peaceful nature is noted. We will guide you.'")
        player.crew_members.append("Keeper Guide")
        return gateway_choice(player)
    elif choice == 2:
        slow_print("\n'Hostility detected. Initiating defensive protocols.'")
        player.hp -= 30
        slow_print("Your ship takes damage before you can apologize!")
        return alien_encounter(player)
    else:
        slow_print("\n'This is the Gateway to the Lost Worlds. You may enter.'")
        return gateway_choice(player)

def signal_source(player):
    """Main signal source"""
    print_stats(player)
    slow_print("You arrive at the signal source - a massive space station!")
    slow_print("It's older than human civilization itself.")
    
    if "Crystalline Key" in player.inventory or "Crystalline Artifact" in player.inventory:
        slow_print("\nYour artifact resonates with the station!")
        return gateway_choice(player)
    else:
        slow_print("\nThe station's doors remain sealed. You need a key...")
        return search_ending(player)

def gateway_choice(player):
    """Final major choice"""
    print_stats(player)
    slow_print("The gateway activates! It can transport you to:")
    slow_print("Ancient worlds, untouched by time...")
    
    print("\nWhat is your decision?")
    print("1. Enter the gateway (The Unknown)")
    print("2. Take readings and return home (Scientific Caution)")
    print("3. Invite humanity to explore together (Diplomatic)")
    
    choice = get_choice(3)
    
    if choice == 1:
        return explorer_ending(player)
    elif choice == 2:
        return scientist_ending(player)
    else:
        return diplomat_ending(player)

def explorer_ending(player):
    """Explorer ending"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("ENDING: THE EXPLORER")
    slow_print("="*50)
    slow_print("\nYou step through the gateway. Light surrounds you...")
    slow_print("On the other side, a new galaxy awaits.")
    slow_print("Your name will be remembered as the first to traverse the Lost Sector.")
    slow_print(f"\nCaptain {player.name}, your journey has just begun...")
    return True

def scientist_ending(player):
    """Scientific ending"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("ENDING: THE SCIENTIST")
    slow_print("="*50)
    slow_print("\nYou collect invaluable data and return home.")
    slow_print("Your discoveries advance human understanding by centuries.")
    slow_print("The gateway remains, waiting for humanity to be ready.")
    slow_print(f"\nCaptain {player.name}, you have enlightened humanity!")
    return True

def diplomat_ending(player):
    """Diplomatic ending"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("ENDING: THE DIPLOMAT")
    slow_print("="*50)
    slow_print("\nYou call for humanity to witness this moment together.")
    slow_print("The gateway becomes a symbol of unity and exploration.")
    slow_print("A new era of cooperation begins among the stars.")
    slow_print(f"\nCaptain {player.name}, you have united humanity!")
    return True

def safe_ending(player):
    """Safe/cautious ending"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("ENDING: THE CAUTIOUS COMMANDER")
    slow_print("="*50)
    slow_print("\nYou play it safe. The artifact is studied by experts.")
    slow_print("Your career is stable, but you'll always wonder...")
    slow_print("What mysteries lay beyond that signal?")
    slow_print(f"\nCaptain {player.name}, you survived, but at what cost?")
    return True

def backup_ending(player):
    """Backup ending"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("ENDING: THE ONE THAT GOT AWAY")
    slow_print("="*50)
    slow_print("\nThe signal vanishes before you can investigate.")
    slow_print("The mystery of Sector X-9 remains unsolved.")
    slow_print("Perhaps some secrets are meant to stay hidden...")
    slow_print(f"\nCaptain {player.name}, the stars keep their secrets.")
    return True

def search_ending(player):
    """Search ending"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("ENDING: THE ENDLESS SEARCH")
    slow_print("="*50)
    slow_print("\nWithout the key, you cannot enter.")
    slow_print("You dedicate your life to finding another way in...")
    slow_print("The gateway taunts you with possibilities.")
    slow_print(f"\nCaptain {player.name}, your quest continues...")
    return True

def game_over(player, reason):
    """Game over"""
    print_stats(player)
    slow_print("\n" + "="*50)
    slow_print("GAME OVER")
    slow_print("="*50)
    slow_print(f"\n{reason}")
    slow_print(f"Captain {player.name} fell in the line of duty.")
    slow_print("The stars remember the brave...")
    return False

def main():
    """Main game loop"""
    player = intro()
    
    # Game progression
    result = distress_signal(player)
    
    if result:
        slow_print("\n✓ Mission Complete!")
        slow_print("Thank you for playing Starship Odyssey!")
    else:
        slow_print("\nWould you like to try again? (y/n)")
        retry = input().lower()
        if retry == 'y':
            main()

if __name__ == "__main__":
    main()