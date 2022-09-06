#!/usr/bin/env python

import ipaddress, argparse, itertools

def hexroute(routes: list, uppercase=True) -> str:
    '''
       Takes a list of lists or tuples in the form ('network/prefix', 'gateway_ip')
       and returns a DHCP option 121/249 hex string

       >>> hexroute([('192.168.100.0/24','192.168.100.1')])
       '18:C0:A8:64:C0:A8:64:01'
       >>> hexroute([('172.16.0.0/24', '172.16.0.1')])
       '18:AC:10:00:AC:10:00:01'
       >>> hexroute([('10.1.1.10/8', '10.254.254.1')])
       '08:0A:0A:FE:FE:01'
       >>> hexroute([('192.168.1.0/23','192.168.0.1'), ('192.168.0.0/23', '192.168.0.1')])
       '17:C0:A8:00:C0:A8:00:01'
    '''

    hex = []
    networks = []
    for route in routes:
        net = ipaddress.IPv4Network(route[0], strict=False)
        if net in networks:
            continue
        prefix = net.prefixlen
        net_address = [int(i) for i in str(net.network_address).split('.')]
        gateway_address = [int(i) for i in str(route[1]).split('.')]
        octets = []
        if prefix > 0:
            octets.append(net_address[0])
        if prefix > 8:
            octets.append(net_address[1])
        if prefix > 16:
            octets.append(net_address[2])
        if prefix > 24:
            octets.append(net_address[3])
        container = [prefix]
        container += octets
        container += gateway_address
        hex += ['{:02X}'.format(i) for i in container]
        networks.append(net)
    
    opt249str = ':'.join(hex)
    if not uppercase:
        return opt249str.lower()
    return opt249str

def hexroute_reverse(hex_string):
    '''
       Takes a hexadecimal DHCP option 249 string and returns the IPv4 networks and their gateways

       >>> hexroute_reverse('18:C0:A8:64:C0:A8:64:01')
       [(IPv4Network('192.168.100.0/24'), IPv4Address('192.168.100.1'))]
       >>> hexroute_reverse('18:AC:10:00:AC:10:00:01')
       [(IPv4Network('172.16.0.0/24'), IPv4Address('172.16.0.1'))]
       >>> hexroute_reverse('08:0A:0A:FE:FE:01')
       [(IPv4Network('10.0.0.0/8'), IPv4Address('10.254.254.1'))]
       >>> hexroute_reverse('17:C0:A8:00:C0:A8:00:01')
       [(IPv4Network('192.168.0.0/23'), IPv4Address('192.168.0.1'))]
    '''

    decimal_vals = [int(i, 16) for i in hex_string.split(':')]
    routes = []
    while len(decimal_vals):
        next = 0
        subnet = decimal_vals.pop(0)
        for i in (0, 8, 16, 24):
                if subnet > i:
                        next += 1
        subnet_octets = decimal_vals[:next]
        while len(subnet_octets) < 4:
                subnet_octets.append(0)
        network = ipaddress.IPv4Network('.'.join([str(i) for i in subnet_octets]) + '/{}'.format(subnet), strict=False)
        del decimal_vals[:next]
        gateway_address = decimal_vals[:4]
        gateway = ipaddress.IPv4Address('.'.join([str(i) for i in gateway_address]))
        del decimal_vals[:4]
        routes.append((network, gateway))
    return routes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Generate or parse a DHCP option 249 hexadecimal string')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-r',
        '--route',
        help='Specify a network/gateway pair',
        metavar=('192.168.0.0/16', '192.168.0.1'),
        nargs=2,
        action='append'
    )
    group.add_argument(
        '-R',
        '--reverse',
        help='Convert an option 121/249 hex string into IPv4 network/route pairs',
        metavar='18:C0:A8:64:C0:A8:64:01'
    )
    args = parser.parse_args()
    if args.route:
        print(hexroute(args.route))
    if args.reverse:
        print(hexroute_reverse(args.reverse))
