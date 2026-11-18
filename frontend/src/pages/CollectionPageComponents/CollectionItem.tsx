import GameCard from "@/features/cards/GameCard";
import type { CollectionEntry } from "@/types/card";

interface CollectionItemProps {
    cardInfo: CollectionEntry;
}

export default function CollectionItem({ cardInfo }: CollectionItemProps) {
    return (
        <div>
            <div className="w-full min-w-0 relative">
                <GameCard {...cardInfo.card} className="w-full" responsive />
                <div className="flex flex-row justify-start">
                    <p className="mt-2 text-xs text-muted">{cardInfo.quantity} in collection</p>
                    {
                        cardInfo.isFavorite
                        ? <p className="ml-1 mt-2 text-xs text-muted">· Favorite</p>
                        : null
                    }
                </div>

            </div>
        </div>
    );
}
