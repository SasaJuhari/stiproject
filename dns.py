#!usr/bin/python

import vymgmt

def createdns(name, eth):
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
	vyos.login()
	vyos.configure()
	vyos.set("service dns forwarding name-server %s" %(name))
	vyos.set("service dns forwarding  listen-on %s" %(eth))
	vyos.commit()
	vyos.save()
	vyos.exit()

def readdns():
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
        vyos.login()
	vyos.configure()
	print (vyos.run_op_mode_command("show dns forwarding nameservers"))
	y = vyos.run_op_mode_command("show dns forwarding nameservers")
	vyos.exit()
	vyos.logout()
	return y

def deldns(name):
	vyos = vymgmt.Router('192.168.0.1', 'vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
        vyos.delete("service dns forwarding name-server %s" %(name))
	vyos.commit()
	vyos.save()


def updatedns(name, name1):
	vyos = vymgmt.Router('192.168.0.1','vyos', password='vyos', port=22)
        vyos.login()
        vyos.configure()
	vyos.delete("service dns forwarding name-server %s" %(name))
	vyos.set("service dns forwarding name-server %s" %(name1))
	vyos.commit()
	vyos.save()
	vyos.exit()
	vyos.logout()

