import CardBack from "@/features/cards/CardBack";
import GameCard from "@/features/cards/GameCard";
import RevealCard from "@/features/cards/RevealCard";

export default function MarketPage() {
    return (
        <div className="flex h-screen w-auto flex-col items-center justify-center gap-14 relative">
            <div>
                <RevealCard
                    front={<GameCard rarity="legendary" name="LOL" rating={9.4} resume="asbkafkjfkfbasjkbfkbajkfbs" isGame={true} isShiny={true} image="https://cdn.akamai.steamstatic.com/steam/apps/1593500/header.jpg" />}
                    back={<CardBack/>}
                />
            </div>
        </div>
    )
}
