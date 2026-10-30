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

                {
                    cardInfo.quantity > 1
                        ?   <div className="absolute top-3 right-3 h-8 font-bold w-8 z-30 rounded-full bg-red-400 flex  justify-center items-center text-[#F5F5F5]">
                               <span>x{cardInfo.quantity}</span>
                            </div>
                        : null
                }
            </div>
        </div>
    );
}
