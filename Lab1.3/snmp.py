from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('10.31.70.107', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
)

for varBind in varBinds:
    print (varBind)

resault= nextCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('10.31.70.107', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2') ),  lexicographicMode=False)

for varBind in resault:
    for i in varBind[3]:
        print (i)

