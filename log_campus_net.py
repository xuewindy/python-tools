'''
filenam log_campuse_net.py
fun :log the bupt net work

'''
import urllib2,re,cookielib,urllib
import regex
class log_campuse:
    username = ''#username# raw_input('username:')
    pwd = ''#raw_input('password:')
    url = 'http://10.3.8.211/'
    def __init__(self,username,pwd):
        #return
        self.username = username
        self.pwd = pwd
#username='2014140268'
#pwd='103030'
    def getresp(self):
        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        opener.addheaders.append(('Cookie','myusername='+self.username+';username='+self.username+'; smartdot='+str(self.pwd)+'; pwd='+str(self.pwd)))
        urllib2.install_opener(opener)
        resp = urllib2.urlopen(self.url)
        respinfo = resp.info()

#generate a post data
        postdata=urllib.urlencode(
                    {'DDDDD':str(self.username),
                    'upass':str(self.pwd),
                    'savePWD':'0',
                    '0MKKey':''})

#print postdata;

        req = urllib2.Request(self.url,postdata)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:40.0) Gecko/20100101 Firefox/40.0')
        resp=urllib2.urlopen(req)
        info = resp.info()
        content = resp.read()
        return content
    def checkresp(self,content):
        succ_confirm='You have successfully logged into our system'
        failed_confirm='Ivalid account or password'
        if(succ_confirm in content):#log success get again and acquire data
            print 'logging successfully'	
            req = urllib2.Request(self.url)
            resp = urllib2.urlopen(req)
            content = resp.read()
            time,flow,fee = regex.dataproc(content)
                #regex.dataproc(content);
            print 'time:'+time+' Min'
            print 'flow:'+flow+' Kb'
            print 'fee:'+fee +''
        if(failed_confirm in content):
            print failed_confirm

if __name__ =='__main__':
    username = raw_input('username:')
    pwd = raw_input('password:')
    log = log_campuse(username,pwd)
    content = log.getresp()
    log.checkresp(content)


