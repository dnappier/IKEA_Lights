'''
Created on Jan 11, 2014

@author: dougnappier
'''

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from actionhandler import ActionHandler
from homelog import Log

class UDPCommandHandler(DatagramProtocol):
    def datagramReceived(self, data, (host, port)): 
        #print "received %r from %s:%d" % (data, host, port)
        self.transport.write(data, (host, port))
        action = ActionHandler()
        stop = action.executeCommand(data)
        if stop:
            reactor.stop()

    def run(self):
        Log().log("Booting up server")
        self.listenPort = reactor.listenUDP(8899, UDPCommandHandler())
        reactor.run()

