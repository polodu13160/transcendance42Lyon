# 3. React : penser en composants et en état

## 3.1 Un composant est une fonction qui décrit une interface

```tsx
type GreetingProps = { name: string };

function Greeting({ name }: GreetingProps) {
  return <h1>Bienvenue {name}</h1>;
}
```

Exemple pédagogique. Le JSX ressemble au HTML, mais fait partie de JavaScript. `{name}` insère une expression. `className` correspond à l’attribut de classe. Un composant commence par une majuscule ; `<Greeting />` appelle le mécanisme de rendu de React, tandis que `<h1>` désigne un élément natif.

Un fichier `.tsx` autorise TypeScript et JSX. L’option `jsx: "react-jsx"` évite d’avoir à importer `React` uniquement pour écrire du JSX. Certains fichiers l’importent néanmoins pour utiliser `React.useState` ou ses types.

## 3.2 Props : les entrées d’un composant

`GameCard` reçoit `name`, `rating`, `resume`, `image`, `rarity`, `isShiny` et `isGame`. Il affiche ces entrées. Il ne choisit pas lui-même le contenu du booster.

Les props sont lues comme des valeurs fournies par le parent. Pour demander une action au parent, l’enfant appelle une fonction reçue en prop.

```text
HomePage détient boosterCards
    ↓ cardsPack
BoosterOpening affiche la pile
    ↑ appelle resetFunction()
HomePage décide du retour à idle
```

Le flux des données descend ; les callbacks permettent de signaler une intention vers le haut. Cela conserve une responsabilité claire pour chaque état.

## 3.3 `children` : composer sans connaître le contenu

Dans `Modal`, `TiltCard` et `RevealCard`, `ReactNode` autorise du contenu React : élément, texte, fragment, etc.

```tsx
<Modal onClose={closeModal}>
  <LoginForm />
</Modal>
```

`Modal` gère le cadre et la fermeture. `LoginForm` gère son contenu. Le parent décide de les associer. Un fragment `<>...</>` regroupe plusieurs éléments sans ajouter de boîte HTML.

## 3.4 `useState` : mémoire et prochain rendu

Extrait actuel de l’accueil :

```tsx
const [boosterState, setBoosterState] = useState<BoosterTiming>("idle");
```

Le premier élément du couple est la valeur du rendu actuel. Le second permet de demander une nouvelle valeur. Le changement conduit React à recalculer l’interface.

