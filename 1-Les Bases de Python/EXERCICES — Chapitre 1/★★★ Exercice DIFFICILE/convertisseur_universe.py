"""

Creez un programme qui :
1) Demande une temperature en Celsius
2) La convertit en Fahrenheit (formule : F = C * 9/5 + 32) et en Kelvin (K = C + 273.15)
3) Affiche les trois valeurs avec 2 decimales (utilisez :.2f dans la f-string)
4) Indique si la temperature est : glaciale (<0), froide (0-15), moderee (15-25), chaude (>25)
Indice : Cherchez comment afficher 2 decimales dans une f-string avec :.2f

"""

print("Bonjour cher utilisateur, veuillez entrer la temperature qu'il fait :")

temperature = float(input("Entrez la temperature en degres celsius : "))

fahrenheit = (temperature * 9/5) + 32

kelvin = temperature + 273.15

print(f"{temperature:.2f} degres celsius fait {fahrenheit:.2f} degres fahrenheit et {kelvin:.2f} degres kelvin.")

if temperature < 0:
    print(f"{temperature:.2f} est une temperature glaciale.")
elif temperature >= 0 and temperature <= 15:
    print(f"{temperature:.2f} est une temperature glaciale.")
elif temperature >= 0 and temperature <= 15:    
    print(f"{temperature:.2f} est une temperature froide.")
elif temperature >= 15 and temperature <= 25:
    print(f"{temperature:.2f} est une temperature moderée.")
else:
    print(f"{temperature:.2f} est une temperature chaude.")   