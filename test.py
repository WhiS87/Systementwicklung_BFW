import os

# Variablen zur Speicherung der Namen
path = "C:\\Users\\HartmanM\\OneDrive - Berufsförderungswerk Köln gGmbH\\Dokumente\\Testdaten"
#path = r"C:\Users\HartmanM\OneDrive - Berufsförderungswerk Köln gGmbH\Dokumente\Testdaten"

# Funktion zum Auflisten der Dateien
def list_files(path):
    #for file in os.listdir(path):
    #    print(file)
    # Alle Dateinamen in einer Liste speichern und zurückgeben
    return os.listdir(path)

# Funktion zum Sortieren der Dateien nach Länge (absteigend)
def sort_names(names):
    # Ausgabe und Sortierung der Liste nach Länge (absteigend)
    #print("\n" .join(sorted(names, key=len, reverse=True)))
    # Rückgabe der sortierten Liste
    return sorted(names, key=len, reverse=True)
    
# Funktion zum Speichern von Dateinamen und Größen in einem Dictionary
def in_dict(sorted_names, path):
    file_dict = {}  # Vermeidet Verwendung von geschützten Namen wie 'dict'

    for data in sorted_names:
        # Kompletter Dateipfad
        data_path = os.path.join(path, data)

        # Nur Dateien betrachten, keine Ordner
        if os.path.isfile(data_path):
            size = os.path.getsize(data_path)  # Größe der Datei in Bytes
            file_dict[data] = size  # Datei und Größe im Dictionary speichern

    # Ausgabe des Dictionaries in Zeilenform
    #for key, value in file_dict.items():
    #    print(f"{key}: {value} Bytes")

    return file_dict  # Rückgabe des erzeugten Dictionaries
    
# Dateien auflisten und sortieren
names = list_files(path)
sorted_names = sort_names(names)
file_dict = in_dict(sorted_names, path)
# Debugging Ausgabe
# print(file_dict)