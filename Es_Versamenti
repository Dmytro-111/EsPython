partecipanti= {}

while True:
    nome = input("Come ti chiami? ")
    rata = int(input("Quanto hai pagato? "))

    if nome in partecipanti:
        partecipanti[nome] += rata
    else:
        partecipanti[nome] = rata

    print("Totale pagato a persona: ")
    print(partecipanti)

    totale = sum(partecipanti.values())
    print("La somma totale di tutti versamenti:", totale)

    scelta = input("Vuoi aggiungere qualcosa? (si/no): ")
    if scelta == "no":
        break
