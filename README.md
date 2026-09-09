# 🗡️ Zelda Game Python

>An action-adventure RPG inspired by The Legend of Zelda, built using Python and the Pygame framework. Navigate tilemaps, engage in real-time combat, cast magic spells, and defeat enemy AI in a dynamic open-world style environment.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-387EF5?style=flat&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-Green?style=flat&logo=python&logoColor=white)

---

## 🎮 Features

* **Real-time Combat:** Sword attacks, weapon switching, and particle impact effects.
* **Magic & Spells:** Cast healing or attack spells using an interactive magic system.
* **Enemy AI & Physics:** Pathfinding, hitboxes, recoil physics, and enemy state machines.
* **Tilemap & Camera System:** Smooth camera tracking over custom-designed tilemaps.
* **UI & Stats:** Interactive HUD displaying health, stamina, EXP, weapon selection, and active magic.
* **Upgrade System:** Level up player stats including health, energy, attack power, and magic strength.

---

## 🚀 Demo & Screenshots

>   ![Project Preview](https://repository-images.githubusercontent.com/468181616/a7445cf0-7d0c-43b4-86ac-a7035f814767)

---
## 🛠️ Installation & Setup

### Prerequisites
Make sure you have **Python 3.11** installed on your system.

### Steps

1. **Clone the repository:**
    ```bash
    git clone [https://github.com/DevilSavi/Zelda_game_python git](https://github.com/DevilSavi/Zelda_game_python.git)

 * Navigate to the project directory:
    ```bash
    cd Zelda_game_python

 * Install dependencies:
    ```bash
    pip install pygame

 * Run the game:
    ```bash
    python main.py
   

## 📂 Project Structure

```
Zelda_game_python/
│
├── main.py             # Starts the Pygame application and runs the main loop.
├── debug.py            # Renders real-time debug info like FPS and positions on screen.
├── enemy.py            # Controls enemy AI, state machines, and attack behavior.
├── entity.py           # Base class for shared player and enemy movement/collision logic.
├── level.py            # Handles camera movement, map layout, and sprite updates.
├── magic.py            # Manages spellcasting mechanics, energy costs, and magic effects.
├── particles.py        # Spawns visual effects like spell impacts and leaf bursts.
├── player.py           # Controls player movement, stats, inputs, and weapon usage.
├── settings.py         # Stores global constants like resolution, colors, and tile sizes.
├── support.py          # Helper functions for importing CSV maps and slicing spritesheets.
├── tile.py             # Defines map tiles, collision boundaries, and interactive objects.
├── ui.py               # Renders the HUD, health bars, weapon icons, and EXP counter.
├── upgrade.py          # Handles the stat upgrade menu and attribute leveling system.
├── weapon.py           # Controls attack hitboxes, weapon sprites, and attack timing.
│
├── graphics/           # Folder for character animations, tilemaps, and UI assets.
├── audio/              # Folder for background music and sound effects.
└── README.md           # Project documentation
```
---

## 🕹️ Controls

| Action | Key / Control |
|---|---|
| Move | Arrow Keys |
| Attack | Spacebar |
| Cast Magic | Left Control |
| Switch Weapon | Q |
| Switch Magic | E |
| Upgrade Menu | M |
| Upgrade(in Menu) | Spacebar |

---

## 🤝 Contributing
Contributions, bug reports, and feature requests are welcome!

 * Fork the repository.
 * Create your feature branch (`git checkout -b feature/NewFeature`).
 * Commit your changes (`git commit -m 'Add NewFeature'`).
 * Push to the branch (`git push origin feature/NewFeature`).
 * Open a Pull Request.
---

## 📄 License

Distributed under the MIT License. See LICENSE for details.

> Copyright © Savindu Nethmika. 
> All Right Reserved.
