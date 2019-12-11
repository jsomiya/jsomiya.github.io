l=['xyxyx', 'ababa', '1221', '34567', 'fghj', '34143']
l1=[]
for i in range(len(l)):
    x=l[i]
    reverse(x)
    
def reverse(x):
    a=x[::-1]
    if (l[i]==a):
        l1.append(a)

print (l1)
