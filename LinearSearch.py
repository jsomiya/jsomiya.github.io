t=[1,2,3,4,5,87,34]
x=int(input())
c=0
d=0
for i in range (len(t)):
    if t[i]==x:
        c+=1
        break
    else : 
        d+=1
if c==1 :
    print ("yes")
else :
    print ("no")
