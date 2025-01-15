import os

while True:
    path = input(r"Bitte geben Sie einen gültigen Pfad ein (z. B. C:\Ordner\Datei) oder ende zum Beenden: ").strip()

    if path.lower() == "ende":  # Beenden
            print("Das Programm wird beendet.")
            break
    # Normiere den Pfad
    path = os.path.normpath(path)

    def data_structure(path):
        if not os.path.exists(path):
            print("The Path does not exist.")
            return None
        names = os.listdir(path)
        sorted_names = sorted(names, key=len, reverse=True)
        dictan = {}
        for data in sorted_names:
            data_path = os.path.join(path, data)
            if os.path.isfile(data_path):
                size = os.path.getsize(data_path)
                dictan[data] = size
        filtert = {k: v for k, v in dictan.items() if k.endswith('.txt')}
        return filtert

    filtered_dict = data_structure(path)
    if filtered_dict is not None:
        print("\n ".join([f"{key}: {value}" for key, value in filtered_dict.items()]))