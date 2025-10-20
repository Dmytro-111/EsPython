n=int(1)
i=int(0)
somma=int(0)
while n!=0:
    n=input("Inserisci un numero ")
    if n!=0:
        somma+=n
        i+=1

print(f"La somma dei valori è {somma}")
media=float(somma/i)
print(f"La media dei valori vale {media}")
    