Une variable locale ordinaire repart de sa déclaration au prochain appel du composant. Un état persiste tant que React conserve l’identité du composant dans l’arbre. Voir [l’état comme mémoire d’un composant](https://react.dev/learn/state-a-components-memory).

```tsx
setVisibleIndex(previous => previous - 1);
console.log(visibleIndex);
```

Le log lit toujours la valeur capturée par la fonction du rendu courant. Le setter ne réécrit pas cette variable locale. C’est crucial pour comprendre la vérification `visibleIndex === 0` à la fin d’un booster.

## 3.5 Le cycle d’affichage

```text
Événement → demande de mise à jour → rendu React → modifications DOM → affichage navigateur
```

Le **rendu** appelle les composants pour calculer la description de l’interface. Le **commit** applique les changements nécessaires au DOM. Le navigateur effectue ensuite son propre travail d’affichage. Un rendu React ne signifie pas que toute la page est détruite puis reconstruite. Voir [Render and Commit](https://react.dev/learn/render-and-commit).

Évite de lancer un timer ou de modifier le DOM directement dans le corps d’un composant : ce travail se reproduirait au rythme des rendus. Une interaction se traite dans un événement ; une synchronisation externe peut se traiter dans un effet.

## 3.6 Événements et callbacks

```tsx
function closeModal(): void {
  setActiveModal(null);
}
```

Cette fonction appartient à `App`, car `App` détient `activeModal`. Elle descend jusqu’au bouton de fermeture grâce à la prop `onClose`.

Dans `RevealCard`, le clic appelle `flipCard`, qui modifie son état local `flip`, puis appelle `swapFunction`. Deux actions distinctes se produisent : la face devient la cible de l’animation et le parent autorise le drag.

Un nom comme `onReveal` expliquerait mieux l’événement que `swapFunction`. Le comportement dépend du contrat de la fonction, pas de son nom.

## 3.7 Rendu conditionnel

```tsx
{activeModal !== null && <Modal onClose={closeModal}>...</Modal>}
```

Quand la condition devient fausse, ce composant quitte l’arbre : il est **démonté**. Son état local est perdu. S’il revient plus tard à la même place après avoir été absent, c’est une nouvelle instance.

L’accueil utilise un ternaire : si l’état vaut `revealed`, afficher les cartes ; sinon afficher l’illustration du pack. Ce choix explique pourquoi la pile n’existe pas avant la révélation.

## 3.8 Listes et identité avec `key`

```tsx
cards.map(card => <GameCard key={card.id} {...card} />)
```

Exemple de liste fondée sur des identifiants uniques. Une clé aide React à reconnaître un enfant parmi ses frères. Ce n’est pas une prop automatiquement disponible dans l’enfant. Pour l’utiliser dans le composant, passe aussi une prop `id`.

L’index est fragile quand les éléments changent d’ordre, sont insérés ou remplacés : l’état peut rester attaché à une position plutôt qu’au bon objet. Dans la pile actuelle, l’ordre reste fixe et les suppressions se font par le dessus ; `key={index}` est moins problématique dans ce cas précis, mais un identifiant stable facilite les évolutions.

Dans `HomePage`, `key={incrementPacks}` sur `BoosterOpening` exprime une nouvelle identité à chaque pack. La pile est déjà démontée lorsque l’accueil retourne à `idle` ; le changement de clé renforce donc une remise à zéro également obtenue par ce démontage.

## 3.9 Où mettre l’état ?

| État actuel | Propriétaire | Raison |
| --- | --- | --- |
| `activeModal` | `App` | Navigation et contenu doivent ouvrir la même modale |
| `boosterState`, `boosterCards` | `HomePage` | Contrôle du parcours et du résultat du tirage |
| `visibleIndex`, `dragOn`, `swapDirection` | `BoosterOpening` | Contrôle de la pile |
| `flip` | Chaque `RevealCard` | Chaque carte doit retenir son propre retournement |
| `toggleButton` | `ThemeToggle` | Pilote la classe de thème globale |
| `menuState` | `MoreButton` | Ouverture du menu mobile |

Règle de travail : place l’état au plus proche ancêtre commun des composants qui doivent le lire ou le modifier. Un état trop haut rend les dépendances inutiles ; trop bas, il oblige à dupliquer l’information.

`buttonState` pourrait être dérivé de `boosterState !== "idle"`. Deux états qui expriment la même information peuvent se contredire si un chemin met à jour l’un en oubliant l’autre.

## 3.10 `useRef` : garder un accès sans demander de rendu

```tsx
const cardRef = useRef<HTMLDivElement>(null);
```

Dans `TiltCard`, `ref={cardRef}` permet ensuite d’accéder à l’élément DOM via `cardRef.current`. Avant le montage, ou après le démontage, la valeur peut être `null` : il faut la vérifier.

Changer `.current` ne déclenche pas un rendu. Les positions de pointeur sont fréquentes : le composant modifie des variables CSS pour l’inclinaison plutôt que de déclencher un état React à chaque déplacement. Il faut éviter que React et une manipulation directe pilotent la même propriété sans règle claire.

## 3.11 `useEffect` : synchroniser et nettoyer

Extrait actuel du thème :

```tsx
React.useEffect(() => {
  document.documentElement.classList.toggle("dark", toggleButton === true);
}, [toggleButton]);
```

L’état React est synchronisé avec une classe sur `<html>`, un objet extérieur au composant. Le tableau de dépendances indique les valeurs qui gouvernent cette synchronisation. Un effet n’est pas nécessaire pour un calcul directement dérivable des props et de l’état. Voir [Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects).

Pour un abonnement, retourne le nettoyage :

```tsx
useEffect(() => {
  const update = () => setWidth(window.innerWidth);
  window.addEventListener("resize", update);
  return () => window.removeEventListener("resize", update);
}, []);
```

Extrait pédagogique à placer dans un composant ayant un état `width`. La même fonction `update` doit servir à ajouter et à enlever l’écouteur. Le hook `use-mobile` suit cette idée.

Un timer peut aussi nécessiter un nettoyage lorsqu’un composant quitte la page ; l’accueil actuel ne le fait pas encore.

## 3.12 Règles des hooks

Appelle les hooks au niveau supérieur d’un composant ou d’un autre hook, avant les retours conditionnels éventuels. Ne les appelle pas dans une boucle, une condition ou une callback de clic. React doit retrouver un ordre d’appels cohérent à chaque rendu.

Un hook personnalisé, comme `useIsMobile`, réutilise une logique avec ses hooks. Il ne partage pas automatiquement un même état entre tous ses utilisateurs. Le hook de toasts du dépôt partage, lui, une mémoire de module explicitement construite pour cela.

## À reconstruire sans modèle

Crée un parent qui possède `isOpen`, un bouton qui l’ouvre et un enfant qui reçoit `onClose`. Ajoute ensuite un compteur dans l’enfant. Ferme et rouvre : prédis si le compteur repart de zéro, puis vérifie. Explique le résultat avec le montage et le démontage.
