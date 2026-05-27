Systeme de retry avec logging


Creez une fonction appel_api_simule(url) qui simule un appel reseau :
- Genere aleatoirement une TimeoutError (30% de chance), ConnectionError (20%) ou reussit
(50%)
- Creez une fonction avec_retry(func, max_tentatives=3, delai=1) qui reessaie
automatiquement
- Loggez chaque tentative avec le module logging (date, tentative, succes/echec)
- Apres le nombre max de tentatives, levez une erreur finale personnalisee


Indice : 
Utilisez time.sleep(delai) pour attendre entre les tentatives et import logging pour les logs.