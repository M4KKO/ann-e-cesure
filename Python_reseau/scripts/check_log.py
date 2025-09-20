import re
from collections import Counter
liste_ip=[]
with open("/var/log/auth.log") as f:
	for line in f:
		if "Failed password" in line:
			parties=line.split()
			ip=parties[parties.index("from")+1] #on prends l'index juste apres le from car apres from il y a l'ip
			liste_ip.append(ip)
compte = Counter(liste_ip)
print(compte.most_common(3))

