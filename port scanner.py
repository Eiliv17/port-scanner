import socket
import asyncio


portmax = 65535
portmin = 1


def portscanner(ipaddr):
    tcpactiveports = []
    udpactiveports = []

    socket.setdefaulttimeout(1)

    for port in range(portmin, portmax):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((ipaddr,port))
                tcpactiveports.append(port)
            except:
                print("Port {} not opened".format(port))
                continue
        
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            try:
                s.connect((ipaddr,port))
                udpactiveports.append(port)
            except:
                print("Port {} not opened".format(port))
                continue
    
    return tcpactiveports, udpactiveports


ipaddress = input("Insert the ip address for the port scan: ")

tcpports, udpports = portscanner(ipaddress)

print("Active tcp ports {}".format(tcpports))
print("Active udp ports {}".format(udpports))