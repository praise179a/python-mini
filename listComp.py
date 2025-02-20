#create lists

label = ["Even" if x%2 ==0 else "Odd" for x in range(10)]
print(label)

pairs = [(x,y) for x in [1,2] for y in [3,4]]
print(pairs)

def fahr(cel):
    return (cel * 9/5) + 32

temps = [0,10,20]
temps_fahr = [fahr(temp) for temp in temps]
print(temps_fahr)