import sys
import socket
def scan_port(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        message="connexion réussie, le port est ouvert"
    except ConnectionRefusedError:
        message="port fermé (connexion refusée)"
    except Exception :
        message="erreur inattendue"
    finally:
            s.close()
            return message

if len(sys.argv)>3:
    ip=sys.argv[1]
    for i in range (2,len(sys.argv)):
        port=int(sys.argv[i])
        message=scan_port(ip,port)
        print(f"Port:{port}",message)
else:
    print("Usage : python3 test_port.py ip (ou localhost) port1 port2 ...")
