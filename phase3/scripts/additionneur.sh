#!/bin/bash

if [[ "$1" =~ ^[0-9]+$ && "$2" =~ ^[0-9]+$ ]]; then
	somme=$(( $1 + $2 ))
	echo "La somme de $1 et $2 est $somme"
elif [[ -n "$1" && -n "$2" ]]; then
	echo "Seuls les nombres sont acceptés en argument"
else
	echo "Entrez deux nombres en argument"
fi
