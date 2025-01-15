# Version: 1.0
def main():
    while True:  
        print("""
        Willkommen im Systementwicklungstool.  
        Drücken Sie:
        1 - Vokalzählung
        2 - Operatoren
        3 - Häufigkeitsanalyse
        4 - Datenstrukturen
        5 - Passwortgenerator  
        0 - Beenden
        """)
        auswahl = input("Wählen Sie Ihr gewünschtes Programm aus: ")
        if auswahl == "1":
            import Vocale
        elif auswahl == "2":
            import Operatoren
        elif auswahl == "3":
            import Haeufigkeitsanalyse
        elif auswahl == "4":
            import Datenstrukturen
        elif auswahl == "5":
            import PasswordGenerator
        elif auswahl == "0":
            print("Das Programm wird beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte erneut eingeben.")
            continue    


if __name__ == "__main__":
    main()