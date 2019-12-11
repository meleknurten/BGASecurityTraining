#!/bin/bash

msf_resource_file=$(mktemp /tmp/$USER.XXXXXX)

echo "workspace test" >> $msf_resource_file
echo "spool /tmp/msf-result.dat" >> $msf_resource_file
echo "use auxiliary/scanner/http/dir_listing" >> $msf_resource_file
echo "services -p 443 -R" >> $msf_resource_file
echo "set THREADS 10" >> $msf_resource_file
echo "run" >> $msf_resource_file
echo "exit" >> $msf_resource_file


msfconsole -r "$msf_resource_file"  2>/dev/null >/dev/null

cat /tmp/msf-result.dat | grep "+" | mail -s "TEST RESULTS" sonuc@example.com

rm -rf "$msf_result_file" "/tmp/msf-result.dat" 2>/dev/null
