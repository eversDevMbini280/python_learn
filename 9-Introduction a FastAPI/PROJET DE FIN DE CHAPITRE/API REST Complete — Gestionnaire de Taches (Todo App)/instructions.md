API REST Complete — Gestionnaire de Taches (Todo App)


Description:

Construisez une API FastAPI complete et fonctionnelle pour une application de gestion de
taches, prete a etre connectee a un frontend.


Objectifs:

41. Modeles : Tache (id, titre, description, statut, priorite, date_creation, date_limite)
42. CRUD complet avec validation Pydantic stricte
43. Filtres : par statut (todo/en_cours/termine), par priorite, par date
44. Recherche par texte dans le titre et la description
45. Statistiques : GET /stats -> nombre par statut, taux de completion, taches en retard
46. Persistance : sauvegarder et charger depuis un fichier JSON


Bonus:

Documentez votre API avec des descriptions dans chaque route (parametre description de
@app.get). Ajoutez des exemples dans vos modeles Pydantic avec class Config.