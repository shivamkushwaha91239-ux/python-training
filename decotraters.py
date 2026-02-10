def greet (fx):
    def mfx(*args ,**kwargs):
        print("Good Morning" )
        fx(*args ,**kwargs)
        print("Have a nice day!")
    return mfx
@greet
def Hello():
    print("Hello World!")
#greet(hello)()  same as @greet and hello()
Hello()

@greet
def add(a,b):
    print(a+b)
#greet(add)(2,3)  same as @greet and add(2,3)
add(2,3)  