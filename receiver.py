import os
import sys
import time

ipkharej = sys.argv[1]
os.system("ip tunnel add tun6to4 mode sit ttl 254 remote {}".format(ipkharej))
os.system("ip link set dev tun6to4 up")
os.system("ip addr add fc01::1/64 dev tun6to4")
os.system("ip tunnel add gre1 mode ip6gre remote fc01::2 local fc01::1")
os.system("ip link set gre1 up")
os.system("ip addr add 10.10.15.1/30 dev gre1")
os.system("ip route add default via 10.10.15.2 table 4")
os.system("sysctl net.ipv4.ip_forward=1")
os.system("iptables -t nat -A PREROUTING -p tcp --dport 22 -j DNAT --to-destination 10.10.15.1")
os.system("iptables -t nat -A PREROUTING -j DNAT --to-destination 10.10.15.2")
os.system("iptables -t nat -A POSTROUTING -j MASQUERADE")
os.system("cat /dev/null > ~/.bash_history")
os.system("rm -rf receiver.py")
