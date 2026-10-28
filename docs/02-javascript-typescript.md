# 2. JavaScript et TypeScript utiles au projet

## 2.1 Variables et valeurs

```ts
const name = "Hollow Knight";
const rating = 9.5;
const isShiny = true;
let visibleIndex = 4;
visibleIndex = visibleIndex - 1;
```

`const` interdit de réassigner la variable. Il ne rend pas automatiquement immuable l’objet ou le tableau qu’elle référence. `let` permet une réassignation. Une chaîne, un nombre et un booléen ont des rôles différents : `"false"` est une chaîne non vide, donc une valeur vraie dans une condition JavaScript.

`null` exprime ici une absence volontaire, comme « aucune modale ». `undefined` peut être le résultat d’un accès manquant ou d’une fonction qui ne retourne rien.

## 2.2 Objets et déstructuration

```ts
const card = { name: "Hollow Knight", rating: 9.5, isShiny: false };
const { name, rating } = card;
const shinyCard = { ...card, isShiny: true };
```

`card.name` accède à un champ. La déstructuration crée des variables depuis ces champs. Le spread `...card` copie les propriétés de premier niveau ; les propriétés suivantes écrasent celles de même nom. Les objets imbriqués restent partagés si tu ne les copies pas aussi.

Dans `GameCard({ rarity, name, rating, ... })`, la déstructuration se fait directement dans le paramètre de la fonction.

## 2.3 Fonctions, paramètres et retours

```ts
function aboveThreshold(offset: number): boolean {
  return Math.abs(offset) > 100;
}

const aboveThresholdArrow = (offset: number): boolean => Math.abs(offset) > 100;
```

Ces deux fonctions ont la même intention. `number` décrit le paramètre, `boolean` le résultat. `void` indique qu’aucune valeur de retour exploitable n’est attendue.

Une **callback** est une fonction transmise à un autre morceau de code pour qu’il l’appelle au bon moment. `resetFunction` est une callback : le booster signale sa fin au parent, qui choisit comment réinitialiser l’accueil.

```tsx
onClick={handleBoosterState}
onClick={() => setActiveModal("login")}
```

Le premier transmet une fonction existante. Le second en crée une qui précise un argument. `onClick={handleBoosterState()}` exécuterait la fonction pendant le rendu : ce n’est pas le comportement recherché.

## 2.4 Conditions utilisées dans le JSX

```ts
const label = isGame ? "Game" : "DLC";
const canDrag = index === visibleIndex && dragOn;
```

Le ternaire choisit une valeur entre deux possibilités. `&&` s’arrête dès qu’une valeur est fausse et retourne un opérande. Dans `{isShiny && <Effect />}`, le booléen décide si React reçoit le composant.

Attention à `{count && <Badge />}` : si `count` vaut `0`, React peut afficher `0`. Préfère `{count > 0 && <Badge />}`.

`===` compare sans conversion implicite. `!dragOn` inverse un booléen. `condition || fallback` choisit le fallback pour toute valeur falsy, dont `0` ; `condition ?? fallback` ne remplace que `null` et `undefined`.

## 2.5 Tableaux : les méthodes à maîtriser

| Expression | Résultat | Modifie le tableau original ? |
| --- | --- | --- |
| `cards.map(c => c.name)` | Nouveau tableau transformé | Non |
| `cards.filter(c => c.isShiny)` | Nouveau tableau sélectionné | Non |
| `cards.slice(0, 5)` | Cinq premiers éléments au maximum | Non |
| `cards.find(c => c.id === id)` | Premier élément trouvé ou `undefined` | Non |
| `[...cards]` | Copie superficielle du tableau | Non |
| `cards.sort(compare)` | Tableau réordonné | Oui |

Dans l’accueil :

```ts
return [...cards]
  .sort(() => Math.random() - 0.5)
  .slice(0, 5);
```

La copie protège l’ordre de la liste source. Le tri aléatoire ne respecte toutefois pas le contrat d’un comparateur stable et ne garantit pas un mélange uniforme. Voir le [diagnostic et Fisher–Yates](08-diagnostic.md).

Dans `BrowsePage` :

```ts
Array.from({ length: 50 }, (_, index) => ({
  ...cards[index % cards.length],
  instanceId: index,
}));
```

`Array.from` crée 50 éléments. `_` indique un paramètre ignoré. `%` est le reste de la division : avec 30 cartes, `30 % 30` vaut `0`, donc la liste reprend au début. Il faut une source non vide ; le code actuel ne prévoit pas ce garde-fou.

