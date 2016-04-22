#!/usr/bin/env python

import time,sys,telnetlib,socket
def print_output (string):
  print string

def telnet_login(session, device):
  output = ''
  try:
    session.read_until('sername:', device['telnet_timeout'])
    time.sleep(1)
    session.write(device['username'] + '\n')
    session.read_until('word:', device['telnet_timeout']) 
    time.sleep(1)
    session.write(device['password'] + '\n')
    time.sleep(1)
    output = session.read_until("uthentication failed", device['telnet_timeout'])
  except socket.timeout:
    sys.exit("Connection Timed Out")
  if not output:
    sys.exit("Authentication Failure")
  else:
    print "Terminal Login Complete"

def telnet_send_command(session, cmd):
  output = ''
  try:
    cmd.rstrip()
    session.write(cmd + '\n')
    time.sleep(1)
    output = session.read_very_eager()
  except socket.timeout:
    sys.exit("Connection Timed Out")
  return (output)

def telnet_close(session):
  print "Closing Telnet Session \n"
  session.close()

def telnet_create(device):
  print "Opening Telnet Session \n"
  try:
    telnet = telnetlib.Telnet(device['ip'], device['telnet_port'], device['telnet_timeout'])
  except socket.timeout:
    sys.exit("Connection Timed Out")
  return(telnet)

if __name__ == "__main__":
  pynet_rtr1 = {'ip':'50.76.53.27','username':'pyclass','password':'88newclass','telnet_port':23,'telnet_timeout':10}
  cmd = "show ip interface brief"
  telnet_session = telnet_create(pynet_rtr1)
  telnet_login(telnet_session, pynet_rtr1)
  interfaces = telnet_send_command(telnet_session, cmd)
  print_output(interfaces)
  telnet_close(telnet_session)



