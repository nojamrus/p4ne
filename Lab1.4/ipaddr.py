import ipaddress
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self, n='0.0.0.0',p='0'):
        ipaddress.IPv4Network.__init__(self,(n,p),strict=False)

    def key_value(self):
        return "%s/%s" % (int(self.network_address._ip), int(self.netmask._ip) )

def MyFn(s):
    ret=s.key_value()
    return int(ret[-10:])

list_network=[]
for i in range(10):
    for y in range(255):
        list_network.append(IPv4RandomNetwork(random.randint(0x0B000000,0xDF000000), random.randint(8,24)))

new_sort=sorted(list_network,key=MyFn)

for one_new_sort in new_sort:
    print (one_new_sort.key_value())




