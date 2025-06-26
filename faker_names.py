_______________________________________
# Génération de données factices
# liste de contacs
# Date 26-06-2025
# Auteur: Locad Dacol 
_______________________________________


import pandas as pd
from faker import Faker


# Initialisation de Faker
fake = Faker("fr_FR")


# Nom de fichier avec la date concaténée
filename = f"contacts_data_{current_date}.csv"

# Génération de données factices
data = {
    "Nom": [fake.name() for _ in range(100)],
    "Adresse": [fake.address() for _ in range(100)],
    "Email": [fake.email() for _ in range(100)],
    "Téléphone": [fake.phone_number() for _ in range(100)],
    "Compétences": [fake.pystr(min_chars=5, max_chars=10) for _ in range(100)],
}

# Création d'un DataFrame pandas
df = pd.DataFrame(data)

# Écriture dans un fichier Excel
df.to_excel("enregistrements_factices.xlsx", index=False)

print("Fichier Excel généré avec succès.")