`instanceId` identifie l’occurrence affichée, pas une carte réellement possédée. Les 50 éléments ne représentent donc pas 50 jeux distincts.

## 2.6 Imports et exports

```ts
import GameCard from "../features/cards/GameCard";
import { TiltCard } from "../features/cards/TiltCard";
import type { GameCardProps } from "../features/cards/GameCard";
```

Un `export default` s’importe sans accolades. Un export nommé s’importe avec des accolades. `import type` ne sert qu’à TypeScript et disparaît du code livré au navigateur.

`@/features/...` est un alias de `src/features/...`. Le dépôt le configure à la fois dans Vite pour la résolution réelle et dans TypeScript pour la vérification et l’éditeur. Le dossier physique `@/` à la racine n’est pas la cible de cet alias.

## 2.7 Les types primitifs et les contrats

```ts
type Rarity = "common" | "uncommon" | "rare" | "epic" | "legendary";

interface LearningCard {
  id: string;
  name: string;
  rarity: Rarity;
  isShiny: boolean;
}
```

Exemple pédagogique : les chaînes de l’union sont les seules valeurs acceptées. Une interface décrit la forme attendue d’un objet. TypeScript vérifie les usages avant l’exécution ; il ne transforme pas une réponse réseau erronée en bonne donnée.

Dans le dépôt, `GameCardProps` définit les données nécessaires au composant visuel. `CollectionCard = GameCardProps & { id: string }` est une intersection : elle impose les propriétés de la carte et un identifiant.

Le type `GameProps` de `src/types/game.ts` est différent : `id` numérique, `imageUrl`, `description`, `funfact`, `reviewCount`, et rareté `ultra-rare` au lieu de `epic`. Il n’est pas le contrat utilisé par les cartes actuelles.

## 2.8 `keyof typeof`, unions et propriétés facultatives

```ts
type CardRarity = keyof typeof cardThemes;
type ModalType = "login" | "signup" | null;
type DragAxis = false | "x";
type TiltOptions = { max?: number };
```

`typeof cardThemes` obtient le type de l’objet existant ; `keyof` en extrait les noms de propriétés. Ajouter une clé dans les thèmes fait alors évoluer le type de rareté correspondant.

`max?` est facultatif. `function TiltCard({ max = 32 })` fournit une valeur par défaut si `max` manque ou vaut `undefined`. Une valeur explicite de `0` reste `0`.

`false | "x"` est plus précis que `boolean | string` : le composant attend exactement l’arrêt du drag ou un drag horizontal.

## 2.9 Assertion de type et validation

```ts
const cards = cardsData as CollectionCard[];
```

`as` dit au compilateur de traiter cette valeur comme ce type. Il n’exécute aucune validation du JSON. Un nom de rareté invalide peut donc arriver jusqu’à `cardThemes[rarity]` puis faire échouer l’accès à `theme.cardBorder`.

Pour une future API, commence par recevoir `unknown`, vérifie les champs et les valeurs autorisées, puis construis le modèle validé. Un type statique et une validation à l’exécution répondent à deux problèmes différents. Voir le [manuel TypeScript sur les types courants](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html).

## 2.10 Asynchronisme et fermeture sur les variables

```ts
setTimeout(() => {
  setBoosterState("revealed");
}, 1000);
```

Le délai est en millisecondes. Il programme la callback au plus tôt après ce délai, selon la disponibilité du navigateur ; il ne bloque pas la page pendant une seconde.

La callback garde accès aux variables de son contexte : c’est une **fermeture**, ou closure. En React, une fonction créée pendant un rendu observe les valeurs de ce rendu. Cela explique pourquoi un état lu juste après son setter n’a pas encore changé.

Pour modifier un état à partir de sa valeur précédente :

```ts
setIncrementPack(previous => previous + 1);
```

React reçoit une fonction qui calcule le prochain état à partir de l’état en attente. Évite de modifier directement un objet d’état ou un tableau : crée la nouvelle valeur.

## Mini-exercice

Écris une fonction qui reçoit des cartes, conserve les shiny, trie une copie par note décroissante et retourne les trois premières. Vérifie que le tableau d’origine n’a pas changé. Explique pourquoi `filter().sort()` peut trier sans modifier la source : `filter` a déjà créé un nouveau tableau.
