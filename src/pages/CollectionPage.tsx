import GameCard from "../features/cards/GameCard";
import type { GameCardProps } from "../features/cards/GameCard";
import cardsData from "../../test_data/cardsData.json";

type CollectionCard = GameCardProps & {
    id: string;
};

const cards = cardsData as CollectionCard[];

export default function CollectionPage() {
    return (
        <div className="h-screen bg-slate-500 dark:bg-[#18181B] flex flex-col justify-center items-center">
            <div className="relative">
                {cards.map((card, index: number) => (
                    <div className={index === 0 ?
                                    ""
                                    : "absolute top-0"} 
                    key={card.id}>
                        <GameCard
                            name={card.name}
                            resume={card.resume}
                            rating={card.rating}
                                image={card.image}
                            rarity={card.rarity}
                            isShiny={card.isShiny}
                            isGame={card.isGame}
                        />
                    </div>
                ))}
            </div>
            <div className="mt-4 gap-5 flex flex-col">
                <span className="">Remaining boosters : 5</span>
                <button className="border">Open Pack</button>
            </div>
        </div>
    );
}