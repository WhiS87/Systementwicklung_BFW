import string

def count_characters():
    while True:
        text = input("Geben Sie den Text ein (oder '1' zum Beenden): ").strip()

        if text == "1":  # Beenden
            print("Das Programm wird beendet.")
            break

        # Satzzeichen und Leerzeichen entfernen
        filtered_text = ''.join(char for char in text if char.isalpha())

        if not filtered_text:  # Prüfen, ob nach Filterung noch Zeichen übrig sind
            print("Ungültige Eingabe! Bitte gib einen Text ein!")
            continue

        filtered_text = filtered_text.upper()  # In Großbuchstaben umwandeln
        characters = {}  # Dictionary für Buchstabenhäufigkeit

        # Zähle Buchstaben
        for character in filtered_text:
            characters[character] = characters.get(character, 0) + 1

        # Berechne die Gesamtzahl der Buchstaben
        total_count = sum(characters.values())

        # Füge die prozentuale Berechnung hinzu
        percentages = {
            char: (count / total_count) * 100
            for char, count in characters.items()
        }

        # Ergebnisse ausgeben
        print(f"\nDu hast insgesamt {total_count} Buchstaben eingegeben (ohne Leer- und Satzzeichen).")
        print("Prozentuale Verteilung:")
        for char, percent in percentages.items():
            print(f"Der Buchstabe {char} kommt {characters[char]} mal vor. Das sind {percent:.2f}%.")
        print("\n")  # Neue Zeile für bessere Lesbarkeit


# Hauptprogramm
count_characters()

