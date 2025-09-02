#!/bin/bash
for i in {1..2}
do
	echo "je teste le fichier:  fichier$i.txt"
	if [ -f "fichier$i.txt" ]; then
		mv "fichier$i.txt" "fichier${i}_old.txt"
	else
		echo "Le fichier$i n'existe pas"
	fi
done
