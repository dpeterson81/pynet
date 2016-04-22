#!/usr/bin/env python
'''
Write a script that connects to the lab pynet-rtr1, logins, and executes the
'show ip int brief' command.
'''

import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class telnet_session:
    def __init__(self, ip_addr, username, password,  port, timeout): 
        self.ip = ip_addr
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.session = telnetlib.Telnet(self.ip, self.port, self.timeout)
    
    #def telnet_connect(self):
        '''
        #Establish telnet connection
        '''
        #try:
            #self.session = telnetlib.Telnet(self.ip, self.username, self.password, self.port,self.timeout )
        #except socket.timeout:
            #sys.exit("Connection timed-out")
    
    def close(self):
        self.session.close()

    def send_command(self, cmd):
        '''
        Send a command down the telnet channel
        Return the response
        '''
        cmd = cmd.rstrip()
        self.session.write(cmd + '\n')
        time.sleep(1)
        return self.session.read_very_eager()

    def login(self):
        '''
        Login to network device
        '''
        output = self.session.read_until("sername:", self.timeout)
        self.session.write(self.username + '\n')
        output += self.session.read_until("ssword:", self.timeout)
        self.session.write(self.password + '\n')
        return output

    def disable_paging(self, paging_cmd='terminal length 0'):
        '''
        Disable the paging of output (i.e. --More--)
        '''
        return self.send_command(paging_cmd)


def main():
    '''
    Write a script that connects to the lab pynet-rtr1, logins, and executes the
    'show ip int brief' command.
    '''
    ip_addr = raw_input("IP address: ")
    ip_addr = ip_addr.strip()
    username = 'pyclass'
    password = getpass.getpass()

    remote_conn = telnet_session(ip_addr, username, password, TELNET_PORT, TELNET_TIMEOUT)
    #remote_conn.telnet_connect()
    output = remote_conn.login()

    time.sleep(1)
    remote_conn.session.read_very_eager()
    remote_conn.disable_paging()

    output = remote_conn.send_command('show ip int brief')

    print "\n\n"
    print output
    print "\n\n"

    remote_conn.close()

if __name__ == "__main__":
    main()
