import random
from datetime import datetime

def password_generator():
    while True:
        print("Wie lang soll das Passwort sein? Min 12 - Max 40 Zeichen!")
        lenght = input("Geben Sie den Wert ein oder 'Ende' zum Beenden: ")
        
        if lenght.lower() == "ende":
            print("Das Programm wird beendet.")
            break  # Beende die Schleife und die Funktion
        
        if not lenght.isdigit():  # Eingabe ist keine Zahl
            print("Bitte geben Sie eine Zahl ein.")
            continue  # Zurück zum Anfang der Schleife
        
        lenght = int(lenght)  # Konvertiere in eine Ganzzahl
        if lenght < 12 or lenght > 40:  # Prüfe, ob die Zahl im erlaubten Bereich liegt
            print("Bitte geben Sie eine Zahl zwischen 12 und 40 ein.")
            continue
        
        # Generiere das Passwort
        chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        chars_k = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!§$%&/()=?*#")
        result = []
        now = datetime.now()
        answer = input("Möchten Sie Sonderzeichen in Ihrem Passwort haben? (ja/nein): ")
        
        for _ in range(lenght): 
            if answer.lower() == "ja":  # Wenn der Benutzer Sonderzeichen haben möchte
                result.append(random.choice(chars_k))
            else:
                result.append(random.choice(chars))
        # Mische die Zeichen in der Liste
        random.shuffle(result)
        
        # Kombiniere die Zeichen zu einem String
        password = ''.join(result)
        print(f"Es ist {now}.")  # Gebe das aktuelle Datum und die Uhrzeit aus
        print(f"Ihr generiertes Passwort: {password}")  # Gebe das Passwort aus

password_generator()
