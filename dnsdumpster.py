
import re
import requests
import argparse
from fake_useragent import UserAgent

usage = "Usage: use --help for further information"
description = "DnsDumpster"
parser = argparse.ArgumentParser(description = description, usage = usage)

parser.add_argument('-d', '--domain', dest = 'domain', action = 'store', help = 'Domain Name', required = True)

args = parser.parse_args()

domain = args.domain

ua = UserAgent()
headers =  { 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-us,en;q=0.5', 'Accept-Encoding': 'gzip,deflate', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7', 'Keep-Alive': '300', 'Connection': 'keep-alive', 'User-Agent': ua.random, 'Content-Type': 'application/x-www-form-urlencoded' }


headers['Referer'] = 'https://dnsdumpster.com'

url =  'https://dnsdumpster.com'
req = requests.get(url, headers = headers, verify=False, timeout=5)
csrftoken = req.headers['Set-Cookie'].split("=")[1].split(";")[0]

csrfmiddletoken = None

for line in req.text.split("\n"):
     if re.search("name=\"csrfmiddlewaretoken\" value=\"(.*)\"", line):
             csrfmiddletoken = re.search("name=\"csrfmiddlewaretoken\" value=\"(.*)\"", line).groups()[0]
             break

print csrftoken, csrfmiddletoken

data = "csrfmiddlewaretoken={0}&targetip={1}".format(csrfmiddletoken, domain)
cookie = "csrftoken={0}; _ga=GA1.2.1122453016.1576062688; _gid=GA1.2.1474885402.1576062688; _gat=1".format(csrftoken)

post_headers = { 'Host': 'dnsdumpster.com', 'User-Agent': ua.random, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': '112', 'Origin': 'https://dnsdumpster.com', 'DNT': '1', 'Connection': 'close', 'Referer': 'https://dnsdumpster.com/', 'Cookie': cookie, 'Upgrade-Insecure-Requests': '1' }


results = []

req = requests.post(url, data = data, headers = post_headers, verify=False, timeout=10)
for line in req.text.split("\n"):
    if re.search("q=https?://([a-zA-Z0-9\-]+)\.({0})\"".format(domain), line):
        subdomain = re.search("q=https?://([a-zA-Z0-9\-]+)\.({0})\"".format(domain), line).groups()[0]
        results.append(subdomain)        

alive_http_subdomains = []

for line in results:
    http_url = "http://{0}.{1}/".format(line, domain)
    try:
        req = requests.get(http_url, headers = headers, verify=False, timeout=5)
        alive_http_subdomains.append(http_url)
    except:
        pass

    https_url = "https://{0}.{1}/".format(line, domain)
    try:
        req = requests.get(https_url, headers = headers, verify=False, timeout=5)
        alive_http_subdomains.append(https_url)
    except:
        pass

for result in  alive_http_subdomains:
    print result



















        

