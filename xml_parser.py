>>> import xml.etree.ElementTree as ET
>>> result_file = "NMAP-SCAN-RESULT.xml"
>>> dom = ET.parse(result_file)
>>> root = dom.getroot()
>>> for host in root.findall("host"):
...     for address in host.findall("address"):
...             if not address.get("addrtype") == "mac":
...                     print address.get("addr")
...     for ports in host.findall("ports"):
...             for port in ports.findall('port'):
...                     print port.get('portid')
...     print "----"

