# Ultra-Fast Multilanguage Emotion Detector 🚀  

Ce projet est une démonstration simple mais puissante d'un modèle de classification nommé `roberta-base-go_emotions`.  
Il permet d'extraire les émotions d'une phrase, quelle que soit la langue utilisée.  

/!\ *Des améliorations sont à venir, le repository est actuellement à ses premiers commits...*

---

## ✨ Fonctionnalités  

- **Détection multilingue** : Analysez les émotions d'une phrase dans n'importe quelle langue grâce à un prétraitement automatique.  
- **Rapide et efficace** : Utilise le modèle `roberta-base-go_emotions` optimisé pour détecter les émotions de manière précise.  
- **Cas d'utilisation variés** : Affichez les émotions en fonction des entrées utilisateur, intégrez-les dans des assistants virtuels...

---

## 🚀 Installation  

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine.  

Installez les dépendances nécessaires avec :  

```bash  
pip3 install -r ./requirements.txt 
```  

---

## 🛠️ Utilisation  

1. Clonez le dépôt ou téléchargez les fichiers nécessaires.  
2. Lancez le script principal en utilisant la commande suivante :  

```bash  
python3 main.py  
```  

3. Entrez une phrase dans la langue de votre choix, et découvrez les émotions associées !  

---

## 🧪 Exemple d'utilisation  

```bash
Input: "Je suis super heureux"  
Output:    
    Langue détectée : fr
    Texte traduit en anglais : I'm super happy.
    Émotions détectées :
    - joy: 0.89
    - approval: 0.03
    - admiration: 0.03
    - relief: 0.02
    - neutral: 0.02
    Durée totale de l'opération : 0.035 secondes
```

Testé sur `Orange pi 5 pro (16Go RAM)`, sans utilisation du NPU

Temps de traiement moyen ( 10 tokens ): 39ms

---

## 📂 Structure du projet  

- **`main.py`** : Contient le code principal pour la détection des émotions.  
- **`requirements.txt`** : Liste des dépendances nécessaires pour une installation facile.  

---

## 📖 Ressources supplémentaires  

- [Documentation Transformers](https://huggingface.co/docs/transformers/)  
- [Argos Translate](https://github.com/argosopentech/argos-translate)  
- Modèle utilisé : [`roberta-base-go_emotions`](https://huggingface.co/SamLowe/roberta-base-go_emotions)  

---

## 🤝 Contributions  

Les contributions sont les bienvenues ! Si vous souhaitez améliorer ou ajouter des fonctionnalités, n'hésitez pas à soumettre une pull request ou à ouvrir une issue.  

---

## 📜 Licence  

Ce projet est distribué sous la licence MIT. Consultez le fichier `LICENSE` pour plus de détails.  