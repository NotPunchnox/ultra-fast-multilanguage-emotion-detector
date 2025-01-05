# Importation des librairies
from transformers import pipeline
import argostranslate.package
import argostranslate.translate
from langdetect import detect
import time

# Chargement du modèle de classification
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
print("Modèle de classification chargé avec succès.")

# Paramètres de traduction
from_code = "fr"
to_code = "en"

# Téléchargement et installation du module de traduction
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(filter(lambda a: a.from_code == from_code and a.to_code == to_code, available_packages))
argostranslate.package.install_from_path(package_to_install.download())
print("Module de traduction installé avec succès.")

# Effacer la console pour une meilleure lisibilité
print('\033[H\033[J')
print("Tous les algorithmes sont prêts. Le programme peut démarrer.\n")

# Démarrage du programme CLI
while True:
    # Demander à l'utilisateur sa requête
    prompt = input("Entrez une phrase : ")

    # Début du timer
    start = time.time()

    # Détection de la langue de la requête
    detected_language = detect(prompt)
    print(f"Langue détectée : {detected_language}")

    # Traduction de la requête vers l'anglais si nécessaire
    if detected_language != "en":
        translated_text = argostranslate.translate.translate(prompt, from_code, to_code)
        print(f"Texte traduit en anglais : {translated_text}")
    else:
        translated_text = prompt
        print("Le texte est déjà en anglais. Traduction ignorée.")

    # Détection des émotions
    output = classifier([translated_text])[0]
    print("Émotions détectées :")
    for emotion in output:
        if emotion['score'] > 0.02:
            print(f"  - {emotion['label']}: {emotion['score']:.2f}")

    # Temps total de l'opération
    duration = time.time() - start
    print(f"Durée totale de l'opération : {duration:.2f} secondes\n")
