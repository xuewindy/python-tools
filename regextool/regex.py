import re

#f = open('data.html')
def dataproc(content):
	match=[]
	m=[]
	pr= re.compile('time=\'(.*?)\'.*?flow=\'(.*?)\'.*?fee=\'(.*?)\'')
	m = pr.findall(content)
	#mt= pr.findall(cont)
	match.append(m)
	return match[0][0][0],match[0][0][1],match[0][0][2]
