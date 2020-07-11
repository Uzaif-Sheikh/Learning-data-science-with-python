try:
  f=open("text.txt",'r')      #read the file text.text
except FileNotFoundError:
    s="hello world"           #if file is not found then read f as s
else:
    s=f.read()                #read file as s
finally:
    print(s)                #finally print s variable
