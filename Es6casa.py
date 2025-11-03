# Data una lista,
# costruire un dizionario che registri la frequenza di ciascun carattere presente in essa
lista = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
frequenze = {}
for carattere in lista:
    if carattere in frequenze:
        frequenze[carattere] += 1
    else:
        frequenze[carattere] = 1
print(frequenze)