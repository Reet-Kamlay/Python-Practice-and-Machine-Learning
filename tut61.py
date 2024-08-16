n1=int(input("Enter the number: "))
n2=int(input("Enter the number: "))
sum=0
count=0
for i in range(n1,n2+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        sum+=i
print(sum)