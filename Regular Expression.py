import re
p = re.compile("sushi")
m = p.search("i love sushi")
if(m):
    print(m.group())
else:
    print("not found")
    
#Second code:-

import re
text = input("enter a string:")
p = re.compile("sushi")
f=open("text.txt",'w')
f.write(text)
f.close()
f=open("text.txt",'r')
m = p.search(f.read())
if(m):
    print(m.group())
else:
    print("not found")



