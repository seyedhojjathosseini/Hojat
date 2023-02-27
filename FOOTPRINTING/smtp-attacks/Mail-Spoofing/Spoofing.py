import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

print("Welcome to SMTP Email Spoofer!\n")
print("This program allows you to send an email with a spoofed 'From' address.")
print("Please follow the prompts to send your email.\n")
# Get input from user
from_addr = input("Enter the spoofed 'From' address: ")
to_addr = input("Enter the recipient email address: ")
subject = input("Enter the email subject: ")
body = input("Enter the email body: ")
attachment = input("Enter the path to an image file to attach to the email (or leave blank): ")
server = input("Enter the SMTP server address: ")
port = int(input("Enter the SMTP server port (or leave blank for default 587): ") or "587")
username = input("Enter the SMTP server username: ")
password = input("Enter the SMTP server password: ")

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(body)
msg.attach(body)
if attachment:
    with open(attachment, 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)

try:
    with smtplib.SMTP(server, port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username, password)
        smtp.sendmail(from_addr, to_addr, msg.as_string())
    print("Email sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Error: The server didn't accept the username and password combination.")
except smtplib.SMTPConnectError:
    print("Error: Could not connect to the server.")
except smtplib.SMTPDataError as e:
    print(f"Error: {e.smtp_code} {e.smtp_error.decode()}")
except Exception as e:
    print(f"Error: {e}")
