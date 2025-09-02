#!/bin/bash
echo "Supprimer les fichier datant de combien de jours"

read jour

if [[ "$jour" =~ ^[0-9]+$ ]];then 
	resultat=$(find . -type f -mtime +$jour)
	if [ -n "$resultat" ];then
		echo "$resultat"
		echo "Souhaitez vous supprimer ces fichier ?  (o/n)"
		read reponse
		if [ "$reponse" = "o" ];then
			find . -type f -mtime +$jour -delete
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
