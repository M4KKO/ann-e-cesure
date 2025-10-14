import subprocess  
from datetime import datetime
import os
timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
droit=subprocess.run(["ls -l /etc/passwd /etc/shadow"], shell=True, capture_output=True, text=True)
ports_ouvert=subprocess.run(["ss -tulnp"], shell=True, capture_output=True, text=True)
processus=subprocess.run(["ps aux --sort=-%mem | head -n 5"], shell=True, capture_output=True, text=True)

base_dir = os.path.dirname(__file__)
dossier_fichier = os.path.join(base_dir, "..", "reports")
os.makedirs(dossier_fichier, exist_ok=True)

date_fichier=datetime.now().strftime("%Y-%m-%d")
nom_fichier="audit_" + date_fichier + ".log"
fichier=os.path.join(dossier_fichier, nom_fichier)

with open(fichier, "w") as f:
    f.write(f"{timestamp}\n")
    f.write(f"Ports ouverts : \n {ports_ouvert.stdout}\n --------------------------\n")
    f.write(f"Les 5 processus qui prennent le plus de mémoire : \n{processus.stdout}\n --------------------------\n")
    f.write(f"Droits des fichiers critiques : \n{droit.stdout}\n --------------------------\n")
