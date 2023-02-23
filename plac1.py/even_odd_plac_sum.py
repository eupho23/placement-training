n=int(input())
odd_sum=0
even_sum=0
cnt=0
while(n>0):
    
    cnt+=1
    m=n%10
    n=n//10 # // is imp 
    
   
    
    if(cnt%2==0): # % pakaram // etta moojal akum ta
        
        even_sum += m
    else:
        odd_sum += m
print("even places sum is:")
print(even_sum)
print("odd places sum is:")
print(odd_sum)