n = int(input())
#python stops-end point is a place before specified point
for i in range (n-1,-n,-1):
    for j in range(1,abs(i)+2):
        print("*",end="")
    print()
