nums = [x for x in range(1000000)]
print(nums[:5])

nums = (x for x in range(1000000))
print(next(nums))
print(next(nums))

def myGen():
    yield 1
    yield 2
    yield 3

gen = myGen() 

print(next(gen))
print(next(gen))
print(next(gen))

def countTo(n):
    num = 1 
    while num <= n:
        yield num 
        num += 1

for val in countTo(5):
    print(val)


def infiniteNums():
    num = 0 
    while True:
        yield num
        num += 1
