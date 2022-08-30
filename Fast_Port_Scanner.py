
import pyfiglet
import socket
import threading
import concurrent.futures
import datetime
import argparse


parser = argparse.ArgumentParser(prog='fast.py', usage='%(prog)s [Target] [Port]',epilog="Example: fast.py google.com 1-10000  fast.py github.com all ")
parser.add_argument("target", help = "[target ip]")
parser.add_argument("port", help = "[port] (default = 1-1000)",default=1,  nargs = '?') 
args = parser.parse_args()
ip=args.target
nport=args.port
if nport==1:
        start=1
        end=1000

elif nport== "all":
        start=1
        end=65535
else:
        
        start,end= nport.split("-")
        start= int(start)
        end= int(end)




print("-" * 70)
print("github.com/DoguhanPOLAT")
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

def date_time():
	return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print_lock = threading.Lock()


# translate hostname to IPv4
targetip = socket.gethostbyname(ip)

# For information
print("-" * 70)
print("Scanning Target - {} ({})".format(ip,targetip))
print("Scan started - [{}]".format(date_time()))
print("-" * 70)

print("\n      Ip\t\tPort\t\tState")
print("-" * 55)
#Scaning
def scan(ip,port):
    scanner= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        scanner.connect((ip,port))
        scanner.close()

        with print_lock:
            print("{}\t\t{}\t\tOpen".format(targetip,port))

    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # will scan ports between 1 to 65,535
    for port in range(start,end):
        executor.submit(scan, ip, port + 1)


print("\nScan finished - [{}]".format(date_time()))
print("-" * 70)
