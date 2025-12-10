import tkinter as tk
from tkinter import ttk, messagebox
import random
import time

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

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Starship Odyssey: The Lost Sector")
        self.root.geometry("900x700")
        self.root.configure(bg="#0a0e27")
        
        self.player = None
        self.typing_speed = 30  # milliseconds per character
        self.current_text = ""
        self.text_index = 0
        
        self.setup_ui()
        self.show_intro()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg="#0a0e27")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        self.title_label = tk.Label(
            main_frame,
            text="STARSHIP ODYSSEY",
            font=("Courier New", 24, "bold"),
            bg="#0a0e27",
            fg="#00ff88"
        )
        self.title_label.pack(pady=(0, 10))
        
        # Stats frame
        self.stats_frame = tk.Frame(main_frame, bg="#1a1e37", relief=tk.RIDGE, bd=2)
        self.stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.stats_label = tk.Label(
            self.stats_frame,
            text="",
            font=("Courier New", 10),
            bg="#1a1e37",
            fg="#00ff88",
            justify=tk.LEFT,
            padx=10,
            pady=5
        )
        self.stats_label.pack()
        
        # Story text area with scrollbar
        text_frame = tk.Frame(main_frame, bg="#0a0e27")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.story_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=("Courier New", 11),
            bg="#0f1419",
            fg="#00ff88",
            insertbackground="#00ff88",
            relief=tk.FLAT,
            padx=15,
            pady=15,
            yscrollcommand=scrollbar.set,
            state=tk.DISABLED
        )
        self.story_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.story_text.yview)
        
        # Choices frame
        self.choices_frame = tk.Frame(main_frame, bg="#0a0e27")
        self.choices_frame.pack(fill=tk.X, pady=(10, 0))
        
    def update_stats(self):
        if self.player:
            stats = f"Captain {self.player.name} | HP: {self.player.hp}/{self.player.max_hp} | Energy: {self.player.energy}"
            if self.player.inventory:
                stats += f"\nInventory: {', '.join(self.player.inventory)}"
            if self.player.crew_members:
                stats += f"\nCrew: {', '.join(self.player.crew_members)}"
            self.stats_label.config(text=stats)
        
    def add_text(self, text, delay=True):
        """Add text to story area with optional typewriter effect"""
        self.story_text.config(state=tk.NORMAL)
        
        if delay:
            self.current_text = text + "\n\n"
            self.text_index = 0
            self.type_character()
        else:
            self.story_text.insert(tk.END, text + "\n\n")
            self.story_text.see(tk.END)
            self.story_text.config(state=tk.DISABLED)
        
    def type_character(self):
        """Typewriter effect for text"""
        if self.text_index < len(self.current_text):
            self.story_text.insert(tk.END, self.current_text[self.text_index])
            self.story_text.see(tk.END)
            self.text_index += 1
            self.root.after(self.typing_speed, self.type_character)
        else:
            self.story_text.config(state=tk.DISABLED)
    
    def clear_choices(self):
        """Clear all choice buttons"""
        for widget in self.choices_frame.winfo_children():
            widget.destroy()
    
    def add_choice(self, text, command):
        """Add a choice button"""
        btn = tk.Button(
            self.choices_frame,
            text=text,
            font=("Courier New", 10, "bold"),
            bg="#1a4d2e",
            fg="#00ff88",
            activebackground="#2d6a4f",
            activeforeground="#00ff88",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10,
            command=command,
            cursor="hand2"
        )
        btn.pack(fill=tk.X, pady=5)
        
    def show_intro(self):
        """Show game introduction"""
        self.add_text("=" * 50)
        self.add_text("STARSHIP ODYSSEY: The Lost Sector")
        self.add_text("=" * 50)
        self.add_text("\nYear 2347. Humanity has reached the stars...")
        self.add_text("Your ship, the USS Wanderer, has detected a mysterious signal")
        self.add_text("from Sector X-9, a region marked as 'Lost' on all star charts.\n")
        
        self.root.after(3000, self.ask_name)
    
    def ask_name(self):
        """Ask for player name"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Captain Name")
        dialog.geometry("400x150")
        dialog.configure(bg="#0a0e27")
        dialog.transient(self.root)
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="Enter your captain's name:",
            font=("Courier New", 12),
            bg="#0a0e27",
            fg="#00ff88"
        ).pack(pady=20)
        
        name_entry = tk.Entry(
            dialog,
            font=("Courier New", 12),
            bg="#1a1e37",
            fg="#00ff88",
            insertbackground="#00ff88"
        )
        name_entry.pack(pady=10, padx=20, fill=tk.X)
        name_entry.focus()
        
        def submit():
            name = name_entry.get().strip()
            if name:
                self.player = Player(name)
                self.update_stats()
                dialog.destroy()
                self.distress_signal()
            else:
                messagebox.showwarning("Invalid Name", "Please enter a valid name!")
        
        name_entry.bind('<Return>', lambda e: submit())
        
        tk.Button(
            dialog,
            text="Begin Adventure",
            font=("Courier New", 11, "bold"),
            bg="#1a4d2e",
            fg="#00ff88",
            command=submit
        ).pack(pady=10)
    
    def distress_signal(self):
        """First choice scene"""
        self.clear_choices()
        self.add_text("Your sensors pick up a distress signal from a nearby ship.")
        self.add_text("Scans reveal it's damaged but might contain survivors... or danger.")
        self.add_text("\nWhat do you do?")
        
        self.add_choice("1. Dock with the ship and investigate", self.investigate_ship)
        self.add_choice("2. Send a probe to scan first", self.probe_scan)
        self.add_choice("3. Ignore it and continue to the signal source", self.ignore_ship)
    
    def investigate_ship(self):
        """Direct investigation path"""
        self.clear_choices()
        self.add_text("You dock with the damaged vessel. The airlock hisses open...")
        self.add_text("Inside, emergency lights flicker. You hear movement ahead.")
        
        self.root.after(2000, self.investigate_choice)
    
    def investigate_choice(self):
        self.add_text("\nWhat do you do?")
        self.add_choice("1. Call out to identify yourself", self.call_out)
        self.add_choice("2. Proceed cautiously with weapon drawn", self.combat_droid)
        self.add_choice("3. Check the ship's computer first", self.check_computer)
    
    def call_out(self):
        self.clear_choices()
        self.add_text("A figure emerges - it's Dr. Sarah Chen, a xenobiologist!")
        self.add_text("'Thank the stars! Our ship was attacked by unknown hostiles.'")
        self.player.crew_members.append("Dr. Chen")
        self.player.energy += 10
        self.update_stats()
        self.root.after(3000, self.ancient_artifact)
    
    def check_computer(self):
        self.clear_choices()
        self.add_text("You access the computer. Logs show they found something...")
        self.add_text("An artifact of unknown origin. It's still aboard!")
        self.player.inventory.append("Ancient Map")
        self.update_stats()
        self.root.after(3000, self.ancient_artifact)
    
    def combat_droid(self):
        """Combat encounter"""
        self.clear_choices()
        self.droid_hp = 50
        self.add_text("You round a corner and face a malfunctioning security droid!")
        self.add_text("COMBAT INITIATED!")
        self.root.after(2000, self.combat_round)
    
    def combat_round(self):
        """Single combat round"""
        if self.droid_hp <= 0:
            self.add_text("\n✓ Droid defeated!")
            self.add_text("You find a power cell in the wreckage.")
            self.player.inventory.append("Power Cell")
            self.update_stats()
            self.root.after(3000, self.ancient_artifact)
            return
        
        if self.player.hp <= 0:
            self.game_over("The droid overwhelmed you...")
            return
        
        self.clear_choices()
        self.add_text(f"\nDroid HP: {self.droid_hp} | Your HP: {self.player.hp}")
        
        self.add_choice("⚔️ Attack (20-30 damage)", lambda: self.combat_action("attack"))
        self.add_choice("🛡️ Defend (Reduce incoming damage)", lambda: self.combat_action("defend"))
        self.add_choice("💊 Use med-kit (Heal 25 HP)", lambda: self.combat_action("heal"))
    
    def combat_action(self, action):
        """Process combat action"""
        self.clear_choices()
        
        if action == "attack":
            damage = random.randint(20, 30)
            self.droid_hp -= damage
            self.add_text(f"You attack for {damage} damage!", delay=False)
            
            if self.droid_hp > 0:
                incoming = random.randint(15, 25)
                self.player.take_damage(incoming)
                self.add_text(f"Droid attacks for {incoming} damage!", delay=False)
        
        elif action == "defend":
            self.add_text("You take a defensive stance!", delay=False)
            incoming = random.randint(5, 10)
            self.player.take_damage(incoming)
            self.add_text(f"Droid attacks for {incoming} damage (reduced)!", delay=False)
        
        else:  # heal
            self.player.heal(25)
            self.add_text("You use a med-kit and heal 25 HP!", delay=False)
            if self.droid_hp > 0:
                incoming = random.randint(15, 25)
                self.player.take_damage(incoming)
                self.add_text(f"Droid attacks for {incoming} damage!", delay=False)
        
        self.update_stats()
        self.root.after(1500, self.combat_round)
    
    def probe_scan(self):
        """Probe scanning path"""
        self.clear_choices()
        self.add_text("You launch a probe. Scans reveal organic life signs...")
        self.add_text("And something else - an energy signature unlike anything known.")
        self.player.energy -= 5
        self.update_stats()
        
        self.root.after(2000, self.probe_choice)
    
    def probe_choice(self):
        self.add_text("\nWhat do you do?")
        self.add_choice("1. Dock with the ship now that you know more", self.investigate_ship)
        self.add_choice("2. Call for backup from the nearest station", self.backup_ending)
        self.add_choice("3. Proceed directly to the main signal source", self.signal_source)
    
    def ignore_ship(self):
        """Ignoring the distress signal"""
        self.clear_choices()
        self.add_text("You continue toward the main signal. Your crew looks uneasy.")
        self.add_text("Suddenly, your ship shudders - you're caught in a tractor beam!")
        self.player.hp -= 20
        self.update_stats()
        
        self.root.after(2000, lambda: self.add_text("An alien vessel appears. They're scanning you..."))
        self.root.after(4000, self.alien_encounter)
    
    def ancient_artifact(self):
        """Artifact discovery scene"""
        self.clear_choices()
        self.add_text("You discover the ship's cargo bay. Inside...")
        self.add_text("A crystalline artifact pulses with otherworldly energy!")
        
        self.root.after(2000, self.artifact_choice)
    
    def artifact_choice(self):
        self.add_text("\nWhat do you do?")
        self.add_choice("1. Take the artifact", self.take_artifact)
        self.add_choice("2. Leave it and report your findings", self.safe_ending)
        self.add_choice("3. Study it first with your scanner", self.study_artifact)
    
    def take_artifact(self):
        self.clear_choices()
        self.add_text("As you touch it, visions flood your mind!")
        self.add_text("You see the location of an ancient alien gateway...")
        self.player.inventory.append("Crystalline Artifact")
        self.update_stats()
        self.root.after(3000, self.gateway_choice)
    
    def study_artifact(self):
        self.clear_choices()
        self.add_text("Scans reveal it's a key of some kind...")
        self.add_text("The main signal source - it's a lock mechanism!")
        self.player.inventory.append("Crystalline Key")
        self.update_stats()
        self.root.after(3000, self.signal_source)
    
    def alien_encounter(self):
        """Alien contact scene"""
        self.clear_choices()
        self.add_text("A voice speaks in perfect English:")
        self.add_text("'We are the Keepers. You have found what was lost.'")
        
        self.root.after(2000, self.alien_choice)
    
    def alien_choice(self):
        self.add_text("\nHow do you respond?")
        self.add_choice("1. 'We come in peace' (Diplomatic)", self.peaceful_alien)
        self.add_choice("2. 'Release us immediately!' (Aggressive)", self.aggressive_alien)
        self.add_choice("3. 'What is this place?' (Curious)", self.curious_alien)
    
    def peaceful_alien(self):
        self.clear_choices()
        self.add_text("'Your peaceful nature is noted. We will guide you.'")
        self.player.crew_members.append("Keeper Guide")
        self.update_stats()
        self.root.after(3000, self.gateway_choice)
    
    def aggressive_alien(self):
        self.clear_choices()
        self.add_text("'Hostility detected. Initiating defensive protocols.'")
        self.player.hp -= 30
        self.update_stats()
        self.add_text("Your ship takes damage before you can apologize!")
        self.root.after(3000, self.alien_encounter)
    
    def curious_alien(self):
        self.clear_choices()
        self.add_text("'This is the Gateway to the Lost Worlds. You may enter.'")
        self.root.after(3000, self.gateway_choice)
    
    def signal_source(self):
        """Main signal source"""
        self.clear_choices()
        self.add_text("You arrive at the signal source - a massive space station!")
        self.add_text("It's older than human civilization itself.")
        
        if "Crystalline Key" in self.player.inventory or "Crystalline Artifact" in self.player.inventory:
            self.add_text("\nYour artifact resonates with the station!")
            self.root.after(3000, self.gateway_choice)
        else:
            self.add_text("\nThe station's doors remain sealed. You need a key...")
            self.root.after(3000, self.search_ending)
    
    def gateway_choice(self):
        """Final major choice"""
        self.clear_choices()
        self.add_text("The gateway activates! It can transport you to:")
        self.add_text("Ancient worlds, untouched by time...")
        
        self.root.after(2000, self.final_choice)
    
    def final_choice(self):
        self.add_text("\nWhat is your decision?")
        self.add_choice("1. Enter the gateway (The Unknown)", self.explorer_ending)
        self.add_choice("2. Take readings and return home (Scientific Caution)", self.scientist_ending)
        self.add_choice("3. Invite humanity to explore together (Diplomatic)", self.diplomat_ending)
    
    # ENDINGS
    def explorer_ending(self):
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("ENDING: THE EXPLORER")
        self.add_text("=" * 50)
        self.add_text("\nYou step through the gateway. Light surrounds you...")
        self.add_text("On the other side, a new galaxy awaits.")
        self.add_text("Your name will be remembered as the first to traverse the Lost Sector.")
        self.add_text(f"\nCaptain {self.player.name}, your journey has just begun...")
        self.show_restart()
    
    def scientist_ending(self):
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("ENDING: THE SCIENTIST")
        self.add_text("=" * 50)
        self.add_text("\nYou collect invaluable data and return home.")
        self.add_text("Your discoveries advance human understanding by centuries.")
        self.add_text("The gateway remains, waiting for humanity to be ready.")
        self.add_text(f"\nCaptain {self.player.name}, you have enlightened humanity!")
        self.show_restart()
    
    def diplomat_ending(self):
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("ENDING: THE DIPLOMAT")
        self.add_text("=" * 50)
        self.add_text("\nYou call for humanity to witness this moment together.")
        self.add_text("The gateway becomes a symbol of unity and exploration.")
        self.add_text("A new era of cooperation begins among the stars.")
        self.add_text(f"\nCaptain {self.player.name}, you have united humanity!")
        self.show_restart()
    
    def safe_ending(self):
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("ENDING: THE CAUTIOUS COMMANDER")
        self.add_text("=" * 50)
        self.add_text("\nYou play it safe. The artifact is studied by experts.")
        self.add_text("Your career is stable, but you'll always wonder...")
        self.add_text("What mysteries lay beyond that signal?")
        self.add_text(f"\nCaptain {self.player.name}, you survived, but at what cost?")
        self.show_restart()
    
    def backup_ending(self):
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("ENDING: THE ONE THAT GOT AWAY")
        self.add_text("=" * 50)
        self.add_text("\nThe signal vanishes before you can investigate.")
        self.add_text("The mystery of Sector X-9 remains unsolved.")
        self.add_text("Perhaps some secrets are meant to stay hidden...")
        self.add_text(f"\nCaptain {self.player.name}, the stars keep their secrets.")
        self.show_restart()
    
    def search_ending(self):
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("ENDING: THE ENDLESS SEARCH")
        self.add_text("=" * 50)
        self.add_text("\nWithout the key, you cannot enter.")
        self.add_text("You dedicate your life to finding another way in...")
        self.add_text("The gateway taunts you with possibilities.")
        self.add_text(f"\nCaptain {self.player.name}, your quest continues...")
        self.show_restart()
    
    def game_over(self, reason):
        """Game over"""
        self.clear_choices()
        self.add_text("\n" + "=" * 50)
        self.add_text("GAME OVER")
        self.add_text("=" * 50)
        self.add_text(f"\n{reason}")
        self.add_text(f"Captain {self.player.name} fell in the line of duty.")
        self.add_text("The stars remember the brave...")
        self.show_restart()
    
    def show_restart(self):
        """Show restart button"""
        self.root.after(3000, lambda: self.add_choice("🔄 Play Again", self.restart_game))
    
    def restart_game(self):
        """Restart the game"""
        self.story_text.config(state=tk.NORMAL)
        self.story_text.delete(1.0, tk.END)
        self.story_text.config(state=tk.DISABLED)
        self.clear_choices()
        self.player = None
        self.stats_label.config(text="")
        self.show_intro()

def main():
    root = tk.Tk()
    game = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()