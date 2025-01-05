# Importation des libs
from transformers import pipeline
import argostranslate.package
import argostranslate.translate
import time

# Chargement du modèle de classification
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
print("model launched")

from_code = "fr"
to_code = "en"

# Téléchargement et installation du module de traduction
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(filter(lambda a: a.from_code == from_code and a.to_code == to_code, available_packages))
argostranslate.package.install_from_path(package_to_install.download())

# Clear console
print('\033[H\033[J')
print("Chargement des alrogithmes terminé avec succès.\n")


# Démarrage du programme cli
while True:
    
    # Demander à l'utilisateur sa requete
    prompt = input("prompt: ")
    
    # Début du timer
    start = time.time()
    
    # Traduction de la requete vers de l'anglais
    translatedText = argostranslate.translate.translate(prompt, from_code, to_code)
    print('\033[H\033[J')
    print("Traduction: ", translatedText)
    
    # Détéction des émotions
    output = classifier([translatedText])[0]
    print("Emotions: \n", output[0], output[1])
    
    print("Durée de l'opération: ", (time.time() - start), "s")