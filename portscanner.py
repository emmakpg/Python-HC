from socket import *
import optparse
from threading import *
from termcolor import colored, cprint
from colorama import init
init(autoreset = True)

def portScan(host, ports):
    try:
        tgtIP = gethostbyname(host)
    except:
        print(f'Unknown host {host}')
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'[*] Scan Results for: {tgtName[0]}')
    except:
         print(f'[*] Scan Results for: {tgtIP[0]}')
    setdefaulttimeout(1)

    for port in ports:
        t = Thread(target= pscan, args=(host, int(port)))
        t.start()

def pscan(host, port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))    
        print(colored(f"[+]Port {port} is open",'yellow'))
    except:
        print(colored(f"\n[-]Port {port} is closed", 'red'))
    finally:
        sock.close()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest = 'tgtHost', type='string', help = 'Specify target host')
    parser.add_option('-p', dest = 'tgtPort', type='string', help = 'Specify target port(s) separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if(tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == "__main__":
    main()
