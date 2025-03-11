from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import Controller, RemoteController, OVSSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel, info

class CustomTopo(Topo):
    def build(self):
        # Add switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')  # Server

        # Add links (with bandwidth control)
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s3)
        self.addLink(h6, s3)
        self.addLink(h7, s4)

        self.addLink(s1, s2, bw=100)   # S1-S2: 100 Mbps
        self.addLink(s2, s3, bw=50)    # S2-S3: 50 Mbps
        self.addLink(s3, s4, bw=100)   # S3-S4: 100 Mbps

if __name__ == '__main__':
    setLogLevel('info')
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=Controller, switch=OVSSwitch, link=TCLink)
    net.start()
    info("Network started\n")
    net.pingAll()
    net.stop()
