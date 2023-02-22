import requests
import argparse
from bs4 import BeautifulSoup


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", dest="domain", help="Domain name to find subdomains for.")
    return parser.parse_args()


def get_subdomains_vt(domain, api_key):
    url = "https://www.virustotal.com/api/v3/domains/{}/subdomains".format(domain)
    headers = {'x-apikey': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        vt_data = response.json()
        if 'data' in vt_data:
            return [subdomain['id'] for subdomain in vt_data['data']]
    print("No subdomains found on VirusTotal")
    return []


def get_subdomains_crt(domain):
    url = "https://crt.sh/?q=%25.{}&output=json".format(domain)
    response = requests.get(url)
    if response.status_code == 200:
        crt_data = response.content.decode('utf-8')
        crt_data = "[" + crt_data.replace("}{", "},{") + "]"
        crt_json = json.loads(crt_data)
        return list(set([subdomain['name_value'] for subdomain in crt_json]))
    print("No subdomains found on crt.sh")
    return []


def get_subdomains_censys(domain, api_id, api_secret):
    subdomains = []
    url = "https://censys.io/api/v1/search/certificates"
    params = {"query": "parsed.names:*.{}".format(domain), "fields": ["parsed.names"]}
    r = requests.post(url, auth=(api_id, api_secret), json=params)
    if r.status_code == 200:
        results = r.json()['results']
        for result in results:
            subdomains.extend(result['parsed.names'])
        subdomains = list(set(subdomains))
        return subdomains
    print("No subdomains found on censys.io")
    return []


if __name__ == "__main__":
    args = get_arguments()
    domain = args.domain
    print("Finding subdomains for domain: {}\n".format(domain))

    # VirusTotal
    vt_api_key = "YOUR_VIRUSTOTAL_API_KEY"
    subdomains_vt = get_subdomains_vt(domain, vt_api_key)
    if subdomains_vt:
        print("Subdomains found on VirusTotal:")
        print("\n".join(subdomains_vt))
        print("")

    # crt.sh
    subdomains_crt = get_subdomains_crt(domain)
    if subdomains_crt:
        print("Subdomains found on crt.sh:")
        print("\n".join(subdomains_crt))
        print("")

    # Censys
    censys_api_id = "YOUR_CENSYS_API_ID"
    censys_api_secret = "YOUR_CENSYS_API_SECRET"
    subdomains_censys = get_subdomains_censys(domain, censys_api_id, censys_api_secret)
    if subdomains_censys:
        print("Subdomains found on censys.io:")
        print("\n".join(subdomains_censys))
        print("")
