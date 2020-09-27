print("enter the text file name where the code is kept(no need to add .txt):",end='')
name=input()
name+=".txt"
try:
    aslkdjhfaskdjhf=open(name,'r')
except:
    print("error\n please check the file name(do not add .txt at the end)")
    print("\npress enter to exit...")
    a=input()
    exit()
code=""
for i in aslkdjhfaskdjhf:
    code+=i
print(code)     
exec(code)
print("\npress enter to exit...")
a=input()	
aslkdjhfaskdjhf.close()
