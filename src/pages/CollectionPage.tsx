import GameCard from "../features/cards/GameCard";

export default function CollectionPage() {
    return (
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 justify-items-center items-start content-start gap-14 min-h-dvh p-8 bg-neutral-100 dark:bg-[#18181B]">
            <GameCard
                name="Stardew Valley"
                resume="Transforme une ferme abandonnée en un petit paradis : cultures, pêche, exploration et rencontres au village."
                rating={9.2}
                image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/413150/header.jpg"
                rarity="common"
            />

            <GameCard
                name="Hollow Knight"
                resume="Explore un royaume souterrain oublié, affronte des créatures redoutables et découvre les secrets de Hallownest."
                rating={9.5}
                image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/367520/header.jpg"
                rarity="uncommon"
            />

            <GameCard
                name="Cyberpunk 2077"
                resume="Deviens mercenaire à Night City, une mégalopole où implants cybernétiques, pouvoir et trahisons façonnent ton destin."
                rating={8.8}
                image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1091500/header.jpg"
                rarity="rare"
            />

            <GameCard
                name="The Witcher 3"
                resume="Incarne Geralt de Riv et traque des monstres dans un monde où chaque contrat cache des choix difficiles."
                rating={9.7}
                image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/292030/header.jpg"
                rarity="epic"
            />

            <GameCard
                name="Elden Ring"
                resume="Parcours l’Entre-terre, défie des demi-dieux déchus et forge ta légende dans un vaste monde de dark fantasy."
                rating={9.8}
                image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/header.jpg"
                rarity="legendary"
            />
        </div>
    );
}