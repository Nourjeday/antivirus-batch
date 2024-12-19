import os

def scan_directories(path="."):
    """Scanne les répertoires pour trouver les fichiers .bat."""
    bat_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".bat"):
                bat_files.append(os.path.join(root, file))
    return bat_files
directory="C:/Users"
if __name__ == "__main__":
    files = scan_directories(directory)
    print(f"Fichiers .bat trouvés : {files}")

dangerous_commands = ["del", "format", "shutdown", "rmdir"]
def analyze_bat_file(file_path):
    """Analyse le contenu d'un fichier .bat pour des commandes dangereuses."""
    try:
        with open(file_path, "r") as file:
            content = file.read()
            for command in dangerous_commands:
                if command in content:
                    return True  # Fichier suspect
    except Exception as e:
        print(f"Erreur lors de la lecture de {file_path}: {e}")
    return False
if __name__ == "__main__":
    files = scan_directories(directory)
    suspects = []

    for file in files:
        if analyze_bat_file(file):
            suspects.append(file)

    if suspects:
        print(f"Fichiers suspects détectés : {suspects}")
    else:
        print("Aucun fichier suspect détecté.")

def generate_report(suspects):
    """Génère un rapport des fichiers suspects."""
    with open("scan_report.txt", "w") as report:
        for file in suspects:
            report.write(f"Fichier suspect : {file}\n")
    print("Rapport généré : scan_report.txt")

if __name__ == "__main__":
    files = scan_directories("C:/Users")
    suspects = []

    for file in files:
        if analyze_bat_file(file):
            suspects.append(file)

    if suspects:
        print(f"Fichiers suspects détectés : {suspects}")
        generate_report(suspects)
    else:
        print("Aucun fichier suspect détecté.")

import winreg as reg
import os

def add_to_startup(file_path):
    """Ajoute le script au démarrage de Windows."""
    try:
        key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as registry:
            reg.SetValueEx(registry, "AntiVirusBatch", 0, reg.REG_SZ, file_path)
        print("Ajouté au démarrage.")
    except Exception as e:
        print(f"Erreur lors de l'ajout au démarrage : {e}")
if __name__ == "__main__":
    exe_path = os.path.abspath("dist/antivirus.exe")
    add_to_startup(exe_path)
