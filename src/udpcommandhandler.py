'''
Created on Jan 11, 2014

@author: dougnappier
'''

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from actionhandler import ActionHandler
from log import Log

class UDPCommandHandler(DatagramProtocol):

    def __init__(self, port):
        self.port = port

    def datagramReceived(self, data, (host, port)): 
        print "received %r from %s:%d" % (data, host, port)
        self.transport.write(data, (host, port))
        action = ActionHandler()
        result = action.executeCommand(data)
        Log().log(result)

    def run(self):
        Log().log("Booting up server")
        self.listenPort = reactor.listenUDP(self.port, UDPCommandHandler(self.port))
        reactor.run()

