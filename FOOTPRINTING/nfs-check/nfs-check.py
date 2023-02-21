import argparse
import os

def check_nfs_access(ip, port):
    if os.system(f"nc -zv {ip} {port}") != 0:
        print(f"Port {port} is not open for {ip}")
        return

    cmd = f"rpcinfo -p {ip}"
    output = os.popen(cmd).read()

    if "nfs" not in output:
        print(f"No NFS access for {ip}")
        return

    lines = output.split("\n")[1:]
    for line in lines:
        fields = line.split()
        if len(fields) > 2 and fields[1] == "nfs":
            print(fields[2])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check NFS access and list files using rpcinfo")
    parser.add_argument("ip", help="IP address to check")
    parser.add_argument("--port", default=111, type=int, help="Port to check (default: 111)")
    args = parser.parse_args()

    check_nfs_access(args.ip, args.port)
