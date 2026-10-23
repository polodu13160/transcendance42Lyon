
import { useState } from "react";
import type { GameCardProps } from "../features/cards/GameCard";
import cardsData from "../../test_data/cardsData.json";
import BoosterOpening from "@/features/boosters/BoosterOpening";

type CollectionCard = GameCardProps & {
    id: string;
};

const cards = cardsData as CollectionCard[];

function getRandomCards(): CollectionCard[] {
    return [...cards]
        .sort(() => Math.random() - 0.5)
        .slice(0, 5);
}

export default function CollectionPage() {
    const [boosterCards, setBoosterCards] = useState<CollectionCard[]>([]);

    function openBooster() {
        setBoosterCards(getRandomCards());
    }

    return (
        <div className="h-screen bg-slate-500 dark:bg-[#18181B] flex flex-col justify-center items-center">
            <div className="relative">
                <BoosterOpening cardsPack={boosterCards} />
            </div>

            <div className="mt-4 flex flex-col">
                <span>Remaining boosters : 5</span>
                <button className="border" onClick={openBooster}>
                    Open Pack
                </button>
            </div>
        </div>
    );
}
