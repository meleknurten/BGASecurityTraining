#!/bin/bash

tcpdump -tttnn -r sample.pcap  -c 20 | cut -d ">" -f1  | awk -F " " '{print $3}' | cut -d "." -f1-4 | while read ip
do 
	geo=$(geoiplookup $ip | cut -d ":" -f2 | cut -d " " -f2 | tr -d ",")
	echo "$geo - $ip"
done

