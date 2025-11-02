a=int(1)
li=[]

while a!=0:
    a=float(input("inserisci un valore "))
    li.append(a)

pari=0
dispari=1
for num in li:
     if num % 2 == 0:
          pari+=num
     else:
          dispari*=num
print("La tua lista di numeri è: ", li)
print("La somma dei numeri pari è: ", pari)
print("Il prodotto dei numeri dispari è: ", dispari)

    

    
