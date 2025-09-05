#!/bin/bash

echo "Entrez un processus valide :"

read nom_processus

ps aux | grep "$nom_processus" | grep -v grep #on exclue le grep des processus
if [ $? -eq 0 ]; then
	echo "Processus trouvé"
	echo "Voulez vous l'arrêter ? (o/n)"
	read reponse
	reponse=${reponse,,} #met la reponse en minuscule
	if [ $reponse = "o" ]; then
		pkill "$nom_processus"
		echo "Processus arrêté"
	elif [ $reponse = "n" ]; then
		echo "Processus conservé"
	else
		echo "Entrez une réponse valide"
	fi
else
	echo "Processus introuvable"
fi
