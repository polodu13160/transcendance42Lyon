# 5. Cartes : du JSON aux effets visuels

## 5.1 Le modèle réellement utilisé

Le JSON contient 30 objets. Chaque entrée fournit `id`, `name`, `resume`, `rating`, `image`, `rarity`, `isShiny` et `isGame`. Le composant reçoit toutes ces propriétés sauf `id`, qui sert aux listes ou à la logique du parent.

```ts
export type GameCardProps = {
  rarity: keyof typeof cardThemes;
  name: string;
  rating: number;
  resume: string;
  image: string;
  isShiny: boolean;
  isGame: boolean;
};
```

La rareté et le shiny sont indépendants : une carte commune peut être shiny, une légendaire peut ne pas l’être. `isGame` choisit seulement le texte « Game » ou « DLC ». Les valeurs de combat `9000` et `7432` sont écrites directement dans le JSX ; elles ne proviennent pas des données.

## 5.2 `cardThemes` : un dictionnaire de présentation

```ts
const theme = cardThemes[rarity];
```

Les clés sont `common`, `uncommon`, `rare`, `epic` et `legendary`. Chaque entrée contient :

| Champ | Utilisation |
| --- | --- |
| `cardBorder` | Fond de l’enveloppe qui simule une bordure |
| `backGround` | Fond intérieur d’une carte normale |
| `shinyBack` | Fond intérieur d’une carte brillante |
| `badge` | Couleur de bordure et de texte du badge |
| `rarityName` | Libellé lisible de la rareté |

Cela évite cinq versions presque identiques de `GameCard`. La structure reste commune ; le dictionnaire concentre les différences.

Pour ajouter une rareté, il faut une entrée complète, des données compatibles, puis une vérification de toutes les vues. Un champ incomplet ou une valeur non reconnue dans le JSON casse ce contrat.

## 5.3 Lire l’arbre visuel de `GameCard`

```text
TiltCard : interaction avec le pointeur
  └─ enveloppe arrondie + padding + fond de bordure
       └─ intérieur au ratio 2/3
            ├─ décors shiny éventuels
            ├─ zone image
            │    ├─ image en object-cover
            │    └─ badge de rareté + étoile shiny
            └─ zone d’informations
                 ├─ titre
                 ├─ étoile, note, séparateur et Game/DLC
                 ├─ résumé
                 └─ valeurs de combat fixes
```

Le fond de bordure reste visible grâce au padding de l’enveloppe. L’image remplit sa zone avec `h-full w-full object-cover` : elle conserve son ratio mais peut être recadrée.

`draggable={false}` empêche le drag natif de l’image, qui gênerait l’interaction avec la carte. Cela ne désactive pas le drag Motion de son parent.

Les icônes viennent de `react-icons`. Ce sont des composants SVG ; une couleur ou une taille peut être passée comme à d’autres composants.

## 5.4 Effet shiny : plusieurs couches distinctes

Le résultat combine :

1. Une bordure en dégradé dont la position de fond est animée.
2. Un fond intérieur dépendant de la rareté.
3. `.shiny-waves`, un petit SVG encodé en URL de données et répété en arrière-plan.
4. `.shiny-sweep`, un voile coloré qui traverse la carte.
5. Le reflet du pointeur ajouté par `TiltCard`.

Le SVG des vagues est une texture statique dans le code actuel ; le balayage, lui, se déplace. Ne confonds pas la présence de lignes courbes avec une animation de vagues.

Le masque du balayage utilise du transparent sur les bords et du noir au centre. Dans ce masque alpha, la zone opaque laisse apparaître le fond coloré et les bords transparents le masquent.

```css
@keyframes shiny-sweep {
  0% { transform: translateX(-150%); }
  50%, 100% { transform: translateX(150%); }
}
```

Il traverse durant la première moitié du cycle de deux secondes, puis reste hors cadre jusqu’au cycle suivant.

Deux éléments `.shiny-sweep` sont actuellement rendus pour une carte shiny : l’un dans le groupe décoratif, l’autre dans une enveloppe `z-20`. Cela peut renforcer l’effet, mais il faut vérifier si cette duplication est souhaitée.

## 5.5 `TiltCard` utilise le DOM et du CSS

Ce composant n’utilise pas Motion. Il écoute `onPointerMove`, mesure le rectangle du wrapper, normalise la position puis écrit des variables CSS sur la carte intérieure.

Il contient deux refs :

