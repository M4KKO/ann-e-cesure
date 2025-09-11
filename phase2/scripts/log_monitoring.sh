#!/bin/bash

echo "Entrez un fichier log à analyser"
read fichier
if [ -f "$fichier" ]; then
	echo "Entrez un mot à retrouver (error, fail...)"
	read mot_a_trouver
	if [ -n "$mot_a_trouver" ];then
		nb=$(grep -i "$mot_a_trouver" "$fichier" | wc -l)
		echo "il y a $nb fois le mot $mot_a_trouver dans le fichier $fichier"
		echo "Voulez vous activer le suivi en temps réel du fichier ? (o/n)"
		read reponse
		reponse=${reponse,,}
		if [ "$reponse" = "o" ]; then
			echo "Suivi activé (ctrl+c pour arreter)"
			tail -f "$fichier" | grep --line-buffered -i "$mot_a_trouver" #--line-buffered pour qu'il sorte les lignes des qu elles arrivent sans attendre 
		elif [ "$reponse" = "n" ]; then
			echo "Suivi non activé"
		else
			echo "rentrez une reponse valide"
		fi
	else
		echo "Entrez un mot"
	fi
else
	echo "Entrez un fichier existant"
fi
