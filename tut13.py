p=int(input("Enetr the value of principal amount: "))
t=int(input("Enter the time you want to keep the money for: "))
if(p<200000):
    r=10
    s=(p*r*t)/100
    print("The simple interest with 10% interest rate: ",s)
elif(p>=200000 and p<=100000):
    r=12
    s=(p*r*t)/100
    print("The simple interest with 12% interest rate: ",s)
else:
    r=15
    s=(p*r*t)/100
    print("The simple interest with 15% interest rate: ",s)
