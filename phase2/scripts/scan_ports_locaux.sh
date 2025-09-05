#!/bin/bash
#Port TCP
rep_tcp=$(ss -tln)
rep_udp=$(ss -uln)
rep_service=$(ss -tulnp)
if [ -n "$rep_tcp" ];then
	echo "Port TCP ouvert:"
	echo "$rep_tcp"
else
	echo "Aucun port TCP ouvert"
fi

if [ -n "$rep_udp" ];then
        echo "Port UDP ouvert:"
        echo "$rep_udp"
else
        echo "Aucun port UDP ouvert"
fi
if [ -n "$rep_service" ];then
        echo "Services détéctés:"
        echo "$rep_service"
else
        echo "Aucun service en écoute"
fi
