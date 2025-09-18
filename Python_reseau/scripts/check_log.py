compteur_failed=0
with open ("var/log/auth.log") as f:
	for line in f:
		if "Failed password" in line:
			compteur_failed+=1
print(f"Il y a {compteur_failed} tentative(s) de connexion echoué")
