Analyseur de logs


Generez d'abord un faux fichier de logs (1000 lignes) avec des entrees comme :
2025-01-15 14:32:01 ERROR /api/users Connection timeout


Parsez ce fichier et produisez un rapport JSON contenant :

Nombre d'erreurs par type (INFO, WARNING, ERROR), les 10 routes les plus touchees par
des erreurs,
Tableau horaire des erreurs, et les erreurs critiques (plus de 5 fois la meme).


Indice :
 Utilisez re.findall() pour extraire les parties du log avec des regex.