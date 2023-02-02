from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()
 
errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.nextCmd(
    cmdgen.CommunityData('kppublic'),
    cmdgen.UdpTransportTarget(('10.43.64.77', 161)),
    '1.3.6.1.2.1.17.7.1.2.2.1.2'    
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
               if   val.prettyPrint() != '8193':
                    print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
