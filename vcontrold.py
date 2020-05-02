import time
import datetime
import telnetlib
import re

class vclient(object):

    def __init__(self, host, port):
        self.telnet_client = telnetlib.Telnet(host, port)
        #self.command = cmd

    def publish(self, cmd):
        #vclient(HOST, PORT)
        for v in vals:
            self.telnet_client.read_until('vctrld>')
            self.telnet_client.write(v + '\n')
            print(self.telnet_client.read_some())
            #out = self.telnet_client.read_until('Grad Celsius')
            #print(out)


HOST = '192.168.168.16' # vcontrold telnet host
PORT = '3002' # vcontrold port

vals = ['getAussentemperatur', 'getWWTempIst']
vals2 = {'command': 'getAussentemperatur', 'command': 'getWWTempIst'}

vc = vclient(HOST, PORT)

vc.publish(vals)

#for v in vals:
#    vc.publish(v)
