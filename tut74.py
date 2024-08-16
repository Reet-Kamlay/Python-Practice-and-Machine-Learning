import math
cnum=0
num=0
l1=[]
l2=[]
n1=int(input("Enter the first value: "))
n2=int(input("Enter the second value: "))
while(1):
    dec1=input("Who are you: ")
    if(dec1=="Alice"):
        dec2=int(input("Enter the number which you want to replace with gcd of current numbers: "))
        if(dec2==n1):
            n1=math.gcd(n1,n2)
            cnum=n1
            num=n2
        elif(dec2==n2):
            n2=math.gcd(n1,n2)
            cnum=n2
            num=n1
        else:
            print("Wrong Value")
    elif(dec1=="Bob"):
        dec2=int(input("Enter the number which you want to replace with lcm of current numbers: "))
        if(dec2==n1):
            n1=math.lcm(n1,n2)
            cnum=n1
            num=n2
        elif(dec2==n2):
            n2=math.lcm(n1,n2)
            cnum=n2
            num=n1
        else:
            print("Wrong Value")
    print("The value of n1 is: ",n1)
    print("The value of n2 is: ",n2)
    if(cnum==n1 and num==n2):
        l1.append(n1)
        l2.append(n2)
    elif(cnum==n2 and num==n1):
        l2.append(n2)
        l1.append(n1)
    dec3=input("Do you want to exit: ")
    if(dec3=="Yes"):
        print("The minimum sum of the numbers is ",min(l1)+min(l2))
        exit(1)
    else:
        continue
    

