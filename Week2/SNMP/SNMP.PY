#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

mib_dict = { \
    'hostname':'1.3.6.1.2.1.1.5.0', \
    'sys_desc':'1.3.6.1.2.1.1.1.0'  \
    }

#Device Tuple definitions format <device_name> = (<ip>, <community_string>, <port>)
devices = [ \
    ('50.76.53.27', 'galileo',7961), \
    ('50.76.53.27', 'galileo',8061) ]

def get_snmp(device, mib):
    data = snmp_get_oid(device, mib)
    return snmp_extract(data)

if __name__ == "__main__":
    for dev in devices:
        hostname = get_snmp(dev, mib_dict['hostname'])
        print "Hostname: {0}".format(hostname)
        sys_desc= get_snmp(dev, mib_dict['sys_desc'])
        print "System Description:\n {0} \n".format(sys_desc)

