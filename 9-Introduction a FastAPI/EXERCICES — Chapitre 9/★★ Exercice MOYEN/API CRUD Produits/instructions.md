API CRUD Produits

Creez une API complete pour gerer des produits avec :

Modele Pydantic Produit (id, nom, prix, stock, categorie)
POST /produits -> creer un produit
GET /produits -> lister tous (avec filtre optionnel par categorie)
GET /produits/{id} -> obtenir un produit
PUT /produits/{id} -> modifier un produit
DELETE /produits/{id} -> supprimer (erreur 404 si inexistant)


Indice : 
Utilisez une liste comme base de donnees en memoire. Gerez les erreurs avec HTTPException.