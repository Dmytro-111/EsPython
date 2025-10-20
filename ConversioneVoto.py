while True:
    voto=float(input("Inserisci il tuo voto"))
    if(voto>=0 and voto<=6.9):
        print("La tua valutazione è F")
    if(voto>=7.0 and voto<=7.6):
        print("La tua valutazione è D")
    if(voto>=7.7 and voto<=8.4):
        print("La tua valutazione è C")
    if(voto>=8.5 and voto<=9.2):
        print("La tua valutazione è B")
    if(voto>=9.3 and voto<=10):
        print("La tua valutazione è A")
    