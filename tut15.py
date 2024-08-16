a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
for i in range(1,(a+b)):
    if(a%i==0 and b%i==0):
        c=i
print(c)
