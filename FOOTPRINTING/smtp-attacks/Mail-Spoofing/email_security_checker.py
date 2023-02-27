import argparse
import dns.resolver
import smtplib


def check_spoofing(domain):
    try:
        smtp = smtplib.SMTP(domain)
        return True
    except:
        return False



# function to check DKIM record

def check_dkim(domain):
    try:
        dkim_record = dns.resolver.resolve('_adsp._domainkey.{}'.format(domain), 'TXT')
        if len(dkim_record) == 0:
            return False
        else:
            return True
    except:
        return False

# function to check SPF record
def check_spf(domain):
    try:
        spf_record = dns.resolver.resolve(domain, 'TXT')
        for rdata in spf_record:
            if 'v=spf1' in str(rdata):
                return True
        return False
    except:
        return False

def test_open_relay(server):
    try:
        conn = smtplib.SMTP(server)
        code, msg = conn.ehlo()
        if code == 250:
            print(f"{server} is not an open relay")
        else:
            print(f"{server} is an open relay")
        conn.quit()
    except Exception as e:
        print(f"Failed to connect to {server}: {e}")

if __name__ == '__main__':
    print("Welcome to the Email Security Checker!\n")
    print("This program checks an email domain's SPF and DKIM records, and tests if the SMTP server is an open relay.\n")
    
    # Define the explanations as strings
    open_relay_explanation = "An open relay is a mail server that allows anyone to send email messages through it, regardless of whether they are authorized to do so. This can lead to spam or phishing attacks."
    spf_explanation = "SPF (Sender Policy Framework) is an email authentication method that helps prevent email spoofing. It allows the recipient's email server to check that incoming mail from a domain is being sent from a server authorized by that domain's administrators."
    dkim_explanation = "DKIM (DomainKeys Identified Mail) is another email authentication method that uses a public key cryptography to verify the authenticity of an email message. It adds a digital signature to the message header that can be validated by the recipient's email server."

    # Print the explanations with a nice format
    print("EXPLANATIONS")
    print("=" * 20)
    print(f"Open Relay:\n{open_relay_explanation}\n")
    print(f"SPF:\n{spf_explanation}\n")
    print(f"DKIM:\n{dkim_explanation}\n\n")

    
    print("Example usage: python email_security_checker.py example.com mail.example.com\n")

    domain = input("Enter the email domain to check: ")
    smtp_server = input("Enter the SMTP server to test for open relay (press Enter to skip): ")

    dkim_result = check_dkim(domain)
    if dkim_result:
        print('{} has a valid DKIM record.'.format(domain))
    else:
        print('{} does not have a valid DKIM record.'.format(domain))


    # Test for open relay
    if smtp_server:
        print("\nTesting for open relay...")
        test_open_relay(smtp_server)

# check SPF record
    spf_result = check_spf(domain)
    if spf_result:
        print('{} has a valid SPF record.'.format(domain))
    else:
        print('{} does not have a valid SPF record.'.format(domain))

    # check webmail spoofing
    spoofing_result = check_spoofing('webmail.' + domain)
    if spoofing_result:
        print('{}\'s webmail has the ability to spoof.'.format(domain))
    else:
        print('{}\'s webmail does not have the ability to spoof.'.format(domain))