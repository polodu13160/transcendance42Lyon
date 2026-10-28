# Apprendre GatchaGames, du code à l’autonomie

Ce guide a deux objectifs : te permettre d’expliquer chaque partie du projet avec tes propres mots et de reconstruire ses fonctionnalités à partir d’un fichier vide. Il part du code réellement présent, puis montre comment raisonner pour écrire le suivant.

**Référence : 27 octobre 2026, commit `fe2b97c`.** Les comportements décrits sont issus de la lecture du dépôt. La compilation et le lint ont été exécutés ; les interactions visuelles ne constituent pas ici une recette manuelle validée dans le navigateur.

## Comment lire ce guide

Dans chaque chapitre, distingue trois choses :

- **Code actuel** : comportement ou extrait constaté dans le dépôt.
- **Exemple pédagogique** : version simplifiée pour comprendre un mécanisme, à adapter avant intégration.
- **Amélioration proposée** : ce qui serait souhaitable mais n’est pas encore fait.

Les exemples pédagogiques ne remplacent aucun fichier de l’application. Une page qui affiche un formulaire de connexion ne prouve pas qu’une connexion existe. Une carte tirée localement ne prouve pas qu’elle est sauvegardée dans une collection.

## Parcours de lecture

| Étape | Chapitre | Ce que tu dois savoir faire en sortant |
| --- | --- | --- |
| 1 | [Architecture](01-architecture.md) | Suivre le trajet du navigateur jusqu’à une carte |
| 2 | [JavaScript et TypeScript](02-javascript-typescript.md) | Lire les fonctions, les tableaux et les types sans deviner |
| 3 | [React](03-react.md) | Choisir les props, l’état et les callbacks d’un composant |
| 4 | [CSS et Tailwind](04-css-tailwind.md) | Refaire une carte et une navigation responsive |
| 5 | [Cartes et effets](05-cartes-et-effets.md) | Expliquer la rareté, le shiny et le calcul de l’inclinaison |
| 6 | [Boosters et Motion](06-boosters-motion.md) | Retracer un clic, un flip, un swipe et la réinitialisation |
| 7 | [Navigation et outils](07-navigation-formulaires-outils.md) | Comprendre les éléments qui entourent les cartes |
| 8 | [Diagnostic](08-diagnostic.md) | Lire une erreur et vérifier une hypothèse |
| 9 | [Exercices et oral](09-exercices-et-oral.md) | Recoder sans modèle puis défendre tes choix |

## Une méthode pour apprendre vraiment

Pour chaque fonctionnalité : lis le chapitre, ferme-le, dessine le flux de données, puis écris une version simple. Rouvre le code seulement pour comparer. Corrige une seule différence à la fois et explique à voix haute pourquoi elle change le résultat.

Évite de considérer « je reconnais ce code » comme une preuve de maîtrise. Le bon test est : « je peux choisir où mettre l’état, écrire les événements et prédire les cas limites avant d’exécuter ».

Une séance peut suivre ce rythme : 15 minutes de lecture, 30 à 45 minutes de reconstruction et 10 minutes de vérification. Passe à la suite lorsque tu sais expliquer ce que tu viens d’écrire.

## Carte mentale du projet

```text
HTML : point d’entrée et structure
  → JavaScript : logique et interactions
  → TypeScript : contrats vérifiés avant l’exécution
  → React : interface calculée depuis props et état
  → React Router : choix de la page selon l’URL
  → Tailwind + CSS : présentation et effets
  → Motion : animation du flip, du glissement et de la sortie
```

Vite assemble ces modules et sert le projet pendant le développement. Les données actuelles viennent de `test_data/cardsData.json`.

## Ce que « complet » couvre ici

Le guide couvre les fichiers source présents, la configuration utile, les fonctionnalités visibles dans le code, les fichiers préparatoires, les erreurs relevées et les mécanismes nécessaires pour reproduire l’ensemble. Il ne suppose pas de backend, de persistance, de multijoueur ou de règles de tirage qui ne sont pas implémentés.

Les documentations officielles sont liées dans les chapitres pour approfondir. Le code du dépôt reste la référence pour comprendre cette version précise du projet.
