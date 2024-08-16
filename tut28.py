from functools import reduce
l=[1,2,4,6,4,3]
def filter_function(a):
    return a>2
newl=list(filter(filter_function,l)) 
print(newl)
newl=list(map(lambda x:x*x*x,l))
print(newl)
numbers=[1,2,3,4,5]
def mysum(x,y):
    return x+y 
sum=reduce(mysum,numbers)
print(sum) 