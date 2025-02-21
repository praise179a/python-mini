#list comprehensions 

squares = []
for x in range(5):
    squares.append(x**2)


squares = [x**2 for x in range(5)]
#list_name = [expression for item in iterable]

evens = [j for j in range(10) if x%2 ==0 ]


def fahr(celsius):
    return (celsius * 9/5) + 32

temps = [0,10,20,30]
temps_fahr = [fahr(temp) for temp in temps]
print(temps_fahr)


#[1.2] [3,4]
pairs = [(x,y) for x in [1,2] for y in [3,4]]

pairs = []
for x in [1,2]:
    for y in [3,4]:
        pairs.append((x,y))


#lambdas  function 
def double(x):
    return x*2
double(5)

double = lambda x: x *2 
double(5)

#lambda arguments: expression

maxVal = lambda a,b:  a if a > b else b
square = list(filter(lambda x: x%2 ==0,[1,2,4]))


pairs = [(1,3), (2,2), (3,1)]
sortPairs = sorted(pairs, key=lambda x: x[1])