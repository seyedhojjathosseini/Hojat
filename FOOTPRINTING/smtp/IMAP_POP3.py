import sys
import getpass
import imaplib
import poplib

# Function to check if a port is open on a given host
def is_port_open(host, port):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
        return True
    except:
        return False
        
# Function to connect to a POP3 or IMAP server
def connect_to_mail_server(protocol, host, port, username, password):
    if protocol == "pop3":
        server = poplib.POP3(host, port)
        server.starttls()
        server.user(username)
        server.pass_(password.encode('utf-8'))
    elif protocol == "pop3s":
        server = poplib.POP3_SSL(host, port)
        server.user(username)
        server.pass_(password.encode('utf-8'))
    elif protocol == "imap":
        server = imaplib.IMAP4(host, port)
        server.login(username, password.encode('utf-8'))
    elif protocol == "imaps":
        server = imaplib.IMAP4_SSL(host, port)
        server.login(username, password)
    else:
        print("Invalid protocol")
        return None
    return server



# Function to display a list of emails
def list_emails(server, mailbox):
    if isinstance(server, poplib.POP3):
        response, message, octets = server.list()
        print(f"Messages in {mailbox}:\n")
        for i in message:
            num, size = i.split()
            response, lines, octets = server.top(num, 0)
            print(f"Message {num} ({int(size)} bytes):\n")
            for j in lines:
                print(j.decode())
            print("\n")
    elif isinstance(server, imaplib.IMAP4):
        server.select(mailbox)
        typ, data = server.search(None, 'ALL')
        for num in data[0].split():
            typ, msg_data = server.fetch(num, '(RFC822)')
            print(f"Message {num}:\n")
            print(msg_data[0][1].decode())
            print("\n")

# Function to download an email
def download_email(server, mailbox, message_num):
    if isinstance(server, poplib.POP3):
        response, lines, octets = server.retr(message_num)
        email = b"\n".join(lines).decode()
        print(f"Message {message_num}:\n")
        print(email)
        print("\n")
    elif isinstance(server, imaplib.IMAP4):
        server.select(mailbox)
        typ, msg_data = server.fetch(message_num, '(RFC822)')
        email = msg_data[0][1].decode()
        print(f"Message {message_num}:\n")
        print(email)
        print("\n")

# Function to delete an email
def delete_email(server, mailbox, message_num):
    if isinstance(server, poplib.POP3):
        server.dele(message_num)
        print(f"Message {message_num} in {mailbox} deleted.")
    elif isinstance(server, imaplib.IMAP4):
        server.select(mailbox)
        server.store(message_num, '+FLAGS', '\\Deleted')
        server.expunge()
        print(f"Message {message_num} in {mailbox} deleted.")






#def search_emails(server, mailbox, search_string):
#    server.select(mailbox)
#    typ, data = server.search(None, 'BODY', search_string)
#    if typ != 'OK':
#        print(f'Error searching for emails: {typ}')
#        return []
#    email_ids = data[0].split()
#    return email_ids

# Function to search emails
def search_emails(server, mailbox, search_string):
    if isinstance(server, poplib.POP3):
        response, message, octets = server.list()
        print(f"Messages in {mailbox} matching search string '{search_string}':\n")
        for i in message:
            num, size = i.split()
            response, lines, octets = server.top(num, 0)
            for j in lines:
                if search_string in j.decode():
                    print(f"Message {num}:\n")
                    print("\n".join(lines).decode())
                    print("\n")
    elif isinstance(server, imaplib.IMAP4):
        server.select(mailbox)
        typ, data = server.search(None, 'ALL')
        for num in data[0].split():
            typ, msg_data = server.fetch(num, '(RFC822)')
            if search_string in msg_data[0][1].decode():
                print(f"Message {num}:\n")
                print(msg_data[0][1].decode())
                print("\n")

def main():
    print("Welcome to the email client program!\n")
    protocol, host, port, username, password = get_user_credentials()
    server = connect_to_mail_server(protocol, host, port, username, password)
    
    while True:
        print("Select an option:\n")
        print("1. List emails")
        print("2. Download email")
        print("3. Delete email")
        print("4. Search emails")
        print("5. Exit")
        option = input("Enter option number: ")
        if option == "1":
            list_emails(server, "INBOX")
            list_emails(server, "SENT")
        elif option == "2":
            mailbox = input("Enter mailbox (INBOX or SENT): ")
            message_num = input("Enter message number: ")
            download_email(server, mailbox, message_num)
        elif option == "3":
            mailbox = input("Enter mailbox (INBOX or SENT): ")
            message_num = input("Enter message number: ")
            delete_email(server, mailbox, message_num)
        elif option == "4":
            search_string = input("Enter search string: ")
            search_emails(server, "INBOX", search_string)
            search_emails(server, "SENT", search_string)
        elif option == "5":
            server.quit()
            print("Goodbye!")
            sys.exit()
        else:
            print("Error: Invalid option entered.")

def get_user_credentials():
    while True:
        host = input("Enter the email server's IP address or hostname: ")
        if not is_port_open(host, 110) and not is_port_open(host, 995) and not is_port_open(host, 143) and not is_port_open(host, 993):
            print("Error: No open POP3 or IMAP ports found on server.")
            continue
        port = None
        while not port:
            protocol = input("Enter the email protocol (pop3, pop3s, imap, imaps): ")
            if protocol == "pop3" and is_port_open(host, 110):
                port = 110
            elif protocol == "pop3s" and is_port_open(host, 995):
                port = 995
            elif protocol == "imap" and is_port_open(host, 143):
                port = 143
            elif protocol == "imaps" and is_port_open(host, 993):
                port = 993
            else:
                print("Error: Invalid protocol or port is closed.")
        username = input("Enter your email username: ")
        password = getpass.getpass("Enter your email password: ")
        if connect_to_mail_server(protocol, host, port, username, password):
            return protocol, host, port, username, password
        else:
            print("Error: Incorrect username or password.")
            continue

if __name__ == "__main__":
    main()
