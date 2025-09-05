#!/bin/bash

echo "Entrez un url valide"

read url

if ping -c 1 $url > /dev/null
then
	echo "Ping réussi"
else
	echo "Ping echoué"
fi

if curl -s --head $url > /dev/null
then
	echo "Le service web est accessible"
else
	echo "Le service web est innacessible"
	curl --head $url
fi
