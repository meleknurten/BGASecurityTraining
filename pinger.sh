#!/usr/bin/env bash

if [ ! $# -eq 1 ]
then
	echo "Usage: $0 <ip/cidr>"
	exit 1
fi

subnet=$1

echo "$subnet" | grep -Eq "^([0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]+$"
if [ ! $? -eq 0 ]
then
	echo "Usage: $0 <IP>"
	exit 2
fi

nmap -n -sL "$subnet" | grep -E "^Nmap scan report" | cut -d " " -f5 | while read ip
do
	ping "$ip" -c 1 -w 1 |grep -Eq "^64 bytes from"
	if [ $? -eq 0 ]
	then
		echo "$ip : UP"
	else
		echo "$ip : DOWN"
	fi
done
