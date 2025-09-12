#!/bin/bash
echo "Voici un chat local entre deux machines"
echo "Voulez vous être serveur ou client ?"
read reponse
reponse=${reponse,,}
if [ "$reponse" = "serveur" ]; then
	echo "Quel port voulez vous ouvrir ?"
	read port_serveur
	if ! [[ "$port_serveur" =~ ^[0-9]+$ ]]; then
		echo "Veuillez choisir un nombre pour le port choisi"
	elif [ "$port_serveur" -lt 1024 ]; then #on évite les ports réservés
		echo "Veuillez choisir un port libre (>1023)"
	else
		echo "ouverture du port $port_serveur "
                nc -l -p "$port_serveur"
	fi
elif [ "$reponse" = "client" ]; then
	echo "Sur quel port voulez vous vous connecter ? "
	read port_choisi
	if ! [[ "$port_choisi" =~ ^[0-9]+$ ]]; then
		echo "Veuillez choisir un nombre pour le port choisi"
	elif [ "$port_choisi" -lt 1024 ]; then #on évite les ports réservés
                echo "Veuillez choisir un port libre (>1023)"
	else
		echo "Saisissez l'adresse ip du serveur (ou localhost si le serveur et le client sont sur la même machine"
		read ip
		ip=${ip,,}
		if [[ "$ip" = "localhost" || "$ip" =~ ^[0-9]{1,3}(\.[0-9]{1,3}){3}$ ]]; then
			echo "connection en cours"
			nc "$ip" "$port_choisi"
			echo "connection établi"
		else
			echo "Entrez une reponse valide"
		fi
	fi
else
	echo "Entrez une reponse valide"
fi

