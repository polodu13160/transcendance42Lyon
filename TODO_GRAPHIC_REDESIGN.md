# Refonte graphique — Electric Citron

Branche de travail : `frontend/graphic-redesign`.
Référence : `kaissott/mygatchagames-electric-citron`, branche `main`, commit `36777146156c6fe56c30d4baaa410071293a484b`.

La dernière version du dépôt Citron utilise une palette arcade : bleu nuit, cyan et actions jaunes. Adapter les éléments visuels dans le dépôt de base, en conservant les changements fonctionnels récents. Les écrans proposés dans les notes de conception ne sont pas tous implémentés dans Citron.

## 1. Retrouver une base affichable

- [ ] Terminer le rendu de la grille de collection : son JSX contient actuellement une fermeture sans boucle correspondante.
- [ ] Vérifier que le frontend démarre et relever les éventuelles erreurs de compilation avant la refonte.

## 2. Définir le thème commun

- [ ] Centraliser les couleurs de fond, surfaces, texte, accent, bordures et états interactifs dans le thème global.
- [ ] Reprendre les références sombres actualisées : fond `#111A35`, navigation `#1C2B50`, panneaux `#21345C`, accent cyan `#62DBF5`, actions jaunes `#FFCF56`.
- [ ] Conserver le thème sombre unique demandé et retirer le ThemeToggle ainsi que ses variantes inutilisées.
- [ ] Adapter le fond et les particules au thème Citron. Vérifier aussi la grille du thème clair, encore violette dans la référence.

## 3. Adapter la navigation

- [ ] Harmoniser la barre latérale, la navigation mobile et le menu supplémentaire.
- [ ] Adapter les liens actifs, les survols, les séparateurs et les boutons de connexion/inscription.
- [ ] Vérifier la cohérence des logos et icônes dans le thème sombre.
- [ ] Vérifier que le thème sombre est cohérent sur ordinateur et mobile.

## 4. Harmoniser les contrôles partagés

- [ ] Définir une apparence cohérente pour les boutons principaux et secondaires, y compris les états désactivé, survolé, pressé et focus clavier.
- [ ] Appliquer le thème aux recherches, listes de filtres et à la pagination.
- [ ] Adapter les modales et le formulaire de connexion.

## 5. Adapter Open Pack

- [ ] Reprendre les couleurs Citron du booster SVG et du dos des cartes après comparaison des assets.
- [ ] Adapter le bouton d'ouverture et l'écran récapitulatif.
- [ ] Vérifier tout le parcours : attente, ouverture, retournement, swipe des cinq cartes, récapitulatif, nouvelle ouverture.
- [ ] Conserver les couleurs des raretés et les effets shiny : ces couleurs ont un sens distinct de l'accent du site.

## 6. Adapter Collection, puis Market

- [ ] Harmoniser les titres, statistiques, filtres, pagination et informations sous les cartes dans Collection.
- [ ] Conserver le comportement et les changements récents du dépôt de base plutôt que remplacer les pages par celles de Citron.
- [ ] Appliquer les mêmes choix aux composants existants de Market.
- [ ] Distinguer les éléments de Market encore à implémenter des changements purement graphiques.

## 7. Vérifier et terminer

- [ ] Vérifier ordinateur et mobile, thème sombre, débordements et contenu masqué par la navigation.
- [ ] Vérifier les contrastes, le focus clavier et la réduction des animations.
- [ ] Rechercher les anciennes couleurs violettes de l'interface et traiter chaque occurrence selon son rôle, en préservant notamment la rareté Epic.
- [ ] Lancer le build et le lint ; distinguer les erreurs préexistantes de celles introduites par la refonte.
- [ ] Comparer visuellement les pages avec Citron et faire des commits par étape cohérente : thème, navigation, contrôles, boosters, collection, market.

## Après la migration visuelle

Trade, Profile, Settings et Play restent largement des ébauches dans les sources Citron consultées. Leur conception complète constitue un chantier séparé ; ne pas considérer les propositions présentes dans les notes comme des pages déjà fonctionnelles à copier.

**Premier objectif : retrouver une grille de collection affichable avant de changer le thème.**
