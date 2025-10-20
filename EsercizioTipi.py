while True:
    tipo=str(input("Inserisci la scala di temperatura che vuoi adottare tra Celsius C, Kelvin K e Fahreneit F "))
    numero=float(input("Inserisci la temperatura"))
    match tipo:
        case "C":
            tK=numero-273.15
            tF=numero*1.8+32
            
            print(f"Il tuo valore in Kelvin è {tK} , in Fahreneit è {tF}")
        case "K":
            tC=numero+273.15
            tF=(numero+273.15)*1.8+32
            
            print(f"Il tuo valore in Celsius è {tC} , in Fahreneit è {tF}")
        case "F":
            tC=(numero-32)/1.8
            tK=tC+273.15
            
            print(f"Il tuo valore in Celsius è {tC} , in Fahreneit è {tF}")
        case _:
            print("Non hai scelto un tipo corretto. Riprova")
            
