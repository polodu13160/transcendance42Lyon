import GameCard from "@/features/cards/GameCard";
import type { CollectionEntry } from "@/types/card";

interface CollectionItemProps {
    cardInfo: CollectionEntry;
}

export default function CollectionItem({ cardInfo }: CollectionItemProps) {
    return (
        <div className="w-full min-w-0">
            <GameCard {...cardInfo.card} className="w-full" responsive />
            <p className="mt-2 text-xs text-zinc-500">{cardInfo.quantity} in collection</p>
        </div>
    );
}
