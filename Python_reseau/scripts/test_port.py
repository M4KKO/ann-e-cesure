import sys
import socket

if len(sys.argv)==3:
    ip=sys.argv[1]
    port=int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        print("Connexion réussie, le port est ouvert")
    except ConnectionRefusedError:
        print("Port fermé (connexion refusée)")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
    finally:
         s.close()
else:
    print("Usage : python3 test_port.py ip (ou localhost) port")
