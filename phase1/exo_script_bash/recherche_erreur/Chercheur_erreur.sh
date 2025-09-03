#!/bin/bash

log=test.log

echo "Il y a $(grep -i error $log | wc -l) erreurs dans le fichier $log"
