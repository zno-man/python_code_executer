print("enter the text file name where the code is kept(no need to add .txt):",end='')
name=input()
name+=".txt"
try:                                                                            #opens the file and handles error
    aslkdjhfaskdjhf=open(name,'r')
except:
    print("error\n please check the file name(do not add .txt at the end)")
    print("\npress enter to exit...")
    a=input()
    exit()
    
code=""
for i in aslkdjhfaskdjhf:
    code+=i                                                                     #gets the code from the file as a single string
print(code)                                                                     #displays the actual code                                                          
exec(code)                                                                      #executes the code
print("\npress enter to exit...")                                               #waits for input/enter key
a=input()	
aslkdjhfaskdjhf.close()
