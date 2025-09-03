#!/bin/bash

log=test.log

echo "Il y a $(grep -i error $log | wc -l) erreurs dans le fichier $log" #wc -l sert a compter les lignes, le -i sert a prendre en compte malgré majuscules
