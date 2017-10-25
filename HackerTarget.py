#/!python
#!/usr/bin/python

import requests
import time
import sys

time.sleep(.1)

R = '\033[91m'  # red
G = '\033[92m'  # green
B = '\033[94m'  # blue

print ("""\n%s_________| HackerTarget API Caller |__________________________________
%s                  _  _   _______  .__  __    __ 
               __| || |__\      \ |__|/  |__/  |______    _____ 
               \   __   //   |   \|  \   __\   __\__  \  /     \ 
    ./c0d3d By  |  ||  |/    |    \  ||  |  |  |  / __ \|  Y Y  \\
               /_  ~~  _\____|__  /__||__|  |__| (____  /__|_|  /
                 |_||_|         \/                    \/      \/ \n
%s__________________________________________| %shttps://IAmNir.ml%s |_______""" % (B, G, B, G, B))

def main():

	assert __file__ == sys.argv[0]

	try:
		cmd = sys.argv[1]
		tar = sys.argv[2]

	except IndexError:
		print ("""%s 
 Usage: ./hta.py <options> <target>
 
 %sOptions:%s

 	1) DNS Tools :
		 	reversedns
		 	zonetransfer
		 	dnslookup
		 	hostsearch
		 	findshareddns

	2) IP Tools  :
		 	nmap
		 	reverseiplookup
		 	subnetcalc

	3) Web Tools :
		 	httpheaders
		 	pagelinks
%s______________________________________________________________________%s
	
                    Powered By "%swww.hackertarget.com%s" 
%s______________________________________________________________________
			""" % (R, B, G, B, G, R, G, B))
		sys.exit(2)

	payload = ("https://api.hackertarget.com/{}/?q={}".format(cmd, tar))
	r = requests.get(url = payload)
	output = r.text
	print ("%s" %(G))
	print(output)
	print("""%s______________________________________________________________________%s
	
                    Powered By "%swww.hackertarget.com%s" 
%s______________________________________________________________________
			""" % (B, G, R, G, B))
if __name__ == '__main__':
	main()
