API avec Authentification

Creez une API avec un systeme d'authentification simple par tokens :

POST /register -> creer un compte (nom, email, mot de passe)
POST /login -> authentifier et retourner un token (UUID genere avec uuid.uuid4())
GET /profil -> retourne le profil (token requis dans les headers)
POST /logout -> invalider le token

Middleware :
 verifier le token pour les routes protegees avec Depends()

Indice :
 Stockez les tokens dans un dict {token: user_id}. Utilisez Header pour lire les headers.