- `wrapRef` désigne la zone stable qui reçoit les événements.
- `cardRef` désigne la surface qui tourne.

Garder le wrapper fixe évite que la carte déplacée modifie sans cesse sa propre zone de mesure et provoque un suivi instable.

## 5.6 Le calcul de l’inclinaison, étape par étape

Code actuel, simplifié uniquement dans la mise en forme :

```ts
const r = wrap.getBoundingClientRect();
const px = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width));
const py = Math.min(1, Math.max(0, (e.clientY - r.top) / r.height));

const rotateY = (px - 0.5) * max;
const rotateX = (0.5 - py) * max;
```

`clientX` et `r.left` utilisent le même repère de viewport. Leur différence donne la position horizontale dans la boîte. La division par la largeur transforme cette position en fraction. Le couple `Math.max` / `Math.min` limite le résultat à l’intervalle `[0, 1]` : c’est un clamp.

Pour une boîte de 300 × 450 px et `max={25}` :

| Position | `px` | `py` | Rotation Y | Rotation X |
| --- | --- | --- | --- | --- |
| Centre | 0.5 | 0.5 | 0° | 0° |
| Bord gauche au milieu | 0 | 0.5 | −12.5° | 0° |
| Bord droit au milieu | 1 | 0.5 | +12.5° | 0° |
| Bord haut au milieu | 0.5 | 0 | 0° | +12.5° |
| Coin bas droit | 1 | 1 | +12.5° | −12.5° |

Le nom `max` peut induire en erreur : avec la formule actuelle, l’angle maximal absolu vaut `max / 2`. Pour obtenir ±25°, il faudrait multiplier la coordonnée centrée par `2 * max`, ou renommer la prop pour parler d’amplitude totale.

## 5.7 De JavaScript à CSS

```ts
card.style.setProperty("--tilt-ry", rotateY.toFixed(2) + "deg");
card.style.setProperty("--tilt-gx", (px * 100).toFixed(1) + "%");
```

Le premier nombre devient un angle avec unité. Le second devient la position du reflet en pourcentage. CSS consomme ces valeurs :

```css
transform:
  perspective(var(--tilt-perspective))
  rotateX(var(--tilt-rx, 0deg))
  rotateY(var(--tilt-ry, 0deg));
```

`perspective(1000px)` donne une profondeur visuelle. Une perspective plus courte accentue généralement la déformation. `preserve-3d` permet de conserver la disposition 3D des descendants ; cela ne crée pas à lui seul de profondeur entre des enfants coplanaires.

## 5.8 Reflet et retour au repos

`.t-tilt-glare` superpose trois dégradés radiaux centrés sur les variables du pointeur. `mix-blend-mode: screen` éclaircit le résultat par mélange avec ce qui est derrière. `pointer-events: none` garde le reflet passif.

Pendant le déplacement, `.is-tilting` choisit une transition de suivi de 400 ms. À la sortie, le composant retire cette classe et remet les angles à zéro ; la transition de repos dure 1000 ms. Malgré un commentaire évoquant un suivi 1:1, les valeurs actuelles produisent un mouvement lissé avec retard, et non un suivi instantané.

Les styles sont injectés une fois lors de l’import du module grâce à l’identifiant `transitions-p19`. Le garde `typeof document !== "undefined"` évite cet accès DOM lorsqu’aucun document n’existe. Pour la maintenance, un fichier CSS explicite serait plus simple à retrouver que du CSS injecté au chargement.

## 5.9 Tactile et confort

`.t-tilt { touch-action: none; }` réserve les gestes au composant et peut empêcher le défilement tactile commencé sur une carte. Ce choix mérite un essai sur téléphone, surtout lorsqu’il est imbriqué avec le drag horizontal du booster.

Le mode de réduction des animations annule la transformation et la transition du tilt. Les écritures JavaScript continuent néanmoins à être exécutées lors des mouvements : neutraliser le rendu n’est pas arrêter les événements.

`<TiltCard max={25} select-none>` transmet aussi une prop `select-none`, mais `TiltCard` ne la lit pas et ne la propage pas. Les classes `select-none` présentes sur les vrais éléments assurent la sélection désactivée ; l’attribut ajouté au composant n’applique pas un utilitaire Tailwind.

## À savoir refaire

Commence par une carte sans effet. Ajoute les thèmes, puis le shiny, puis seulement le tilt. Calcule d’abord les angles sur papier pour le centre et les quatre coins. Si tu sais prédire les angles avant de bouger la souris, tu comprends le mécanisme.
