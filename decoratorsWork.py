def greet():
    return "Hey friend!"

def callFunc(func):
    return func()

print(callFunc(greet))


def outerFunc():
    def innerFunc():
        return "Hi from inner"
    return innerFunc

myFunc = outerFunc()
print(myFunc)