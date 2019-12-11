#!/bin/bash

if [ ! $# -eq 1 ]
then
	echo "Usage: $0 <DIZIN>"
	exit 1
fi

dizin=$1
db_file="/tmp/db.dat"

while [ 1 ]
do
	if [ ! -f "$db_file" ]
	then
		find  "$dizin" > $db_file
	else
		tmp_db_file=$(mktemp /tmp/$USER.XXXXXX)
		find "$dizin" > $tmp_db_file

		diff "$tmp_db_file" "$db_file" | grep -E "<|>"
		rm -rf "$db_file"
		mv "$tmp_db_file" "$db_file"
	fi	
	
	sleep 10	
done
