#!/bin/bash
LOG_DIR="/home/noah/annee-cesure/Bash_avance/scripts"
if [[ "$1" = "localhost" || "$1" =~ ^[0-9]{1,3}(\.[0-9]{1,3}){3}$ ]]; then
	if ! [ "$1" = "localhost" ]; then
		ping -c 1 "$1" | tee -a "$LOG_DIR/ping.log"
	fi
	reessaie=0
	while [ "$reessaie" -eq 0 ]; do
		echo "Entrez un port à scanner"
        	echo -e "22 : SSH \n 80 : HTTP \n 443 : HTTPS \n Ou tout autre port (stop pour arreter)"
		read port
		port=${port,,}
		if [[ "$port" =~ ^[0-9]+$ ]]; then
			nc -z -v -w 1 "$1" "$port" 2>&1 | tee -a "$LOG_DIR/ping.log"
		elif [ "$port" = "stop" ]; then
			reessaie=1
		else
			echo "Entrez une reponse valide"
		fi

	done
else
	echo "Usage: ./scan_reseau.sh IP (ou localhost)"
fi
