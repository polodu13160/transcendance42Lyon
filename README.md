# GatchaGames — Transcendence

Application de cartes à collectionner autour du jeu vidéo, développée avec React, TypeScript, Vite, Tailwind CSS et Motion.

## Apprendre à comprendre et refaire le projet

**Commence par le [guide d’apprentissage complet](docs/README.md).** Il explique le code présent dans ce dépôt, les choix de conception, les limites actuelles et propose un parcours pour recoder les fonctionnalités sans assistance.

1. [Architecture et état réel du projet](docs/01-architecture.md)
2. [JavaScript et TypeScript utiles au projet](docs/02-javascript-typescript.md)
3. [React : composants, état, événements et hooks](docs/03-react.md)
4. [CSS et Tailwind : comprendre la mise en page](docs/04-css-tailwind.md)
5. [Cartes : données, thèmes, effets shiny et inclinaison 3D](docs/05-cartes-et-effets.md)
6. [Boosters et Motion : retournement, drag et sortie](docs/06-boosters-motion.md)
7. [Navigation, modales, formulaires et outils](docs/07-navigation-formulaires-outils.md)
8. [Diagnostic et améliorations à comprendre](docs/08-diagnostic.md)
9. [Exercices, corrections et préparation à l’oral](docs/09-exercices-et-oral.md)

## Lancer le projet

```sh
npm install
npm run dev
```

Ouvre l’adresse indiquée par Vite. Les scripts disponibles sont `dev`, `build`, `lint` et `preview`. `preview` sert le résultat d’un build préalablement réussi.

## État de référence

Documentation fondée sur le code lu le **27 octobre 2026**, à partir du commit `fe2b97c`. L’application utilise des données locales de démonstration ; aucun backend ni système d’authentification fonctionnel n’est implémenté dans le code source examiné.

Les vérifications initiales `npm run build` et `npm run lint` échouent. Le [diagnostic](docs/08-diagnostic.md) consigne les messages et explique leurs causes. Cette documentation n’applique pas les corrections au code de l’application.
