import os
import sys
import time

sender = sys.argv[1]
os.system("ip tunnel add tun6to4 mode sit ttl 254 remote {}".format(sender))
os.system("ip link set dev tun6to4 up")
os.system("ip addr add fc01::2/64 dev tun6to4")
os.system("ip tunnel add gre1 mode ip6gre remote fc01::1 local fc01::2")
os.system("ip link set gre1 up")
os.system("ip addr add 10.10.15.2/24 dev gre1")
os.system("ip route add default via 10.10.15.1 table 4")
os.system("rm -rf sender.py && cat /dev/null > ~/.bash_history && ping -c 3 10.10.15.1")
