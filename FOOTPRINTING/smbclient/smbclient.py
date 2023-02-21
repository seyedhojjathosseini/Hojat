import smbclient
import argparse

def list_files(client, path):
    for filename in client.listdir(path):
        print(filename)

def create_file(client, path, content):
    with client.open_file(path, mode='w') as f:
        f.write(content)

def read_file(client, path):
    with client.open_file(path, mode='r') as f:
        content = f.read()
        print(content)

def main():
    parser = argparse.ArgumentParser(description='SMB client')
    parser.add_argument('ip_address', type=str, help='IP address of SMB server')
    parser.add_argument('share_name', type=str, help='name of the shared folder')
    parser.add_argument('--username', type=str, default='guest', help='username for authentication')
    parser.add_argument('--password', type=str, help='password for authentication')
    parser.add_argument('--list', action='store_true', help='list files in the shared folder')
    parser.add_argument('--create', type=str, metavar='FILE', help='create a new file with the given name')
    parser.add_argument('--read', type=str, metavar='FILE', help='read the content of the given file')

    args = parser.parse_args()

    with smbclient.SambaClient(f"//{args.ip_address}/{args.share_name}", username=args.username, password=args.password) as client:
        if args.list:
            list_files(client, '/')
        elif args.create:
            create_file(client, args.create, 'This is a test file.')
        elif args.read:
            read_file(client, args.read)
        else:
            parser.print_help()

if __name__ == '__main__':
    main()
