
import re
import os
import sys
import time
import yaml
import shlex
import argparse
import subprocess


class CMD(object):

    def __init__(self):
        usage = "Usage: use --help for further information"
        description = "Nmap Scanner"
        parser = argparse.ArgumentParser(description = description, usage = usage)

        parser.add_argument('-c', '--config', dest = 'config', action = 'store', help = 'Configuration File', required = True)
        self.__args = parser.parse_args()

        self.__nmap_cmd_path = "/usr/bin/nmap"
        self.__hydra_cmd_path = "/usr/bin/hydra"
        self.__arpscan_cmd_path = "/usr/sbin/arp-scan"

        self.__ip_regex  = re.compile("([0-9]{1,3}\.){3}[0-9]+")


    def __run_cmd(self, cmd):
 
        """
        cmd = ['ls -la /tmp']
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

        for line in iter(proc.stdout.readline, ''):
            print line[:-1]
        """

        cmd_list = shlex.split(cmd)

        proc = subprocess.Popen(cmd_list, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
        out, err = proc.communicate()

        if proc.returncode == 0:
            return out
        else:
            return None

    

    def __parse_yaml(self, config_file):
    
        try:    
            with open(config_file, 'r') as stream:
                config_values = yaml.safe_load(stream)    
                return config_values
        except Exception, err:
            print >> sys.stderr, "Error: '{0}'".format(err)
            sys.exit(1)


    def _run(self):

        config_file =  self.__args.config
        values = self.__parse_yaml(config_file)
        
        username_file = values['General']['Username']
        password_file = values['General']['Password']

        for is_file_exists in  (username_file, password_file, self.__arpscan_cmd_path, self.__nmap_cmd_path, self.__hydra_cmd_path):
            if not os.path.exists(is_file_exists):
                print >> sys.stderr, "File: '{0}' Doesn't Exists !!!".format(is_file_exists)
                sys.exit(2)
        
        interface = values['General']['Interface']

        ip_list = []

        arp_cmd = "{0} -l -I {1}".format(self.__arpscan_cmd_path, interface)
        arp_cmd_result = self.__run_cmd(arp_cmd)
        for line in arp_cmd_result.split("\n"):
            if re.match(self.__ip_regex, line):
                ip = line.strip().split()[0]
                ip_list.append(ip)

        print ip_list

##
### Main
##      

if __name__ == "__main__":

    cmd = CMD()
    cmd._run()

    sys.exit(0)

    """

    print out
    """
