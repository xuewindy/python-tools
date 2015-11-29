'''
filenam log_campuse_net.py
fun :log the bupt net work

'''
import urllib2,re,cookielib,urllib
import regex
username = raw_input('username:')
pwd = raw_input('password:')
url='http://10.3.8.211/'
#username='2014140268'
#pwd='103030'
cookie=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.addheaders.append(('Cookie','myusername='+username+';username='+username+'; smartdot='+str(pwd)+'; pwd='+str(pwd)))
urllib2.install_opener(opener)
resp = urllib2.urlopen(url)
respinfo=resp.info()

#generate a post data
postdata=urllib.urlencode(
			{'DDDDD':str(username),
			'upass':str(pwd),
			'savePWD':'0',
			'0MKKey':''})

#print postdata;

req = urllib2.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0')
resp=urllib2.urlopen(req)
info = resp.info()
content = resp.read()
succ_confirm='You have successfully logged into our system'
if(succ_confirm in content):#log success get again and acquire data
	print 'logging successfully'	
	req = urllib2.Request(url)
	resp = urllib2.urlopen(req)
	content = resp.read()
	time,flow,fee = regex.dataproc(content)
	#regex.dataproc(content);
	print 'time:'+time
	print 'flow:'+flow
	print 'fee:'+fee




