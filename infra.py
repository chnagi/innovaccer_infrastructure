import sys
import os,numpy
print "Enter source path:(/../) to be cleaned"
sourcepath=raw_input()
print "Enter target path(/../):"
targetpath=raw_input()
path=sourcepath
pat=targetpath
if(os.name=='posix'): # 
        path1='/home/'	
elif(os.name=='nt'):
	path1='C:/User/'	
l=[]
m=[]
e=[]
for root,subdirs,files in os.walk(path1):
	for file in os.listdir(root):
		filepath=os.path.join(root,file)
		size=os.path.getsize(filepath) # getting size in bytes
		print "list of 10 big files with size in MB"
		l.append([(size/float(pow(10,6))),filepath]) # converting to MB
l.sort()
li= l[(len(l)-10):]  # printing top 10 biggest files 
for i in range(len(li)):
	print str(li[i][0])+'MB',str(li[i][1])
# organising files

for root,subdirs,files in os.walk(path):
	for file in os.listdir(root):
		filepath=os.path.join(root,file)
		m.append(filepath)
		path,ext=os.path.splitext(filepath)
		e.append(ext)
		e = list(set(e))
		e_copy=e
for i in range(len(e)):
	if(e[i]==''):
		if not os.path.exists(os.path.join(pat,str(0))):
			os.makedirs(os.path.join(pat,str(0)))
		continue
	else:
		e[i]=e[i].split('.')
		if not os.path.exists(os.path.join(pat,str(e[i][1]))):
			os.makedirs(os.path.join(pat,str(e[i][1])))
for q in m:
	#print q
	path1=q
	path,ext=os.path.splitext(q)
	xpath=pat
	xpath=xpath.split('/')
	q1=q.split('/')
	#print xpath
	s=""
	for i in range(len(xpath)):
                if(xpath[i]!=''):
                        s=s+'/'+xpath[i]
        if(ext=='' and (os.path.exists(q1[len(q1)-1]) is not dir)):
                path2=s+'/'+str(0)+'/'+q1[len(q1)-1]
                os.rename(path1,path2)
        	continue
	        
	for value,item in enumerate(e_copy):
		if(len(item)==2):
			it=item[1]
	#		print item
			item='.'+item[1]
			if(ext==item):
				path2=s+'/'+str(it)+'/'+q1[len(q1)-1]
	#			print path2
				k=os.rename(path1,path2)
				break
			
	
