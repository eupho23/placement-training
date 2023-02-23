n=int(input())
p=n
sum=0
cnt=0
while(n>0):
    cnt+=1
    n=n//10 
n=p
while(n>0):
    m=n%10
    sum += m**cnt
    n=n//10 # // is imp 
print(sum)
if(p==sum):
    print("n is an armstrong num")
else:
    print("n is not")
