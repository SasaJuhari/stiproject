
#!/usr/bin/python 

import vymgmt

def createdhcp(type):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.set("service dhcp-server shared-network-name 'LAN' authoritative %s" %(type))
	vyos.commit()
	vyos.save()
	vyos.exit()

def readdhcp():
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	print(vyos.run_conf_mode_command("show service dhcp"))
	x = vyos.run_conf_mode_command("show service dhcp")
	vyos.exit()
	vyos.logout()
	return x

def deldhcp(type):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.delete("service dhcp-server shared-network-name 'LAN' authoritative %s" % (type))
	vyos.commit()
	vyos.save()

def updatedhcp(type, type1):
	vyos = vymgmt.Router( '192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	vyos.delete("service dhcp-server shared-network-name 'LAN' authoritative %s" %(type))
	vyos.set("service dhcp-server shared-network-name 'LAN' authoritative %s" %(type1))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()
