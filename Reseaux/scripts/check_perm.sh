#!/bin/bash

echo " Choississez un fichier :"
read fichier

if [ -f "$fichier" ];then
	ls -l "$fichier"
	echo "Souhaitez vous changez les permissions de ce fichier ? (o/n)"
	read reponse
	reponse=${reponse,,}
	if [ $reponse = "o" ]; then
		echo "Quel permission voulait vous lui donner ? "
		echo "644 ( lisible par tous, modifiable par l'utilisateur ), 755 ( executable par tous le monde ), 700 ( fichier privé )"
		read choix
		case $choix in
			644|755|700)chmod $choix $fichier
			echo "Permissions changées" ;;
			*) echo "Entrez un nombre valide" ;;
		esac
	elif [ $reponse = "n" ]; then
		echo "Permissions inchangées"
	else
		echo "Entrez une réponse valide"
	fi
else
	echo "Fichier inexistant"
fi
