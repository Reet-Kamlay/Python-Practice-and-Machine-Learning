num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
lcm=0
for i in range(max(num1,num2),(num1*num2)+1,max(num1,num2)):
        while((i%num1)==0 and (i%num2)==0):
            lcm=i
            break
print(f"The lcm of {num1} and {num2} is {lcm}")