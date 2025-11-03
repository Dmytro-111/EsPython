stringa = "abdadca"
frequenza = {}
for lettera in stringa:
    if lettera in frequenza:
        frequenza[lettera] += 1
    else:
        frequenza[lettera] = 1

print(frequenza)
