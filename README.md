# Project Blackout — Python Text Adventure Game

A cybersecurity-themed text adventure game developed in Python as part of my IT-140 Introduction to Scripting coursework at Southern New Hampshire University (SNHU).

## Project Overview

Project Blackout is a command-line adventure game where the player takes on the role of someone trying to protect Sentinel Cyber Solutions from a ransomware attack.

A hacker known as Ghost has targeted the company, and the player's mission is to explore the building, collect six cybersecurity tools, and reach the Server Room to stop the attack.

The challenge is to collect every required item before confronting Ghost. Entering the Server Room without all six tools results in losing the game.

## Technologies Used

- Python 3
- Python standard library (no external packages required)
- GitHub for version control and documentation

## Game Features

- Eight interconnected rooms to explore
- Six collectible cybersecurity-themed items
- Room navigation using directional commands
- Inventory tracking and item collection
- Input validation for invalid commands
- Different winning and losing outcomes
- Interactive command-line gameplay

## Game Map and Items

| Room | Available Item |
|---|---|
| Reception | Starting location |
| Help Desk | Access Badge |
| IT Office | Administrator Credentials |
| Network Closet | Network Access Key |
| Development Lab | Master Decryption Key |
| Security Operations Center (SOC) | Firewall Rule File |
| Backup Storage | Offline Backup Drive |
| Server Room | Final confrontation with Ghost |

## How to Play

### 1. Run the Game

Make sure Python 3 is installed on your computer.

Download or clone this repository, open a terminal in the project folder, and run:

```bash
python TextBasedGame.py
```

On some systems, the command may be `python3 TextBasedGame.py`.

### 2. Navigate Between Rooms

Use the following commands:

- `go north`
- `go south`
- `go east`
- `go west`

The game will tell you if you cannot move in a particular direction.

### 3. Collect Cybersecurity Tools

When an item is available in your current room, collect it by typing its name after `get`.

For example:

```text
get Access Badge
```

Your inventory will update automatically after collecting an item.

### 4. Complete the Mission

Collect all six cybersecurity tools before entering the Server Room.

**Winning condition:** Enter the Server Room with all six items.

**Losing condition:** Enter the Server Room before collecting all six items.

## Python Skills Demonstrated

This project demonstrates several programming concepts:

- **Functions:** Separating game instructions, player status, and gameplay logic.
- **Dictionaries:** Storing rooms, connections, and collectible items.
- **Loops:** Keeping the game running until the player wins or loses.
- **Conditional Statements:** Checking movement, inventory, and game outcomes.
- **Lists:** Managing collected inventory items.
- **String Methods:** Processing player commands with methods such as `strip()`, `lower()`, and `title()`.
- **Input Validation:** Handling invalid commands and unavailable items.

## Project Structure

```text
project-blackout-python-game/
├── TextBasedGame.py
├── README.md
└── .gitignore
```

## Future Improvements

As I continue developing my Python skills, I would like to expand the game by:

- Adding a map command to help players navigate.
- Allowing players to restart without rerunning the program.
- Adding more rooms, challenges, and interactive events.
- Introducing cybersecurity-related puzzles.
- Improving the game's command handling and user experience.

## About This Project

I created Project Blackout while studying Computer Science at Southern New Hampshire University.

Since I am interested in pursuing a career in cybersecurity, I wanted to develop a game with a cybersecurity theme while practicing fundamental Python programming concepts.

This project helped me strengthen my understanding of program structure, user input, loops, conditional logic, and working with dictionaries and lists.
