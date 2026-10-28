# 4. CSS et Tailwind : comprendre ce que tu écris

## 4.1 Tailwind produit du CSS

```tsx
<div className="flex items-center gap-2 rounded-xl p-4" />
```

Cette combinaison crée une boîte flexible, aligne les éléments sur l’axe transversal, les espace, arrondit les coins et ajoute un espace intérieur. Pour la comprendre, il faut connaître les propriétés CSS correspondantes.

Le dépôt utilise Tailwind **v4**, chargé par `@tailwindcss/vite` dans `vite.config.ts` et `@import "tailwindcss"` dans `global.css`. Ne cherche pas nécessairement un `tailwind.config.js` : la configuration CSS de v4 est déjà utilisée ici. Voir [l’installation officielle avec Vite](https://tailwindcss.com/docs/installation/using-vite).

## 4.2 Le modèle de boîte

```text
marge extérieure → bordure → padding → contenu
```

`m-4` agit à l’extérieur ; `p-4` à l’intérieur. `gap-4` espace les enfants d’un conteneur flex ou grid, sans ajouter une marge autour du groupe.

Avec l’espacement par défaut de Tailwind, `p-4` vaut `1rem`, `gap-2` vaut `0.5rem`, `w-75` vaut `18.75rem`. Avec une racine de 16 px, `w-75` correspond à 300 px. Une personnalisation de l’espacement ou de la taille racine changerait ces valeurs calculées.

Le ratio `aspect-2/3` impose largeur / hauteur = 2/3. Une largeur de 300 px donne donc 450 px de hauteur pour la boîte concernée. Attention aux enveloppes : une carte extérieure avec padding et un contenu intérieur au ratio peuvent avoir des dimensions totales différentes.

## 4.3 Flexbox : toujours identifier les axes

```tsx
<div className="flex flex-col items-center justify-center gap-6" />
```

`flex-col` met l’axe principal à la verticale. `justify-center` centre sur cet axe ; `items-center` centre transversalement, donc horizontalement dans ce cas. Avec `flex-row`, ces rôles visuels s’inversent.

Dans `App`, `flex` place la navigation latérale et `<main>` côte à côte. `flex-1` laisse le contenu prendre l’espace disponible. `shrink-0` empêche la navigation ou une carte de rétrécir. `min-w-0` autorise une boîte flexible à devenir plus étroite que la largeur minimale de son contenu, ce qui évite certains débordements.

Dans `GameCard`, `flex-1 min-h-0` permet de partager la hauteur et de laisser les zones internes rétrécir. Sans `min-h-0`, du texte ou une image peut imposer une hauteur minimale inattendue.

## 4.4 Grid : la galerie de cartes

Code actuel :

```tsx
className="mx-auto grid max-w-[120rem] grid-cols-[repeat(auto-fill,18.75rem)] justify-center gap-6"
```

- `grid` active la grille.
- `repeat(auto-fill,18.75rem)` crée autant de colonnes de largeur fixe que possible.
- `justify-center` centre les pistes dans l’espace restant.
- `gap-6` crée les gouttières.
- `max-w-[120rem]` limite la largeur du conteneur.
- `mx-auto` centre ce conteneur si de l’espace horizontal reste disponible.

`auto-fill` peut conserver des pistes vides ; `auto-fit` les réduit. Ici les cartes conservent une largeur fixe. Sous la largeur d’une carte plus les marges de page, la grille peut déborder : une interface responsive ne se résume pas au menu mobile.

Amélioration possible : rendre aussi la carte adaptable et utiliser des colonnes `minmax(...)`. Changer seulement la grille en laissant `w-75` partout ne garantit pas que la carte remplira correctement sa nouvelle colonne.

## 4.5 Positionnement et superposition

| Classe | Effet dans le projet |
| --- | --- |
| `relative` | Fournit un repère à des enfants positionnés |
| `absolute top-0` | Superpose les cartes suivantes en haut de la pile |
| `absolute inset-0` | Couvre entièrement le repère |
| `fixed bottom-0` | Ancre la navigation mobile au viewport |
| `sticky top-0` | Maintient la navigation bureau au bord pendant le défilement, selon son conteneur |
| `z-10`, `z-20`, `z-50` | Ordonne des couches dans leur contexte d’empilement |
| `overflow-hidden` | Découpe ce qui dépasse |
| `pointer-events-none` | Empêche un décor d’intercepter le pointeur |

Une valeur `z-index` plus grande ne franchit pas tous les contextes d’empilement. Une transformation, une isolation ou certains éléments positionnés créent des contextes locaux. `isolation: isolate` dans `.app-shell` délimite volontairement l’empilement du fond et du contenu.

Dans la pile, l’élément d’index `0` reste dans le flux et donne sa taille au conteneur. Les suivants sont absolus. Un conteneur composé uniquement d’enfants absolus peut perdre sa hauteur : c’est un classique à vérifier avant de corriger avec des marges arbitraires.

## 4.6 Dimensions de viewport

`h-screen` correspond à `100vh`. `h-dvh` utilise la hauteur dynamique du viewport, utile lorsque les barres du navigateur mobile apparaissent ou disparaissent. `min-h-dvh` fixe une hauteur minimale tout en permettant à une page de grandir.

La scène `.booster-stage` réserve au moins 560 px, ou 500 px lorsque la hauteur du viewport est au plus 760 px. Cela atténue les sauts lorsque le pack est remplacé par les cartes ; cela ne garantit pas un ajustement parfait sur tous les petits écrans.

Une barre mobile `fixed` ne réserve pas sa hauteur dans le document. Il faudra un espace inférieur approprié pour éviter qu’elle recouvre le dernier contenu.

## 4.7 Responsive : lire sans préfixe, puis avec préfixe

```tsx
<div className="hidden md:block">Navigation bureau</div>
<div className="block md:hidden">Navigation mobile</div>
```

Sans préfixe, la classe s’applique par défaut. `md:` s’applique à partir du breakpoint `md`, pas uniquement sur un type d’appareil. Avec la configuration par défaut de Tailwind, `md` vaut 48 rem, soit habituellement 768 px. Voir [Responsive design](https://tailwindcss.com/docs/responsive-design).

Conséquence concrète : entre 768 et 1023 px, la navigation bureau est visible, tandis que le hook inutilisé `useIsMobile` renverrait encore `true`, car son seuil vaut 1024 px. Si tu branches ce hook un jour, harmonise les seuils ou explique pourquoi ils sont différents.

Les deux navigations sont présentes dans l’arbre React et cachées par CSS. Les effets d’un composant caché peuvent donc quand même s’exécuter ; être masqué n’est pas être démonté.

## 4.8 Couleurs et états interactifs

```tsx
className="bg-[#A78BFA] hover:bg-[#A78BFA]/80 active:scale-95 transition-all duration-200"
```

`[...]` permet une valeur arbitraire. `/80` indique ici une opacité de couleur de 80 %. `hover:` dépend du survol, `active:` de l’activation en cours. `duration-200` indique 200 ms pour une transition CSS.

`transition-colors` limite la transition aux propriétés de couleur concernées ; `transition-transform` aux transformations ; `transition-all` est plus large. Choisis les propriétés réellement animées pour éviter des interpolations inattendues.

Pour le clavier, ajoute des styles `focus-visible:` et conserve un indicateur de focus lisible. Un style de survol seul ne suffit pas à montrer où l’utilisateur navigue au clavier.

## 4.9 Thème sombre

Dans `global.css` :

```css
@custom-variant dark (&:where(.dark, .dark *));
```

Cette règle fait dépendre `dark:` d’une classe `.dark` sur l’élément ou un ancêtre. `ThemeToggle` ajoute ou enlève cette classe sur `<html>`. Voir [Dark mode](https://tailwindcss.com/docs/dark-mode).

```tsx
className="bg-[#E4E4E7] dark:bg-[#232326]"
```

La première couleur est la base ; la seconde s’applique lorsque la variante sombre est active. Plusieurs fonds de l’application sont toutefois codés directement en sombre, sans variante claire : le basculement n’est pas un thème clair complet.

## 4.10 `peer` et sélecteurs avancés

Le champ du thème a `className="sr-only peer"`. `sr-only` le retire visuellement tout en le conservant pour les technologies d’assistance. `peer-checked:` permet de modifier un frère suivant lorsque ce champ est coché.

```tsx
peer-checked:[&>span]:translate-x-6
```

Lecture : quand le peer est coché, cibler les `span` enfants directs de cet élément et les translater horizontalement. C’est un sélecteur CSS conditionnel, pas du JavaScript.

Le champ n’est actuellement pas contrôlé par `checked={toggleButton}` : son état natif et l’état React représentent deux informations distinctes. Voir le diagnostic pour comprendre la désynchronisation initiale.

## 4.11 Classes dynamiques : préférer des chaînes complètes

`cardThemes` stocke des classes entières comme `border-blue-400`. Tailwind peut les repérer dans les sources. Construire `"bg-" + color + "-500"` ne permet pas de détecter toutes les classes possibles à partir du texte source. Voir [Detecting classes in source files](https://tailwindcss.com/docs/detecting-classes-in-source-files).

Les valeurs continues, comme l’angle du pointeur, se prêtent mieux à des variables CSS ou à des styles qu’à des milliers de noms de classe possibles.

Plusieurs classes concurrentes pour la même propriété ne constituent pas une liste fiable d’étapes. La bordure shiny contient plusieurs `via-*` : cela n’ajoute pas automatiquement une étape indépendante par couleur. Il faut inspecter le dégradé calculé ou écrire explicitement le dégradé voulu en CSS.

## 4.12 Transitions, animations et `@theme`

Une **transition** interpole lorsqu’une propriété change de valeur. Une **animation avec keyframes** définit sa propre séquence dans le temps.

```css
@theme {
  --animate-background: background-move ease infinite;
  @keyframes background-move {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
}
```

Code actuel : le token crée l’utilitaire `animate-background`. La carte lui donne une durée avec `[animation-duration:2s]`. Le fond est plus grand que la boîte avec `bg-size-[300%_200%]`, ce qui permet de voir le dégradé se déplacer.

## 4.13 Réduire les animations

Le projet neutralise déjà les particules, la secousse, le balayage shiny et l’inclinaison via `prefers-reduced-motion: reduce`. La bordure animée et les animations Motion n’ont pas toutes une adaptation explicite. Vérifie chaque couche plutôt que de supposer qu’une seule règle coupe toutes les animations.

## Méthode pour déboguer une mise en page

1. Sélectionne la boîte dans les outils du navigateur.
2. Lis sa largeur, sa hauteur, son padding et son positionnement calculés.
3. Active l’affichage des axes flex ou des pistes grid.
4. Désactive une propriété suspecte à la fois.
5. Vérifie le parent avant de compenser dans l’enfant.

Exercice : refais la structure d’une carte avec du CSS simple, puis traduis-la en Tailwind. Si tu ne sais pas traduire une classe en propriété, prends le temps d’étudier cette propriété.
