import dns.resolver
import argparse
from tabulate import tabulate

# Parsing command line arguments
parser = argparse.ArgumentParser(description="Gathering DNS information for a domain.")
parser.add_argument('domain', type=str, help="Domain to gather information for.")
args = parser.parse_args()

name = args.domain

# Perform a DNS query for the given record type
def dns_query(name, record_type):
    try:
        answer = dns.resolver.resolve(name, record_type)
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        return None
    except dns.exception.Timeout:
        return None
    return answer

# Query A records
a_records = dns_query(name, 'A')
a_list = [rdata.address for rdata in a_records] if a_records else []
print("\nA records:")
print(tabulate([(a,) for a in a_list], headers=["IPv4 Address"]))

# Query MX records
mx_records = dns_query(name, 'MX')
if mx_records:
    mx_list = [(rdata.preference, rdata.exchange.to_text()) for rdata in mx_records]
    print("\nMX records:")
    print(tabulate(mx_list, headers=["Preference", "Mail exchanger"]))

# Query CNAME records
cname_records = dns_query(name, 'CNAME')
cname_list = [rdata.target.to_text() for rdata in cname_records] if cname_records else []
print("\nCNAME records:")
print(tabulate([(c,) for c in cname_list], headers=["Canonical Name"]))

# Query TXT records
txt_records = dns_query(name, 'TXT')
txt_list = [rdata.to_text() for rdata in txt_records] if txt_records else []
print("\nTXT records:")
print(tabulate([(t,) for t in txt_list], headers=["Text"]))

# Query SOA records
soa_records = dns_query(name, 'SOA')
soa_list = [(rdata.mname.to_text(), rdata.rname.to_text(), rdata.serial, rdata.refresh, rdata.retry, rdata.expire, rdata.minimum) for rdata in soa_records] if soa_records else []
print("\nSOA records:")
print(tabulate(soa_list, headers=["Primary master name", "Responsible authority's mailbox", "Serial number", "Refresh interval", "Retry interval", "Expire limit", "Minimum TTL"]))

# Perform a zone transfer
try:
    zt = dns.resolver.resolve(name, 'AXFR')
    zt_list = [(rdata.mname.to_text(), rdata.rname.to_text(), rdata.serial, rdata.refresh, rdata.retry, rdata.expire, rdata.minimum) for rdata in zt] if zt else []
    print("\nZonetransfer records:")
    print(tabulate(zt_list, headers=["Primary master name", "Responsible authority's mailbox", "Serial number", "Refresh interval", "Retry interval", "Expire limit", "Minimum TTL"]))
except dns.resolver.NoMetaqueries:
    print("\nZone transfer not allowed.")
