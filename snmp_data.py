from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()
 
errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('Public'),
    cmdgen.UdpTransportTarget(('ip_Address', 161)),
    '1.3.6.1.2.1.17.7.1.2.2.1.2'    #OID МАК на порту Vlana
)
 
if errorIndication:
    print(errorIndication)
else:
    if errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBindTable[-1][int(errorIndex)-1] or '?'
            )
        )
    else:
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
               if   len(val.prettyPrint()) <= 3:  #Отсекаем транковые МАК-и.
                    #print('%s ::: %s ::: %s' % (name.prettyPrint().split(".")[8], name.prettyPrint().split(".")[9:14], val.prettyPrint())) # vlan, mac, port
                    vlan = name.prettyPrint().split(".")[8]
                    mac = name.prettyPrint().split(".")[9:14]
                    port = val.prettyPrint()
                    print(vlan, mac, port)
