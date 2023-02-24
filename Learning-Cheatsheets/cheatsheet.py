import os
import re
from prettytable import PrettyTable

def display_cheatsheet(file_name):
    # Build the file path
    file_path = os.path.join(os.getcwd(), 'cheatsheet', file_name)

    # Read the contents of the file
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract the commands and descriptions using regular expressions
    commands = re.findall(r'\| `(.+?)` \| (.+?) \|', content)

    # Create a table to display the commands and their descriptions
    table = PrettyTable(['Command', 'Description'])
    table.align['Command'] = 'l'
    table.align['Description'] = 'l'

    # Add each command and description to the table
    for command, description in commands:
        table.add_row([command, description.strip()])

    # Print the table
    print(table)



if __name__ == '__main__':
    cheatsheets = {
        '1': 'INTRO_TO_NETWORK_TRAFFIC_ANALYSIS.md',
        '2': 'INTRODUCTION_TO_ACTIVE_DIRECTORY.md',
        '3': 'INTRODUCTION_TO_WINDOWS_COMMAND_LINE.md',
        '4': 'LINUX_FUNDAMENTALS.md',
        '5': 'WEB_REQUESTS.md',
        '6': 'WINDOWS_FUNDAMENTALS.md'
    }

    while True:
        # Display the list of available cheatsheets
        print('Welcome to the cheatsheet viewer! These are a series of files containing Linux and Windows commands along with instructions.')
        print('Here\'s a list of available cheatsheets:')
        for number, name in cheatsheets.items():
            print(f'{number}. {name}')

        # Ask the user to select a cheatsheet or quit
        user_input = input('Enter the number of the file you want to view or press q to quit: ')
        if user_input == 'q':
            break

        # Display the selected cheatsheet or an error message if it doesn't exist
        file_name = cheatsheets.get(user_input)
        if file_name is None:
            print('Invalid input. Please enter a valid number or press q to quit.')
        else:
            display_cheatsheet(file_name)
