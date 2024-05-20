from PIL import Image, ImageDraw
from forms import Cercle, Carre
from image_saver import sauvegarder_image

class Dessinateur:
    def demander_forme(self):
        while True:
            forme = input("Veuillez saisir la forme (cercle ou carre): ").strip().lower()
            if forme not in ["cercle", "carre"]:
                print("Forme non valide. Veuillez saisir 'cercle' ou 'carre'.")
                continue
            return forme

    def demander_couleur(self):
        while True:
            couleur = input("Veuillez saisir la couleur (ex: 'red', 'blue', 'green'): ").strip().lower()
            if couleur not in ["red", "blue", "green"]:
                print("Couleur non valide. Veuillez saisir 'red', 'blue' ou 'green'.")
                continue
            return couleur

    def demander_mesure(self):
        while True:
            try:
                mesure = float(input("Veuillez saisir la mesure: "))
                if mesure <= 0:
                    print("La mesure doit être supérieure à zéro.")
                    continue
                return mesure
            except ValueError:
                print("Valeur de mesure non valide.")

    def creer_forme(self, forme, couleur, mesure):
        if forme == "cercle":
            return Cercle(couleur, mesure)
        elif forme == "carre":
            return Carre(couleur, mesure)

    def dessiner(self):
        while True:
            forme = self.demander_forme()
            couleur = self.demander_couleur()
            mesure = self.demander_mesure()

            # Créer une nouvelle image blanche
            largeur, hauteur = 1000, 1000
            image = Image.new("RGB", (largeur, hauteur), "white")
            image_draw = ImageDraw.Draw(image)

            forme_obj = self.creer_forme(forme, couleur, mesure)
            forme_obj.dessiner_regles(image_draw, largeur, hauteur)
            forme_obj.dessiner(image_draw)

            # Sauvegarder l'image
            sauvegarder_image(image, "forme_dessinee.png")
            break

# Exécution du programme
if __name__ == "__main__":
    dessinateur = Dessinateur()
    dessinateur.dessiner()
