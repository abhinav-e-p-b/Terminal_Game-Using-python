# 🚀 Starship Odyssey: The Lost Sector

A captivating space adventure game with multiple storylines, combat mechanics, and meaningful choices that affect the outcome. Available in both **Terminal** and **GUI** versions!

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📖 Story

Year 2347. Humanity has reached the stars, and you are the captain of the USS Wanderer. Your ship has detected a mysterious signal from Sector X-9, a region marked as "Lost" on all star charts. Your decisions will determine the fate of your crew and potentially all of humanity.

## ✨ Features

### Game Mechanics
- **Dynamic Story Branching**: Your choices matter! Multiple paths lead to different outcomes
- **RPG Elements**: Health points, energy system, inventory management
- **Turn-Based Combat**: Strategic combat with attack, defend, and heal options
- **Crew Management**: Recruit crew members who affect your story
- **7 Unique Endings**: From explorer to diplomat, each playthrough can be different

### Two Versions Available

#### 🖥️ Terminal Version (`terminal_game.py`)
- Classic text-based adventure
- Typewriter text effect for immersion
- Color-coded status displays
- Runs in any terminal/command prompt

#### 🎨 GUI Version (`gui_game.py`)
- Beautiful graphical interface with retro space theme
- Interactive buttons for choices
- Real-time stats display (HP, Energy, Inventory, Crew)
- Scrollable story window
- Smooth typewriter effect
- Dark space-themed design with neon green accents

## 🎮 Installation

### Requirements
- Python 3.7 or higher
- tkinter (for GUI version - usually comes pre-installed with Python)

### Setup

1. Clone or download this repository:
```bash
git clone https://github.com/yourusername/starship-odyssey.git
cd starship-odyssey
```

2. Ensure Python is installed:
```bash
python --version
```

3. No additional packages needed! Both versions use Python's standard library.

## 🚀 How to Play

### Terminal Version
```bash
python terminal_game.py
```

### GUI Version
```bash
python gui_game.py
```

## 🎯 Gameplay Guide

### Making Choices
- Read the story text carefully
- Choose from 2-4 options at each decision point
- Your choices affect:
  - Story progression
  - Character relationships
  - Combat encounters
  - Final ending

### Combat System
When you encounter enemies, you have three options:
- **Attack**: Deal 20-30 damage
- **Defend**: Reduce incoming damage significantly
- **Heal**: Restore 25 HP (limited use)

### Stats Explained
- **HP (Health Points)**: Your life force. Reach 0 and it's game over
- **Energy**: Used for special actions and travel
- **Inventory**: Items you collect that may unlock new paths
- **Crew**: Allies who join your journey

## 📊 Possible Endings

Can you discover all 7 endings?

1. **The Explorer** - Brave the unknown gateway
2. **The Scientist** - Return with invaluable data
3. **The Diplomat** - Unite humanity for exploration
4. **The Cautious Commander** - Play it safe
5. **The One That Got Away** - Miss the opportunity
6. **The Endless Search** - Quest without closure
7. **Game Over** - Fall in the line of duty

## 🎨 Screenshots

### Terminal Version
```
==================================================
STARSHIP ODYSSEY: The Lost Sector
==================================================

Year 2347. Humanity has reached the stars...
Your ship, the USS Wanderer, has detected a mysterious signal
from Sector X-9, a region marked as 'Lost' on all star charts.

Enter your captain's name: Roy

==================================================
Captain Roy | HP: 100/100 | Energy: 50
==================================================

Your sensors pick up a distress signal from a nearby ship.
Scans reveal it's damaged but might contain survivors... or danger.

What do you do?
1. Dock with the ship and investigate
2. Send a probe to scan first
3. Ignore it and continue to the signal source

Your choice: _
```

### GUI Version
*Dark space-themed interface with neon green text, interactive buttons, and real-time stats display*

## 🛠️ Technical Details

### Terminal Version Features
- `sys.stdout` for typewriter effect
- Input validation and error handling
- Clean terminal display with separators
- Modular function design

### GUI Version Features
- Built with `tkinter`
- Custom color scheme (#0a0e27 background, #00ff88 text)
- Event-driven programming
- Responsive button layout
- Scrollable text widget
- Modal dialogs for input

## 🤝 Contributing

Contributions are welcome! Here are some ideas:
- Add more story branches
- Create new enemy types
- Design additional endings
- Add sound effects (GUI version)
- Implement save/load system
- Create difficulty levels

## 📝 License

This project is licensed under the MIT License - feel free to use, modify, and distribute as you see fit.

## 🙏 Credits

Created as a Python learning project demonstrating:
- Object-oriented programming
- Game logic and state management
- User interface design (both CLI and GUI)
- Branching narratives
- Random number generation for combat

## 🐛 Known Issues

- Terminal version may have display issues on some Windows terminals (use Windows Terminal or PowerShell for best experience)
- GUI version requires tkinter, which may need separate installation on some Linux distributions

## 📧 Contact

Have questions or suggestions? Feel free to open an issue or reach out!

---

**Enjoy your journey through the stars, Captain! 🌟**