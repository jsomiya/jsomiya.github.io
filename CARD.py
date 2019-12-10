n=int(input())
def card(n) :
    while(n>0):
        if (n==1) :
            return 2
        elif (n==2) :
            return 7
        else :
            return (((2*card(n-1))-(card(n-2))+3))
card(n)
