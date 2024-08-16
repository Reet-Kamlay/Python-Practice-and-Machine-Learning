prime_count=0
composite_count=0
while True:
    n=int(input("Enter the number: "))
    if(n==-1):
        break
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1
    if(count==2):
        prime_count+=1
    else:
        composite_count+=1
print(f"The numbers of prime numbers are {prime_count}")
print(f"The numbers of composite numbers are {composite_count}")