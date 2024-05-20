from PIL import Image

def sauvegarder_image(image, nom_fichier):
    image.save(nom_fichier)
    print(f"L'image a été sauvegardée sous le nom '{nom_fichier}'.")
