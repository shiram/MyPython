import sys
from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, AUTO_BIND_NO_TLS, SUBTREE
from ldap3.core.exceptions import LDAPCursorError

import xlwt

#DN = username@example.com, secret=password, un=username

# One of those scripts
#

server_name = 'HOST'
domain_name = 'DOMAIN'
user_name = 'ldap@dlap.co.in'
password = 'XXXXX'

server = Server(server_name, get_info=ALL)
conn = Connection(server, user= user_name, password=password, auto_bind=True)
# say rickman.co.ne 
# dc = rickman
# dc = co
# dc = ne
# OU = Object to be authenticated, ie computer, user, service, bot etc
conn.search('OU=Users, dc=rickman,dc=co,dc=ne'.format(domain_name), '(&(objectCategory=user))', attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])
print("**************************ALL ATTRIBUTES**************************")
print("")
print(conn.entries)

print("*******************SOME ATTTR*********************************")
format_string = '{:25} {:30} {:10} {:10} {:20} {}'
print(format_string.format('User', 'UserPrincipalName','FirstName', 'LastName', 'Physical Office', 'Description'))

data_all = []

for e in conn.entries:
	try:

		data_in = []
		name = e.name
		data_in.append(str(name))
		p_name = e.userPrincipalName
		data_in.append(str(p_name))
		fname = e.givenName
		data_in.append(str(fname))
		lname = e.sn
		data_in.append(str(lname))
		office = e.physicalDeliveryOfficeName
		data_in.append(str(office))
		desc = e.description
		data_in.append(str(desc))
		mem = e.distinguishedName


		data_all.append(data_in)
	except LDAPCursorError:
		desc = ""
		dnn = ""
		name = ""
		p_name = ""
		fname = ""
		lname = ""
		office = ""

