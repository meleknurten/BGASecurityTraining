#!/usr/bin/env bash

if [ ! $# -eq 2 ]
then
	echo "Usage: $0 <interface | count>"
	exit 1
fi


function check_interface () {

	interface2=$1
	ifconfig -a | grep -E "^[a-zA-Z0-9]+:" | cut -d ":" -f1 | while read line
	do	
		echo "$line" | grep -q "$interface2"
		if [ $? -eq 0 ]
		then
			return 0
		fi
	done

	return 1
}


function get_ip () {

	interface3="$1"
	ip_addr=$(ifconfig  "$interface3" | grep inet | awk '{print $2}')

	echo "$ip_addr"

}

interface=$1
count=$2

check_interface "$interface" 

if [ $count -eq 0 ]
then
	while [ 1 ]
	do
		old_ip="`get_ip "$interface"`"
		if [ -z "$old_ip" ]
		then
			break
		fi
	done
else

	for loop in `seq 1 $count`
	do
		old_ip="`get_ip "$interface"`"
		echo "Old_Ip:  $old_ip"

		macchanger  -r "$interface"  >/dev/null  2>/dev/null
		if [ $? -eq 0 ]
		then
			dhclient "$interface" >/dev/null 2>/dev/null
			new_ip="`get_ip "$interface"`"

			echo "New_Ip: $new_ip"
		else
			echo "ERROR : Mac Error"
			exit 2
		fi

		echo ""
	done
fi












