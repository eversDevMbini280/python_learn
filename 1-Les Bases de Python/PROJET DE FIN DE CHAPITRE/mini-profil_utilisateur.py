"""

Description
Creez un programme interactif qui construit un profil utilisateur complet et le presente de facon
stylisee dans le terminal.
Objectifs
1. Demander : prenom, nom, age, ville, metier/etudes
2. Calculer l'annee de naissance (utilisez 2026 comme annee actuelle)
3. Afficher un encadre textuel avec toutes les informations
4. Calculer et afficher l'age dans 5, 10 et 20 ans
5. Afficher un message personnalise selon l'age (mineur, jeune adulte, adulte, senior)
Bonus
Ajoutez la validation : si l'utilisateur entre un age negatif ou superieur a 120, affichez un
message d'erreur.

"""


#Recolte d'informations personel de l'utilisateur
print(

    "╔════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
    "\n"
    "║ ▓▒░ bonjour cher utilisateur, veuillez renseigner vos informations afin de constituer votre profil ░▒▓ ║"
    "\n"
    "╚════════════════════════════════════════════════════════════════════════════════════════════════════════╝"

)

prenom = str(input(

    "\n"
    "  ▓▒░ prénom(s): "
))

nom = str(input(

    "\n"
    "  ▓▒░ nom(s) : "
))

age = int(input(

    "\n"
    "  ▓▒░ âge: "
))

ville = str(input(

    "\n"
    "  ▓▒░ ville: "
))

metier = str(input(

    "\n"
    "  ▓▒░ metier/etudes: "
))



#Calcule de l'année de naissance
annee_naissance = 2026 - age


#Recapitulatif des informations de l'utilisateur
print(
     
    "\n"
    "╔═════════════════════════════════════════════════════╗"
    "\n"
    "║ ▓▒░            PROFIL UTILISATEUR               ░▒▓ ║"
    "\n"
    "╠═════════════════════════════════════════════════════╣"
    "\n"
    "║                                                     ║"
    "\n"
   f"║       ▓▒░ prénom(s): {prenom}                              ║"
    "\n"
    "║                                                     ║"
    "\n"
   f"║       ▓▒░ nom(s) : {nom}                                ║"
    "\n"
    "║                                                     ║"
    "\n"
   f"║       ▓▒░ âge: {age} ans                                ║"
    "\n"
    "║                                                     ║"
    "\n"
   f"║       ▓▒░ année de naissance: {annee_naissance}                  ║"
    "\n"
    "║                                                     ║"
    "\n"
   f"║       ▓▒░ ville: {ville}                                  ║"
    "\n" 
    "║                                                     ║"
    "\n"
   f"║       ▓▒░ metier/etudes: {metier}                          ║"
    "\n"
    "║                                                     ║"
    "\n"
    "╠═════════════════════════════════════════════════════╣"
    "\n"
    "║ ▓▒░       powered by eversDevMbini280           ░▒▓ ║"
    "\n"
    "╚═════════════════════════════════════════════════════╝"

)

#calcule et affichage de l'age dans 5, 10 et 20 ans
print(
    "\n"
    " "
    f"▓▒░ Dans 5ans en 2031 vous aurez {age + 5} ans"
    "\n"
    " "
    "\n"
    f"▓▒░ Dans 10ans en 2036 vous aurez {age + 10} ans"
    "\n"
    " "
    "\n"
    f"▓▒░ Dans 20ans en 2046 vous aurez {age + 20} ans"
)


#Affichage d'un message personnalisé selon l'age
if age < 18:
    print(
       "\n"
       " "
       "╔════════════════════════════╗"
       "\n"
       "║ ▓▒░  Vous etes mineur  ░▒▓ ║"
       "\n"
       "╚════════════════════════════╝"
    )
elif age >= 18 and age < 25:
    print(
       "\n"
       " "
       "╔═════════════════════════════════════╗"
       "\n"
       "║ ▓▒░  Vous etes un(e) jeune adulte  ░▒▓ ║"
       "\n"
       "╚═════════════════════════════════════╝"
    )
elif age >= 25 and age < 50:
    print(
       "\n"
       " "
       "╔═══════════════════════════════╗"
       "\n"
       "║ ▓▒░  Vous etes un(e) adulte  ░▒▓ ║"
       "\n"
       "╚═══════════════════════════════╝"
    )
else:
    print(
       "\n"
       " "
       "╔═══════════════════════════════╗"
       "\n"
       "║ ▓▒░  Vous etes un(e) senior  ░▒▓ ║"
       "\n"
       "╚═══════════════════════════════╝"
    )