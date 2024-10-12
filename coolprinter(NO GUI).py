import time
alp="abcdefghijklmnopqrstuvwxyz"
res=''
inp=input("Enter the string that you want to print with coolness: ")
j=0
while(len(res)!=len(inp)):
    if(inp[j]==' '):
        res=res+' '
        j+=1
    for i in alp:
        if i==inp[j]:
            res=res+i
            print(res)
            j+=1
            break
        else:
            time.sleep(0.07)
            print(res+i)