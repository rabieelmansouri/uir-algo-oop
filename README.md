# Mon Projet

Mon projet est une application Python qui permet de dessiner des formes géométriques telles que des cercles et des carrés dans une couleur spécifiée.

## Dénomination : Créateur des formes colorées

L'application demande à l'utilisateur de saisir le type de forme, ses paramètres (rayon pour les cercles, côté pour les carrés), ainsi que la couleur dans laquelle la forme doit être dessinée. Si les entrées sont correctes, l'application génère une image représentant la forme dessinée avec les paramètres spécifiés.

# Instructions d'Installation

## Pour utiliser ce projet, suivez ces instructions :

- Clonez le repo depuis GitHub en utilisant la commande suivante, `git clone https://github.com/rabieelmansouri/uir-algo-oop.git`.
- Accédez au dossier du projet.
- Créez un environnement virtuel pour isoler les dépendances, ex : (`python -m venv env`),
- Activez l'environnement virtuel (`.\env\Scripts\activate`)
- Apres : pip install -r requirements.txt

# Utilisation du Projet

## Une fois les dépendances installées, vous pouvez exécuter le projet en suivant ces étapes :

- `python designer.py` dans vous Terminal

- Suivez les instructions à l'écran pour saisir le type de forme, ses paramètres (rayon ou côté ) et la couleur dans laquelle vous souhaitez dessiner la forme.

### Forme : `string : chaînes de caractères`

### Color : `string : chaînes de caractères`

### Rayon ou côté : `int > 0`

- L'application générera un message et aussi une image dans le répertoire du project, représentant la forme dessinée avec les paramètres spécifiés.

# Structure du Projet :

## Voici la structure des fichiers de ce projet :

- designer.py : Le script principal qui interagit avec l'utilisateur et génère l'image de la forme dessinée le même fichier c'est le Module contenant la classe Dessinateur qui gère l'interaction avec l'utilisateur et la génération de l'image.

- forms.py : Module contenant les classes pour les formes géométriques (Cercle et Carré).

- image_saver.py : Module contenant la fonction sauvegarder_image pour enregistrer l'image générée.
