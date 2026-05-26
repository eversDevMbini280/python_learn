"""

Creez un programme qui :
1) Demande deux nombres a l'utilisateur
2) Affiche leur somme, difference, produit et quotient
3) Affiche aussi le reste de la division (modulo) et la puissance
Indice : Pensez a convertir les entrees avec float() pour gerer les decimaux.

"""

print("Bonjour cher utilisateur, veuillez entrer deux nombres afin d'en effectuer le calcul :")

nombre1 = int(input("Entrez le premier nombre :"))

nombre2 = int(input("Entrez le second nombre :"))

somme = nombre1 + nombre2
print(f"L'addition de {nombre1} et {nombre2} est égale à {somme}")

difference = nombre1 - nombre2 
print(f"La difference entre {nombre1} et {nombre2} est égale à {difference}")

produit = nombre1 * nombre2
print(f"Le produit entre {nombre1} et {nombre2} est égale à {produit}")

quotient = nombre1 / nombre2
print(f"Le quotient de {nombre1} par {nombre2} est égale à {quotient}")

reste = nombre1 % nombre2 
print(f"Le reste de la division de {nombre1} par {nombre2} est égale à {reste}")

puissance = nombre1 ** nombre2
print(f"{nombre1} puissance {nombre2} est égale à {puissance}")