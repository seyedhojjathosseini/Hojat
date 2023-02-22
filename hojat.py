import os

# Function to clear the console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def print_boxed_text(text):
    # Determine the length of the longest line of text.
    longest_line_length = max([len(line) for line in text.split('\n')])

    # Print the top border of the box.
    print('┌' + '─' * (longest_line_length + 2) + '┐')

    # Print the text with borders on either side.
    for line in text.split('\n'):
        print('│ ' + line + ' ' * (longest_line_length - len(line)) + ' │')

    # Print the bottom border of the box.
    print('└' + '─' * (longest_line_length + 2) + '┘')



# Main menu function
def main_menu():
    clear()
    # Banner:
    text = """    Hojat is a modular security toolkit for penetration testing, enabling efficient vulnerability assessment,
            network analysis, and web application testing with customizable and extensible features.    """
    print_boxed_text(text)
    print("\n\n\n")
    # coding: utf-8
    print ("""


     ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
    ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀▀█░█▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ 
    ▐░▌       ▐░▌▐░▌       ▐░▌      ▐░▌    ▐░▌       ▐░▌     ▐░▌     
    ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌      ▐░▌    ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     
    ▐░░░░░░░░░░░▌▐░▌       ▐░▌      ▐░▌    ▐░░░░░░░░░░░▌     ▐░▌     
    ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌      ▐░▌    ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     
    ▐░▌       ▐░▌▐░▌       ▐░▌      ▐░▌    ▐░▌       ▐░▌     ▐░▌     
    ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌ ▄▄▄▄▄█░▌    ▐░▌       ▐░▌     ▐░▌     
    ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░▌    ▐░▌       ▐░▌     ▐░▌     
     ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀      ▀         ▀       ▀      
                                                                 




    SeyedHojjatHosseini@gmail.com

    www.hojat.org


    """)

    print("    Menu Options:")
    print("    1: FOOTPRINTING/DNS - dns-gathering.py")
    print("    2: FOOTPRINTING/nfs-check - nfs-check.py")
    print("    3: FOOTPRINTING/rpcclient - rpcclient.py")
    print("    4: FOOTPRINTING/smbclient - smbclient.py")
    print("    5: FOOTPRINTING/smtp - smtp.py")
    print("    6: INFORMATION GATHERING/netcraft - netcraft.py")
    print("    7: INFORMATION GATHERING/subdomain - subdomain.py")
    print("    8: INFORMATION GATHERING/whois - my_whois.py")
    print("    0: Exit\n")

# Loop to display the menu and run the selected script
while True:
    main_menu()
    selection = input("    Enter the number of the script you want to run: ")
    if selection == '0':
        break
    elif selection == '1':
        os.system('python FOOTPRINTING/DNS/dns-gathering.py')
    elif selection == '2':
        os.system('python FOOTPRINTING/nfs-check/nfs-check.py')
    elif selection == '3':
        os.system('python FOOTPRINTING/rpcclient/rpcclient.py')
    elif selection == '4':
        os.system('python FOOTPRINTING/smbclient/smbclient.py')
    elif selection == '5':
        os.system('python FOOTPRINTING/smtp/smtp.py')
    elif selection == '6':
        os.system('python "INFORMATION GATHERING/netcraft/netcraft.py"')
    elif selection == '7':
        os.system('python "INFORMATION GATHERING/subdomain/subdomain.py"')
    elif selection == '8':
        os.system('python "INFORMATION GATHERING/whois/my_whois.py"')
    else:
        print("Invalid selection, please try again.")
        input("Press enter to continue...")

    print("\nScript execution completed.\n")
    run_again = input("Do you want to run another script? (y/n): ")
    if run_again.lower() != 'y':
        break
