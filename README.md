# Projet Critiques

Le "Projet Critiques" est une application web qui permet aux utilisateurs d'écrire et de partager des critiques sur différents sujets.

## Fonctionnalités

1. **Inscription & Connexion** : Les nouveaux utilisateurs peuvent s'inscrire, et les utilisateurs existants peuvent se connecter.
2. **Créer des billets**: Les utilisateurs peuvent créer des billets sur lesquels d'autres pourront écrire des critiques.
3. **Écrire des critiques** : Les utilisateurs peuvent écrire des critiques sur les billets existants.
4. **Flux d'utilisateurs** : Les utilisateurs ont un flux personnel montrant tous leurs billets et critiques.
5. **Abonnements** : Les utilisateurs peuvent suivre d'autres utilisateurs et voir leurs billets et critiques.
6. **Gestion des billets & critiques**: Les utilisateurs peuvent modifier ou supprimer leurs propres billets et critiques.
7. **Responsive Design** : L'application est conçue pour être utilisée sur des appareils de toutes tailles.

## Installation

1. Clonez le dépôt git.
2. Créez un environnement virtuel en utilisant `python -m venv venv`.
3. Activez l'environnement virtuel:
   - Sous Windows : `venv\Scripts\activate`
   - Sous macOS et Linux : `source venv/bin/activate`
4. Installez les dépendances en utilisant `pip install -r requirements.txt`.
5. Configurez votre base de données et ajustez les paramètres dans `settings.py` si nécessaire.
6. Lancez `python manage.py migrate` pour créer la base de données.
7. Lancez `python manage.py runserver` pour démarrer le serveur de développement.
8. Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/login` pour accéder à la page d'accueil.

## Contribution

Les contributions sont les bienvenues! Veuillez créer une issue ou soumettre une pull request.

## Licence

Ce projet est sous licence MIT.
