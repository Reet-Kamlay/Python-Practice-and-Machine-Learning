r=int(input("Enter the no of rows: "))
R=range(1,2*r-1,2)
k=r
for i in R:
    print(" "*(r-k)+"*"*(i),end=" ")
    k=k+1
    print()