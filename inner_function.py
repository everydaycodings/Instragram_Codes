def func(n):
    print("Hello functon")

    def func1():
        print("First child function.")

    def func2():
        print("Second child function")
    
    if n == 1:
        return func1()
    else:
        return func2()

func(1)
print("")
print("")


def welcomefunction(function):
    def rfun():
        print("Hello")
        function()
        print("Wellcome")
    return rfun()
    

def rfun2():
    print("everydaycodings")

mydef = welcomefunction(rfun2)
