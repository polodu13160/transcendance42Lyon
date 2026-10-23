import GameCard from "../features/cards/GameCard";
import type { GameCardProps } from "../features/cards/GameCard";
import cardsData from "../../test_data/cardsData.json";

const cards = cardsData as (GameCardProps & { id: string })[];
const browseCards = Array.from({ length: 50 }, (_, index) => ({
    ...cards[index % cards.length],
    instanceId: index,
}));

export default function Browse() {
    return (
        <div className="min-h-screen bg-neutral-100 px-4 py-8 dark:bg-[#18181B]">
            <div className="mx-auto grid max-w-[120rem] grid-cols-[repeat(auto-fill,18.75rem)] justify-center gap-6">
                {browseCards.map(({ instanceId, ...card }) => (
                    <GameCard key={instanceId} {...card} />
                ))}
            </div>
        </div>
    )
}
