import sys
import socket
import csv
import json
from threading import Thread
def scan_port(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip,port))
        message="connexion réussie, le port est ouvert"
        port_ouvert=True
    except ConnectionRefusedError:
        message="port fermé (connexion refusée)"
        port_ouvert=False
    except Exception :
        message="erreur inattendue"
        port_ouvert=False
    finally:
            s.close()
            return (port_ouvert, message)
def worker(ip,port):
    etat_port,message=scan_port(ip,port)
    resume.append({"port": port, "msg": message, "open": etat_port})

resume=[]
threads = []
if len(sys.argv)>3:
    ip=sys.argv[1]
    for i in range (2,len(sys.argv)):
        port=int(sys.argv[i])
        t = Thread(target=worker, args=(ip, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    compteur_test=len(resume)
    compteur_port_ouvert = sum(1 for r in resume if r["open"])
    compteur_port_ferme=compteur_test-compteur_port_ouvert
    print(f"Nombre de ports testés : {compteur_test}")
    print(f"Il y a {compteur_port_ouvert} port(s) ouvert(s)")
    print(f"Il y a {compteur_port_ferme} port(s) ferme(s)")
    with open("resultats.json", "w") as f:
        json.dump(resume, f, indent=4)
    with open("resultats.csv", "w") as f:
        writer = csv.writer(f) #création de l'objet écrivain
        writer.writerow(["port", "message"])
        for resultat in resume:
            print(f"Port {resultat['port']} : {resultat['msg']}")
            writer.writerow([resultat["port"], resultat["msg"]])
else:
    print("Usage : python3 test_port.py ip (ou localhost) port1 port2 ...")
