#!/usr/bin/python

import os, sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel, info, debug
from mininet.node import Host, RemoteController

class TreeTopo( Topo ):
    "Tree topology"

    def build( self ):
        # Read ring.in
        # Load configuration of Hosts, Switches, and Links
        # You can write other functions as you need.
        with open('ring.in', 'r') as file:
            num_hosts, num_switches, num_links = map(int, file.readline().strip().split(' '))
            for _ in range(num_links):
                dev1, dev2 = file.readline().strip().split(',')
                if dev1[0] == 'h':
                    self.addHost(dev1)
                else:
                    sconfig = {'dpid': "%016x" % int(dev1[1:])}
                    self.addSwitch(dev1, **sconfig)
                if dev2[0] == 'h':
                    self.addHost(dev2)
                else:
                    sconfig = {'dpid': "%016x" % int(dev2[1:])}
                    self.addSwitch(dev2, **sconfig)
                self.addLink(dev1, dev2)

        # Add hosts
        # > self.addHost('h%d' % [HOST NUMBER])

        # Add switches
        # > sconfig = {'dpid': "%016x" % [SWITCH NUMBER]}
        # > self.addSwitch('s%d' % [SWITCH NUMBER], **sconfig)

        # Add links
        # > self.addLink([HOST1], [HOST2])
        
                    
topos = { 'sdnip' : ( lambda: TreeTopo() ) }

if __name__ == '__main__':
    sys.path.insert(1, '/home/sdn/onos/topos')
    from onosnet import run
    run( TreeTopo() )