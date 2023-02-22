import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

domain_name = input("Please enter the domain name: ")
url = "https://sitereport.netcraft.com/?url=" + domain_name

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = PrettyTable(["Category", "Result"])
table.align["Category"] = "l"
table.align["Result"] = "l"

# Site
th = soup.find("th", string="Site")
td = th.find_next("td")
table.add_row(["Site", td.text.strip()])

# Netblock Owner
th = soup.find("th", string="Netblock Owner")
td = th.find_next("td")
netblock_owner = td.text.strip().replace('\n\n', '\n')
table.add_row(["Netblock Owner", netblock_owner])

# Hosting company
th = soup.find("th", string="Hosting company")
td = th.find_next("td")
table.add_row(["Hosting company", td.text.strip()])

# Hosting country
th = soup.find("th", string="Hosting country")
td = th.find_next("td")
table.add_row(["Hosting country", td.text.strip()])

# IPv4 address
th = soup.find("th", string="IPv4 address")
td = th.find_next("td")
table.add_row(["IPv4 address", td.text.strip()])

# IPv4 autonomous systems
th = soup.find("th", string="IPv4 autonomous systems")
td = th.find_next("td")
table.add_row(["IPv4 autonomous systems", td.text.strip()])

# IPv6 address
th = soup.find("th", string="IPv6 address")
td = th.find_next("td")
table.add_row(["IPv6 address", td.text.strip()])


# IPv6 autonomous systems
th = soup.find("th", string="IPv6 autonomous systems")
td = th.find_next("td")
table.add_row(["IPv6 autonomous systems", td.text.strip()])

# Reverse DNS
th = soup.find("th", string="Reverse DNS")
td = th.find_next("td")
table.add_row(["Reverse DNS", td.text.strip()])

# Domain
th = soup.find("th", string="Domain")
td = th.find_next("td")
table.add_row(["Domain", td.text.strip()])

# Nameserver
th = soup.find("th", string="Nameserver")
td = th.find_next("td")
table.add_row(["Nameserver", td.text.strip()])

# Domain registrar
th = soup.find("th", string="Domain registrar")
td = th.find_next("td")
table.add_row(["Domain registrar", td.text.strip()])

# Nameserver organisation
th = soup.find("th", string="Nameserver organisation")
td = th.find_next("td")
table.add_row(["Nameserver organisation", td.text.strip()])

# Organisation
th = soup.find("th", string="Organisation")
td = th.find_next("td")
table.add_row(["Organisation", td.text.strip()])

# DNS admin
th = soup.find("th", string="DNS admin")
td = th.find_next("td")
table.add_row(["DNS admin", td.text.strip()])

# Top Level Domain
th = soup.find("th", string="Top Level Domain")
td = th.find_next("td")
table.add_row(["Top Level Domain", td.text.strip()])

# DNS Security Extensions
th = soup.find("th", string="DNS Security Extensions")
td = th.find_next("td")
table.add_row(["DNS Security Extensions", td.text.strip()])

# DNS Security Extensions
th = soup.find("th", string="DNS Security Extensions")
td = th.find_next("td")
table.add_row(["DNS Security Extensions", td.text.strip()])


print(table)
