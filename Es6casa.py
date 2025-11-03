li = ['a', 'b', 'd', 'a', 'd', 'c', 'a']
frequenza = {}
for lettera in li:
    if lettera in frequenza:
        frequenza[lettera] += 1
    else:
        frequenza[lettera] = 1

print(frequenza)
