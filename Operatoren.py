def operatoren (Zahl_1, Zahl_2):
    i = 0
    print("Wilkommen beim Programm Operatoren")

    while i < 1:
        while True : 
            Zahl_1 = input("Geben sie die erste Zahl ein. Oder Ende zum Beenden. ")
            if Zahl_1.isdigit(): # Prüfen, ob es eine Zahl ist
                Zahl_1 = int(Zahl_1) # Konvertierung in Integer
            elif Zahl_1.lower() == "ende":
                print("Das Programm wird beendet.")
                i = 1
                break  
            else :
                print("Ungültiger Wert. Bitte geben Sie eine Zahl ein!")

        

            while True : # Schleife läuft, bis gültige Eingabe erfolgt
                Zahl_2 = input("Geben sie die Zweite Zahl ein. ")
                if Zahl_2.isdigit():  # Prüfen, ob es eine Zahl ist
                    Zahl_2 = int(Zahl_2) # Konvertierung in Integer
                    break
                else :
                    print("Ungültiger Wert. Bitte geben Sie eine Zahl ein!")
                
            print("Das addierte Ergebniss der Zahlen ist " + str(Zahl_1 + Zahl_2) + ".")
            print(f"Das subtrahierte Ergebniss der Zahlen ist  {Zahl_1 - Zahl_2}.")
            print("Das multiplizierte Ergebniss der Zahlen ist " + str(Zahl_1 * Zahl_2) + ".")
            print(f"Das dividierte Ergebniss der Zahlen ist {Zahl_1 / Zahl_2}.")
    
    
operatoren(0,0)