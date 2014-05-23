__author__ = 'dougnappier'

from udpcommandhandler import UDPCommandHandler

PORT = 8899

ch = UDPCommandHandler(PORT)
ch.run()