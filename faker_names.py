
# Génération de données factices
# liste de contacs
# Date 26-06-2025
# Auteur: Locad Dacol 

import pandas as pd
from datetime import datetime
from faker import Faker
import os


# === CONFIGURATION ICI ===
EXPORT_FORMAT = "excel"   # 🔁 Change en "excel" si tu veux un .xlsx
NOMBRE_ENREGISTREMENTS = 10
# ==========================

print("Répertoire courant :", os.getcwd())


# Initialisation de Faker
# Génération de données factices
fake = Faker("fr_FR")
data = {
    "Nom": [fake.name() for _ in range(NOMBRE_ENREGISTREMENTS)],
    "Adresse": [fake.address() for _ in range(NOMBRE_ENREGISTREMENTS)],
    "Email": [fake.email() for _ in range(NOMBRE_ENREGISTREMENTS)],
    "Téléphone": [fake.phone_number() for _ in range(NOMBRE_ENREGISTREMENTS)],
    "Compétences": [fake.pystr(min_chars=5, max_chars=10) for _ in range(NOMBRE_ENREGISTREMENTS)],
}

df = pd.DataFrame(data) # Création d'un DataFrame pandas

# Génération du nom de fichier horodaté
current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # format horodaté
base_filename = f"contacts_data_{current_date}"

# Détermination du nom de fichier final
if EXPORT_FORMAT == "csv":
    filename = f"{base_filename}.csv"
elif EXPORT_FORMAT == "excel":
    filename = f"{base_filename}.xlsx"
else:
    raise ValueError("Format non reconnu. Utilise 'csv' ou 'excel'.")

# Affichage
print("Répertoire courant :", os.getcwd())
print("Nom du fichier (complet) :", os.path.abspath(filename))

# Export selon le format choisi
if EXPORT_FORMAT == "csv":
    df.to_csv(filename, index=False)
elif EXPORT_FORMAT == "excel":
    df.to_excel(filename, index=False)


print(f"✅ Fichier {EXPORT_FORMAT.upper()} généré avec succès.")
