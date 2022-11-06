import ipaddress
import random
import sys
from scapy.all import ICMP, IP, sr1,sr,TCP, send
import scapy.all as scapy

#bron voor hostdiscovery https://www.geeksforgeeks.org/network-scanning-using-scapy-module-python/ 

def is_network(adress):
    try:
        network = ipaddress.ip_network(adress)
        return True
    except ValueError:
        return False

request = scapy.ARP()

if len(sys.argv) > 1:
    request.pdst = sys.argv[1]
else:
    request.pdst = input(b"geef een netwerk range in het formaat (192.168.1.1/24) of een ip adress: ")

if is_network(request.pdst):

    broadcast = scapy.Ether() 
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'

    request_broadcast = broadcast / request
    clients = scapy.srp(request_broadcast, timeout = 1)[0]
    for element in clients:
        print(element[1].psrc + "      " + element[1].hwsrc)
else: 
    print("geef een netwerk range in het formaat (192.168.1.1/24)")
    sys.exit()

#SERVICE DISCOVERY
exit = input("wil je verder naar service discovery (poort scan) voor de gevonden hosts? (y/n): ")
if exit == "y":
    #uitleg per poort: https://opensource.com/article/18/10/common-network-ports 
    port_range = port_range = [21,22, 23,25,53, 80,110,119,123,143,161,194, 443]
    for hosts in clients:
        host = hosts[1].psrc
        print(host)
        for dst_port in port_range:
            src_port = random.randint(1025,65534)
            resp = sr1(
            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
            verbose=0,
        )

        if resp is None:
            print(f"{host}:{dst_port} is filtered (silently dropped).")

        elif(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):
                # Send a gratuitous RST to close the connection
                send_rst = sr(
                    IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
                    timeout=1,
                    verbose=0,
                )
                print(f"{host}:{dst_port} is open.")

            elif (resp.getlayer(TCP).flags == 0x14):
                print(f"{host}:{dst_port} is closed.")

        elif(resp.haslayer(ICMP)):
            if(
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
            ):
                print(f"{host}:{dst_port} is filtered (silently dropped).")

#REMOTE OS DETECTIE
seq = 12345
sport = 1040
dport = 80

ip_packet = IP(dst='192.168.1.59')
syn_packet = TCP(sport=sport, dport=dport, flags='S', seq=seq)

packet = ip_packet/syn_packet
synack_response = sr1(packet)

next_seq = seq + 1
my_ack = synack_response.seq + 1

ack_packet = TCP(sport=sport, dport=dport, flags='A', seq=next_seq, ack=my_ack)

send(ip_packet/ack_packet)

payload_packet = TCP(sport=sport, dport=dport, flags='', seq=next_seq)
payload = "this is a test"
send(ip_packet/payload_packet/payload)
