
# Funktion zur Zählung der Vokale
def count_characters(text):
    characters = {}
    symbols = {}
    for character in text:
        if character.isalpha() and character in "AEIOUaeiou":  # Nur Vokale prüfen
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
        else :
            if not character.isalnum():  # Kein Buchstabe und keine Zahl
                if character in symbols:
                    symbols[character] += 1
                else:
                    symbols[character] = 1   
                 
    total_count = sum(characters.values())
    total_count_s = sum(symbols.values())     
    
    uppercase_count = sum(value for key, value in characters.items() if key.isupper())
    lowercase_count = sum(value for key, value in characters.items() if key.islower())

    if len(characters) > 0:
        print(f"Du hast insgesamt {uppercase_count} Vokale in Großbuchstaben und {lowercase_count} Vokale in Kleinbuchstaben eingegeben.") 
        print(f"Das sind insgesamt {total_count} Vokale.")
        print("Detaillierte Vokalhäufigkeit:")
        for character, count in characters.items():
            print(f"Der Buchstabe {character} kommt {count} mal vor.")
            
    if len(symbols) > 0:
        print(f"Du hast insgesamt {total_count_s} Sonderzeichen eingegeben.")
        print("Detaillierte Sonderzeichenzählung:")
        for symbol, count in symbols.items():
            print(f"Das Zeichen '{symbol}' kommt {count} mal vor.")


    return characters,symbols, uppercase_count, lowercase_count, total_count,total_count_s

while True:
    # Eingabe vom Benutzer
    text = input("Geben Sie den Text ein (oder Ende zum Beenden): ").strip()

    # Beendigungsabfrage direkt nach der Eingabe
    if text.lower() == "ende":
        print("Programm wird beendet.")
        break

    # Leere Eingabe prüfen
    if not text:  # Leere Eingabe
        print("Leere Eingabe ist nicht erlaubt. Bitte erneut eingeben.")
        continue  # Zur nächsten Iteration springen

    # Funktion ausführen
    count_characters(text)