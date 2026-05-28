"""

Table de multiplication

Demandez un nombre a l'utilisateur et affichez sa table de multiplication de 1 a 10.
Exemple pour 7 : '7 x 1 = 7', '7 x 2 = 14', etc.

Indice : 
Utilisez une boucle for avec range(1, 11).

"""

#recuperation du chiffre de l'utilisateur.
print(

    "╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗"
    "\n"
    "║ ▓▒░ bonjour cher utilisateur, obtenez la table de multiplication de votre choix en entrant n'inportequel chiffre ou nombre  ░▒▓ ║"
    "\n"
    "╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝"

)


table = int(input(
    
    "\n"
    "  ▓▒░ de quelle table de multiplication avez vous besoin ? :"

))


#système de validation avec la boucle while   
while table >= 11:

    table = int(input(
            
        "\n"
        "═════════════════════════════════════════════════════════════════════════════════════════════════════"
        "\n"
       f"  ▓▒░ erreur la table de {table} n'est pas pris en charge veuillez saisire un autre chiffre ou nombre"
        "\n"
        "═════════════════════════════════════════════════════════════════════════════════════════════════════"
        "\n"
        " "
        "\n"
        "  ▓▒░ de quelle table de multiplication avez vous besoin ? :"

        ))

    if table < 11:
        break
    

print(
        
    "\n"
    "╔══════════════════════════════════════════════════════════╗"
    "\n"
   f"║ ▓▒░   Voici la table de mutiplication de {table}     ░▒▓ ║"
    "\n"
    "╠══════════════════════════════════════════════════════════╝"

)



#utilisation de la bloucle for pour generer des tables de multiplication de 0 à 100
for i in range(11):

    print(

        "║                                  "
        "\n"
       f"║ ▓▒░ {table} x {i} = {table * i}  "
    )

print(
    
    "║                                  "
    "\n"
    "╚══════════════════════════════════════════════════════════╝"

)
