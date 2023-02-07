# `python-hexroute`


## Summary

This is a python version of the original bash `hexroute` script (availble [here](http://www.xrx.ca/hexroute.htm)).


## Installation

Just download and run the script:

    wget https://raw.githubusercontent.com/musashiXXX/python-hexroute/main/hexroute.py
    chmod 755 hexroute.py
    ./hexroute.py


Or install it via `pipenv` to be used as a module:

    pipenv install -e git+https://github.com/musashiXXX/python-hexroute.git#egg=python-hexroute


## Usage

    usage: hexroute.py [-h] (-r 192.168.0.0/16 192.168.0.1 | -R 18:C0:A8:64:C0:A8:64:01)

    Generate or parse a DHCP option 121/249 hexadecimal string

    optional arguments:
      -h, --help            show this help message and exit
      -r 192.168.0.0/16 192.168.0.1, --route 192.168.0.0/16 192.168.0.1
                            Specify a network/gateway pair
      -R 18:C0:A8:64:C0:A8:64:01, --reverse 18:C0:A8:64:C0:A8:64:01
                            Convert an option 121/249 hex string into IPv4 network/route pairs


Generate a hex string:

    ./hexroute.py -r 10.10.10.0/24 192.168.0.1 -r 172.16.0.0/12 192.168.0.1
    18:0A:0A:0A:C0:A8:00:01:0C:AC:10:C0:A8:00:01


Parse a hex string:

    ./hexroute.py -R '18:0A:0A:0A:C0:A8:00:01:0C:AC:10:C0:A8:00:01'
    [(IPv4Network('10.10.10.0/24'), IPv4Address('192.168.0.1')), (IPv4Network('172.16.0.0/12'), IPv4Address('192.168.0.1'))]


## References

 * [RFC 3442](https://www.rfc-editor.org/rfc/rfc3442.html)
 * [2.2.8 DHCPv4 Option Code 249 (0xF9) - Microsoft Classless Static Route Option](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-dhcpe/f9c19c79-1c7f-4746-b555-0c0fc523f3f9)
 * [How to push static routes from the Palo Alto Networks DHCP Server](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClEICA0)
   * > Linux will accept routes learned through DHCP Option 121 and Option 249. if it doesn not, set option `classless_static_routes` in `/etc/dhcpcd.conf`. If both options are configured, Linux will prefer routes defined by DHCP Option 121.
