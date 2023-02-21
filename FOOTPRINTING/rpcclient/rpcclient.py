#!/usr/bin/env python

import argparse
import sys
from impacket import smb, version, smbconnection, ntlm
from impacket.dcerpc.v5 import transport, scmr
from impacket.examples import logger

def print_help():
    print("usage: rpcclient.py [-h] host port")
    print("\nArguments:")
    print("  host        IP address of the target machine")
    print("  port        Port to use for SMB/RPC connections")
    print("\nOptions:")
    print("  -h, --help  Show this help message and exit")

def rpcclient(host, port):
    try:
        smb_connection = smbconnection.SMBConnection(host, host, sess_port=port)
        smb_connection.login('', '')
    except smb.smb_structs.SessionError as e:
        logging.error(str(e))
        sys.exit(1)

    dce = transport.DCERPCTransportFactory(f"ncacn_np:{host}[\pipe\epmapper]").get_dce_rpc()
    dce.connect()
    dce.bind(scmr.MSRPC_UUID_SCMR)

    scmr.hROpenSCManagerW(dce)

    while True:
        cmd = input('rpcclient $ ')
        if cmd in ['quit', 'exit']:
            break
        elif cmd == 'help':
            print('Command                 Description')
            print('-------                 -----------')
            print('querydispinfo           Query information about a service')
            print('openscmanager           Open a connection to the SCM')
            print('quit, exit              Exit rpcclient')
        elif cmd == 'openscmanager':
            scmr.hROpenSCManagerW(dce)
            print('Success')
        elif cmd.startswith('querydispinfo'):
            try:
                service_name = cmd.split()[1]
                service_handle = scmr.hROpenServiceW(dce, scmr.SC_MANAGER_CONNECT, service_name)
                result = scmr.hRQueryServiceDisplayW(dce, service_handle)
                print(f'Service Name: {result["ServiceName"]}')
                print(f'Display Name: {result["DisplayName"]}')
                print(f'Type: {result["ServiceType"]}')
                print(f'Start Type: {result["StartType"]}')
                print(f'Binary Path: {result["BinaryPathName"]}')
                scmr.hRCloseServiceHandle(dce, service_handle)
            except Exception as e:
                print(f'Error: {str(e)}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="rpcclient")
    parser.add_argument('host', help='IP address of the target machine')
    parser.add_argument('port', help='Port to use for SMB/RPC connections', type=int)
    args = parser.parse_args()

    rpcclient(args.host, args.port)
