# Sanja Filipova


def show_instructions():
    """Display the game title, objective, and available commands."""
    print('==========================================')
    print('            PROJECT BLACKOUT')
    print('==========================================')
    print()
    print('Sentinel Cyber Solutions is under attack.')
    print('A hacker known as Ghost has launched a')
    print('ransomware attack.')
    print()
    print('==========================================')
    print()
    print('MISSION:')
    print('Collect all 6 cybersecurity tools before')
    print('entering the Server Room.')
    print('If you enter too early, Ghost wins.')
    print()
    print('COMMANDS:')
    print('Move: go north, south, east, or west')
    print('Collect: get [item name]')
    print()
    print()


def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and room item."""
    print('------------------------------------------')
    print('You are in the', current_room)
    print(f'Inventory ({len(inventory)}/6):')

    # Display the items currently in the player's inventory.
    if inventory:
        for item in inventory:
            print('-', item)
    else:
        print('- Empty')

    # Display the item if the current room still contains one.
    if 'item' in rooms[current_room]:
        print('Item Available:', rooms[current_room]['item'])
    else:
        print('Item Available: None')

    print('------------------------------------------')


def main():
    # Dictionary linking rooms, directions, and items.
    rooms = {
        'Reception': {
            'North': 'IT Office',
            'South': 'Backup Storage',
            'East': 'Development Lab',
            'West': 'Help Desk'
        },
        'Help Desk': {
            'East': 'Reception',
            'item': 'Access Badge'
        },
        'IT Office': {
            'South': 'Reception',
            'East': 'Network Closet',
            'item': 'Administrator Credentials'
        },
        'Network Closet': {
            'West': 'IT Office',
            'item': 'Network Access Key'
        },
        'Development Lab': {
            'West': 'Reception',
            'North': 'Security Operations Center (SOC)',
            'item': 'Master Decryption Key'
        },
        'Security Operations Center (SOC)': {
            'South': 'Development Lab',
            'item': 'Firewall Rule File'
        },
        'Backup Storage': {
            'North': 'Reception',
            'East': 'Server Room',
            'item': 'Offline Backup Drive'
        },
        'Server Room': {
            'West': 'Backup Storage'
        }
    }

    # Name of the room containing the villain.
    villain_room = 'Server Room'

    # Number of items required to win the game.
    required_items = 6

    # Player starts in Reception.
    current_room = 'Reception'

    # Empty inventory at the start of the game.
    inventory = []

    # Display game instructions.
    show_instructions()

    # Continue the game until the player wins or loses.
    while True:
        show_status(current_room, inventory, rooms)

        # Get the player's command.
        command = input('Enter your move: ').strip()
        print()

        # Handle movement commands.
        if command.lower().startswith('go '):
            direction = command[3:].strip().title()

            # Check if the direction is available from the current room.
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]

                # Check whether the player entered the villain's room.
                if current_room == villain_room:
                    if len(inventory) == required_items:
                        print('==========================================')
                        print('             MISSION COMPLETE')
                        print('==========================================')
                        print()
                        print('You stopped Ghost and saved Sentinel Cyber')
                        print('Solutions!')
                        print('All 6 cybersecurity tools were collected.')
                        print()
                        print('Project Blackout was a success!')
                        print()
                        print('==========================================')
                    else:
                        print('==========================================')
                        print('                GAME OVER')
                        print('==========================================')
                        print()
                        print("Ghost encrypted the company's data.")
                        print('You confronted Ghost without all 6 tools.')
                        print()
                        print('Project Blackout has failed!')
                        print()
                        print('==========================================')

                    print()
                    print('Thank you for playing Project Blackout!')
                    break

            else:
                print(f"You can't go {direction.lower()} from the {current_room}.")

        # Handle item pickup commands.
        elif command.lower().startswith('get '):
            item_name = command[4:].strip()

            # Check if the room contains the requested item.
            if ('item' in rooms[current_room] and
                    item_name.lower() == rooms[current_room]['item'].lower()):
                inventory.append(rooms[current_room]['item'])
                print(f"Item collected: {rooms[current_room]['item']}")

                # Remove the item so it cannot be collected again.
                del rooms[current_room]['item']

            elif 'item' not in rooms[current_room]:
                print('There is no item to collect in this room.')

            else:
                print("That item isn't available in this room.")

        # Handle invalid commands.
        else:
            print("Invalid command. Use 'go [direction]' or")
            print("'get [item name]'.")


if __name__ == '__main__':
    main()