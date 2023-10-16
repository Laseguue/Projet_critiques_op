# Projet Critiques OP

## Description
Projet Critiques OP est une application web Django qui permet aux utilisateurs de créer des tickets et des critiques. Les utilisateurs peuvent également suivre d'autres utilisateurs et voir leurs tickets et critiques.

## Fonctionnalités
- Création de tickets et de critiques.
- Suivi d'autres utilisateurs.
- Visualisation des tickets et critiques des utilisateurs suivis et de l'utilisateur connecté.
- Inscription et authentification des utilisateurs.
- Modification et suppression des tickets et critiques créés par l'utilisateur.

## Structure du Projet
- [manage.py](https://github.com/Laseguue/Projet_critiques_op/blob/master/projet_critiques/manage.py) : Fichier de gestion de Django.
- [settings.py](https://github.com/Laseguue/Projet_critiques_op/blob/master/projet_critiques/projet_critiques/settings.py) : Fichier de configuration de l'application Django.
- [urls.py](https://github.com/Laseguue/Projet_critiques_op/blob/master/projet_critiques/projet_critiques/urls.py) : Fichier de configuration des URL de l'application Django.
- [views.py](https://github.com/Laseguue/Projet_critiques_op/blob/master/projet_critiques/critiques/views.py) : Fichier contenant les vues de l'application Django.
- [models.py](https://github.com/Laseguue/Projet_critiques_op/blob/master/projet_critiques/critiques/models.py) : Fichier contenant les modèles de l'application Django.
- [forms.py](https://github.com/Laseguue/Projet_critiques_op/blob/master/projet_critiques/critiques/forms.py) : Fichier contenant les formulaires de l'application Django.
- [templates](https://github.com/Laseguue/Projet_critiques_op/tree/master/projet_critiques/templates) : Dossier contenant les templates HTML de l'application Django.

## Exigences
- Python 3.10 ou supérieur
- Django 4.2.4 ou supérieur

## Installation
1. Clonez le dépôt GitHub.
2. Naviguez vers le dossier du projet.
3. Installez les dépendances avec `pip install -r requirements.txt` (si un fichier requirements.txt est présent).
4. Exécutez les migrations avec `python manage.py migrate`.
5. Démarrez le serveur de développement avec `python manage.py runserver`.
6. Ouvrez un navigateur web et accédez à `http://127.0.0.1:8000/login`.

## Auteur
[Laseguue](https://github.com/Laseguue)