import subprocess  
from datetime import datetime 
timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
droit=subprocess.run(["ls -l /etc/passwd /etc/shadow"], shell=True, capture_output=True, text=True)
ports_ouvert=subprocess.run(["ss -tulnp"], shell=True, capture_output=True, text=True)
processus=subprocess.run(["ps aux --sort=-%mem | head -n 5"], shell=True, capture_output=True, text=True)
date_fichier=datetime.now().strftime("%Y-%m-%d")
nom_fichier="audit_" + date_fichier + ".log"
with open(nom_fichier, "w") as f:
    f.write(f"{timestamp}\n")
    f.write(f"Ports ouverts : \n {ports_ouvert.stdout}\n --------------------------\n")
    f.write(f"Les 5 processus qui prennent le plus de mémoire : \n{processus.stdout}\n --------------------------\n")
    f.write(f"Droits des fichiers critiques : \n{droit.stdout}\n --------------------------\n")
