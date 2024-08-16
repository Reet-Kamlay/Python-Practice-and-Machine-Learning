def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx
@greet
def hello():
    print("Hello World")
def add(a,b):
    print(a+b)
hello()
greet(add)(1,2)