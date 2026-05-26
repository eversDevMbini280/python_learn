# ΙΙΙ Python Learn ΙΙΙ

Bienvenue dans **Python Learn**, un dépôt pensé pour apprendre Python pas à pas, avec une documentation personnalisée, des exercices progressifs et des projets pratiques de fin de chapitre.

L'objectif est double : m'aider à améliorer ma compréhension de Python tout en offrant à d'autres débutants un espace simple, organisé et motivant pour découvrir le langage.

Ce dépôt est public et ouvert aux contributions. Toute personne passionnée par le code peut proposer des ressources, de la documentation, des vidéos, des corrections ou de nouveaux exercices, à condition de respecter l'architecture du projet et de travailler depuis une branche dédiée.

## Α. Vision du projet

| Α - Axe | Β - Description |
| --- | --- |
| Apprentissage | Comprendre Python progressivement, chapitre par chapitre. |
| Pratique | S'exercer avec des exercices faciles, moyens et difficiles. |
| Projet | Consolider chaque chapitre avec un mini-projet final. |
| Partage | Permettre aux débutants et passionnés de contribuer. |
| Organisation | Garder une structure claire et uniforme dans tout le dépôt. |

## Β. Contenu du dépôt

Le dépôt est organisé sous forme de chapitres numérotés. Chaque chapitre aborde une grande notion de Python.

| Α - Chapitre | Β - Thème |
| --- | --- |
| `1-Les Bases de Python` | Variables, affichage, entrées utilisateur, types simples et premiers scripts. |
| `2-Structures de Controle` | Conditions, boucles, `break` et `continue`. |
| `3-Les Fonctions` | Définition, paramètres, retour et portée. |
| `4-Structures de Donnees` | Listes, tuples, dictionnaires et sets. |
| `5-Programmation Orientee Objet` | Classes, objets, méthodes et héritage. |
| `6-Modules et Packages` | Imports, `pip` et bibliothèques standards. |
| `7-Gestion des Erreurs` | `try/except`, exceptions et debugging. |
| `8-Fichiers et JSON` | Lecture, écriture, JSON et CSV. |
| `9-Introduction a FastAPI` | Routes, endpoints, requêtes HTTP et Pydantic. |

Une documentation personnalisée est également disponible dans le fichier :

```text
python_documentation_personaliser_pour_evers_darrell_mbini.pdf
```

## Γ. Architecture recommandée

L'architecture correcte à suivre est celle du chapitre 1 :

```text
1-Les Bases de Python/
├── EXERCICES — Chapitre 1/
│   ├── ★ Exercice FACILE/
│   │   └── carte_de _visite.py
│   ├── ★★ Exercice MOYEN/
│   │   └── calculatrice_simple.py
│   └── ★★★ Exercice DIFFICILE/
│       └── convertisseur_universe.py
└── PROJET DE FIN DE CHAPITRE/
    └── mini-profil_utilisateur.py
```

Chaque nouveau chapitre doit idéalement suivre ce modèle :

```text
N-Nom du Chapitre/
├── 1-Notion principale/
├── 2-Notion suivante/
├── 3-Autre notion/
├── EXERCICES — Chapitre N/
│   ├── ★ Exercice FACILE/
│   ├── ★★ Exercice MOYEN/
│   └── ★★★ Exercice DIFFICILE/
└── PROJET DE FIN DE CHAPITRE/
```

## Δ. Niveau des exercices

| Α - Niveau | Β - Objectif |
| --- | --- |
| `★ Exercice FACILE` | Découvrir la notion avec un exercice simple et direct. |
| `★★ Exercice MOYEN` | Combiner plusieurs notions dans un programme plus complet. |
| `★★★ Exercice DIFFICILE` | Résoudre un problème plus riche, avec davantage de logique. |
| `PROJET DE FIN DE CHAPITRE` | Réutiliser les notions du chapitre dans un mini-projet concret. |

## Ε. Comment utiliser ce dépôt

1. Choisir un chapitre selon la notion que vous voulez apprendre.
2. Lire les ressources ou la documentation associée.
3. Faire les exercices dans l'ordre : facile, moyen, difficile.
4. Terminer avec le projet de fin de chapitre.
5. Modifier les scripts, tester, casser, recommencer et comprendre.

Pour exécuter un fichier Python :

```bash
python "chemin/vers/le/fichier.py"
```

Exemple :

```bash
python "1-Les Bases de Python/PROJET DE FIN DE CHAPITRE/mini-profil_utilisateur.py"
```

## Ζ. Contribuer

Les contributions sont les bienvenues : exercices, corrections, ressources, documentation, liens utiles, vidéos ou améliorations de structure.

Avant toute contribution :

1. Créez votre propre branche.
2. Respectez l'architecture du dépôt.
3. Ajoutez vos fichiers dans le bon chapitre.
4. Nommez clairement vos dossiers et fichiers.
5. Expliquez brièvement ce que vous avez ajouté dans votre pull request.

Exemple de création de branche :

```bash
git checkout -b ajout-exercice-boucles
```

Types de contributions possibles :

| Α - Type | Β - Exemple |
| --- | --- |
| Exercice | Ajouter un exercice sur les boucles `for` et `while`. |
| Documentation | Ajouter une explication simple sur les dictionnaires. |
| Ressource | Ajouter un lien vers une vidéo pédagogique. |
| Correction | Corriger une faute, un bug ou une consigne peu claire. |
| Projet | Ajouter un mini-projet de fin de chapitre. |

## Η. Bonnes pratiques pour les contributeurs

- Garder un style simple et accessible aux débutants.
- Éviter les solutions trop avancées dans les premiers chapitres.
- Ajouter des commentaires utiles quand le code peut être difficile à comprendre.
- Ne pas modifier l'architecture globale sans raison claire.
- Tester les scripts avant de proposer une contribution.
- Respecter le niveau de difficulté indiqué par le dossier.

## Θ. Public visé

Ce dépôt est fait pour :

- les débutants qui découvrent Python ;
- les étudiants qui veulent pratiquer régulièrement ;
- les autodidactes qui aiment apprendre par projet ;
- les passionnés qui veulent partager leurs connaissances ;
- toute personne qui souhaite progresser avec une structure claire.

## Ι. Esprit du projet

Apprendre Python ne se résume pas à lire du code. Il faut pratiquer, se tromper, corriger, comparer, recommencer et construire de petits projets jusqu'à ce que les notions deviennent naturelles.

Ce dépôt avance dans cet esprit : simple, progressif, ouvert et collaboratif.
