n=int(input("Enter the no of rows: "))
k=1
for i in range(1,n+1):
    for i in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()