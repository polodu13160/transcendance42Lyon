import GameCard from "@/features/cards/GameCard";
import type { GameCardProps } from "@/types/card";


export default function MarketItem(props: GameCardProps) {
    return <GameCard {...props} />;
}
