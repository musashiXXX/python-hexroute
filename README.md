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

    Generate or parse a DHCP option 249 hexadecimal string

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

