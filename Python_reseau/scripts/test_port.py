import sys
import socket
import csv
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
compteur_test=0
compteur_port_ouvert=0
compteur_port_ferme=0
resume=[]
if len(sys.argv)>3:
    ip=sys.argv[1]
    for i in range (2,len(sys.argv)):
        port=int(sys.argv[i])
        etat_port,message=scan_port(ip,port)
        resume.append({"port": port, "msg": message})
        compteur_test+= 1
        if etat_port:
            compteur_port_ouvert+=1
        else:
            compteur_port_ferme+=1
    print(f"Nombre de ports testés : {compteur_test}")
    print(f"Il y a {compteur_port_ouvert} port(s) ouvert(s)")
    print(f"Il y a {compteur_port_ferme} port(s) ferme(s)")
    with open("resultats.csv", "w") as f:
        writer = csv.writer(f) #création de l'objet écrivain
        writer.writerow(["port", "message"])
        for resultat in resume:
            print(f"Port {resultat['port']} : {resultat['msg']}")
            writer.writerow([resultat["port"], resultat["msg"]])
else:
    print("Usage : python3 test_port.py ip (ou localhost) port1 port2 ...")

