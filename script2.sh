#!/bin/bash

nmap -n -sL 217.68.216.0/20 | grep -E "^Nmap scan report" | cut -d " " -f5 | while read ip
do 
        result=$(dig -x "$ip" +short)
        if [ ! -z "$result" ]
        then 
                echo "$result"
        fi
done | grep -Ev "(notused|other209)"


#if [ -f "$FILE" ]
#if [ -d "$DIR" ]
#if [ $result -eq 10 ] ==
#if [ $result -lt 10 ] <=
#if [ $result -gt 10 ] >=

