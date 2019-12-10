n = int(input())
def reverse(a) :
    rev=0
    while(a>0):
        r=a%10
        rev=(rev*10)+r
        a=a//10
    return rev

def reversesum(x,y):
        s=reverse(int(x))
        t=reverse(int(y))
        sum1=s+t
        u=reverse(sum1)
        return u
    
for i in range(n) :
    a=input()
    c=a.split()
    print (c)
    j=reversesum(c[0],c[1])
    print (j)
