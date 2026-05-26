"""
Creez un programme qui demande a l'utilisateur : son prenom, son age, et sa ville.
Puis affichez une phrase comme : 'Je m\'appelle Koffi, j\'ai 20 ans et j\'habite a Libreville.'
Indice : Utilisez input() pour les entrees et une f-string pour l'affichage.

"""

print("Bonjour cher utilisateur, veuillez renseigner les informations suivantes :")

prenom = input("Quel est votre prenom ? :")

age = input("Quel est votre age ? :")

ville = input("Dans quelle ville habitez-vous ? :")

print(f"Merci pour votre participation {prenom} agé de {age} ans, habitant de la ville de {ville} et aurevoir !)")