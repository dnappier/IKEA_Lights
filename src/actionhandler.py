'''
Created on Jan 11, 2014

@author: dougnappier
'''

from log import Log


class ActionHandler(object):
    def executeCommand(self, cmd, **kwargs):
        return cmd