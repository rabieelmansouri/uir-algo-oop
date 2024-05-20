from PIL import Image, ImageDraw

class Forme:
    def __init__(self, couleur):
        self.couleur = couleur

    def dessiner(self, image_draw):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")

    def dessiner_regles(self, image_draw, largeur, hauteur):
        # Dessiner les règles
        for i in range(0, largeur, 50):
            image_draw.line([(i, 0), (i, 10)], fill="black")
            image_draw.text((i, 15), str(i), fill="black")
        for i in range(0, hauteur, 50):
            image_draw.line([(0, i), (10, i)], fill="black")
            image_draw.text((15, i), str(i), fill="black")

class Cercle(Forme):
    def __init__(self, couleur, rayon):
        super().__init__(couleur)
        self.rayon = rayon

    def dessiner(self, image_draw):
        bounding_box = [50, 50, 50 + 2 * self.rayon, 50 + 2 * self.rayon]
        image_draw.ellipse(bounding_box, fill=self.couleur)
        # Ajouter la mesure du rayon
        image_draw.text((50 + self.rayon, 50 + self.rayon), f"r = {self.rayon}", fill="black")
        print(f"Dessiner un cercle de couleur {self.couleur} avec un rayon de {self.rayon}.")

class Carre(Forme):
    def __init__(self, couleur, cote):
        super().__init__(couleur)
        self.cote = cote

    def dessiner(self, image_draw):
        bounding_box = [50, 50, 50 + self.cote, 50 + self.cote]
        image_draw.rectangle(bounding_box, fill=self.couleur)
        # Ajouter la mesure du côté
        image_draw.text((50 + self.cote / 2, 50 + self.cote / 2), f"a = {self.cote}", fill="black")
        print(f"Dessiner un carré de couleur {self.couleur} avec un côté de {self.cote}.")
