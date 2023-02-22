import whois
import argparse

def get_whois_info(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if domain_info.status:
            print("Domain: ", domain_name)
            print("Registrar: ", domain_info.registrar)
            print("Creation Date: ", domain_info.creation_date)
            print("Expiration Date: ", domain_info.expiration_date)
            print("Updated Date: ", domain_info.updated_date)
            print("Name Servers: ", domain_info.name_servers)
            print("Status: ", domain_info.status)
        else:
            print("Domain information is not available for:", domain_name)
    except Exception as e:
        print("Error: ", e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get WHOIS information for a domain')
    parser.add_argument('domain', metavar='D', type=str, help='The domain name')
    args = parser.parse_args()
    domain_name = args.domain
    if domain_name.startswith("http://"):
        domain_name = domain_name[7:]
    get_whois_info(domain_name)
