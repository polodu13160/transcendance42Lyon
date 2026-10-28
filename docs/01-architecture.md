# 1. Architecture et état réel du projet

## 1.1 Le produit que l’on construit

GatchaGames est une interface de collection de cartes représentant des jeux vidéo. Le parcours le plus avancé consiste à ouvrir un booster, découvrir cinq cartes, les retourner et les faire glisser pour passer à la suivante.

Le code actuel est une application frontend. Il s’exécute dans le navigateur, importe un JSON local et ne possède pas de serveur applicatif dans les sources examinées.

## 1.2 Qui fait quoi dans la stack ?

| Outil | Responsabilité | Exemple dans le dépôt |
| --- | --- | --- |
| HTML | Document initial | `index.html`, élément `#root` |
| CSS | Présentation, couches et animation graphique | `global.css`, `CardEffects.css` |
| JavaScript | Calculs, fonctions et événements | Tirage, clic, gestion du pointeur |
| TypeScript | Vérification des contrats de données | `GameCardProps`, `BoosterTiming` |
| React | Composants et état de l’interface | `HomePage`, `GameCard` |
| React DOM | Montage dans le DOM du navigateur | `createRoot` dans `main.tsx` |
| React Router | Navigation interne par URL | `BrowserRouter`, `Routes`, `NavLink` |
| Tailwind CSS | Classes utilitaires générant du CSS | `flex`, `rounded-xl`, `md:hidden` |
| Motion | Animations et gestes React | `motion.div`, `AnimatePresence` |
| Vite | Serveur de développement et assemblage de production | `vite.config.ts` |
| ESLint | Analyse de règles de qualité | `eslint.config.js` |

React ne remplace pas JavaScript ; Tailwind ne remplace pas les connaissances CSS ; Motion ne décide pas des règles du jeu.

## 1.3 Versions : déclaration et installation sont différentes

Lecture effectuée le 27 octobre 2026 :

| Paquet | Plage dans `package.json` | Version dans `node_modules` au contrôle |
| --- | --- | --- |
| React / React DOM | `^19.2.8` | `19.3.0` |
| React Router | `^8.4.0` | `8.4.0` |
| Tailwind CSS | `^4.3.3` | `4.3.3` |
| Motion | `^14.6.0` | `14.4.0` |
| TypeScript | `~6.0.2` | `6.0.3` |
| Vite | `^8.3.0` | `8.3.1` |

`^` autorise une plage de mises à jour compatibles selon la version majeure ; `~` est plus restrictif sur la version mineure. `package-lock.json` décrit une résolution verrouillée. `node_modules` représente ce qui est disponible localement maintenant.

La version locale de Motion est inférieure à la plage déclarée : l’installation mérite d’être réconciliée avant d’étudier un comportement propre à une version. Ce guide ne prétend pas avoir réinstallé les dépendances. `npm ls --depth=0` permet de diagnostiquer les écarts ; une réinstallation contrôlée doit ensuite respecter le verrouillage choisi.

## 1.4 Le trajet du premier affichage

```text
index.html
  ├─ charge Ubuntu depuis Google Fonts
  ├─ contient <div id="root"></div>
  └─ charge /src/main.tsx
       ├─ importe global.css
       └─ createRoot(root).render(<App />)
            ├─ BrowserRouter
            └─ app-shell + particules + couche de contenu
                 ├─ Navbar
                 ├─ Modal si activeModal n’est pas null
                 └─ Routes → page correspondant à l’URL
```

`main.tsx` vérifie que `root` existe avant de monter React. Cette version n’enveloppe pas `App` dans `StrictMode`.

Le fond de particules est décoratif. `pointer-events: none` le laisse traverser par les clics, `aria-hidden` le masque aux technologies d’assistance, et une couche `relative z-10` place le contenu au-dessus.

## 1.5 Organisation des dossiers

```text
src/
  app/                 App et futur fichier de routes
  assets/              Logos, icônes SVG et illustration de booster
  components/
    layout/            Navigation et structure commune
    ui/                Modale, lien de navigation, thème
  data/                Emplacement de données préparé, actuellement vide
  features/
    auth/              Interfaces de connexion et inscription
    boosters/          Booster et pile interactive
    cards/             Carte, dos, retournement, inclinaison et thèmes
    collection/        Emplacements de filtres et grille, actuellement vides
  hooks/               Hooks utilitaires non branchés au parcours actuel
  lib/                 Fonctions utilitaires
  pages/               Composants associés aux routes
  services/            Emplacement d’API, actuellement vide
  styles/              CSS global
  types/               Modèle GameProps, distinct du modèle effectivement affiché
test_data/
  cardsData.json       30 objets de démonstration
  usersData.json       Fichier vide
```

Une **page** orchestre un écran. Une **feature** rassemble un comportement métier. Un **composant UI** décrit une brique réutilisable. Cette séparation permet de changer une carte sans réécrire toutes les pages.

## 1.6 Routes et maturité des écrans

| URL | Composant | État constaté |
| --- | --- | --- |
| `/` | `HomePage` | Tirage local, secousse, pile, flip et drag |
| `/collection` | `CollectionPage` | Retourne un titre vide ; aucune collection persistante |
| `/browse-all` | `BrowsePage` | Affiche 50 instances en répétant les données locales |
| `/market` | `MarketPage` | Démonstration d’une carte ; appel incomplet bloquant le build |
| `/profil` | `ProfilePage` | Affiche l’ébauche `SignForm` |
| `/settings` | `SettingsPage` | Conteneur sans contenu |
| `/trade` | `TradePage` | Conteneur sans contenu |
| `/play` | `PlayPage` | Illustration de booster via `BoosterPack` |

Il n’y a pas de route de secours `*` dans `App`. Une URL inconnue peut donc conserver la navigation avec une zone principale vide.

## 1.7 Inventaire des fichiers préparatoires

Sont vides : `src/app/router.tsx`, `src/services/api.ts`, `src/data/mockGames.ts`, `src/components/ui/Button.tsx`, `src/components/layout/Footer.tsx`, `CardDetails.tsx`, `BoosterReveal.tsx`, `CollectionFilters.tsx`, `CollectionGrid.tsx` et `test_data/usersData.json`.

Les hooks `use-mobile` et `use-toast`, ainsi que les fonctions de `src/lib/utils.ts`, existent mais aucun appel depuis les composants actifs n’a été trouvé lors du relevé. La présence d’un fichier ou d’une dépendance ne prouve pas son utilisation.

## 1.8 Ce que montre l’historique

L’historique explique l’ordre de construction, sans remplacer le code actuel :

1. Construction de la navigation, des modales et des formulaires.
2. Mise en forme de `GameCard` et extraction de `cardThemes`.
3. Ajout de `TiltCard`, des variantes shiny et des effets CSS.
4. Ajout de Motion, du dos de carte et de la pile de booster.
5. Évolution des règles de glissement et du seuil de retrait.
6. Ajout du pack SVG, du tirage et de la remise à zéro sur l’accueil.
7. Ajout de la secousse puis intégration flip + drag dans `fe2b97c`.

Des expériences apparaissent dans les messages de commit puis disparaissent des sources : ne présente pas un composant ancien comme encore utilisé. La note locale `.notes/booster-opening-plan.md` décrit aussi des intentions ; bilan final, garanties de rareté et sons restent des propositions.

## À savoir expliquer

Sans regarder le code, décris le chemin `index.html → main.tsx → App → HomePage → BoosterOpening → RevealCard → GameCard`. Pour chaque flèche, précise si elle transporte un composant, une donnée ou une fonction.
