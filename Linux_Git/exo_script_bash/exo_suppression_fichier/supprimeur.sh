#!/bin/bash
echo "Supprimer les fichier datant de combien de jours"

read jour

if [[ "$jour" =~ ^[0-9]+$ ]];then #on vérifie si l'entrée utilisateur est bien un nombre 
	resultat=$(find . -type f -mtime +$jour) #on cherche des fichiers datant du nombre de jour de l'entrée utilisateur
	if [ -n "$resultat" ];then #on vérifie  qu'il y ai des fichiers avec ces caractéristiques
		echo "$resultat"
		echo "Souhaitez vous supprimer ces fichier ?  (o/n)"
		read reponse
		if [ "$reponse" = "o" ];then
			find . -type f -mtime +$jour -delete # si l'utilisateur confirme alors on supprime les fichiers
			echo "fichier supprimer"
		elif [ "$reponse" = "n" ];then
			echo "fichier conservé"
		else
			echo "entrez une reponse valide"
		fi
	else
		echo "aucun fichier trouvé"
	fi
else
	echo "Veuillez entrez un nombre valide"
fi
