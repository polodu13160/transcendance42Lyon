import type { CardRarity } from "./card";

export interface GameProps {
    id: number;
    name: string;
    imageUrl: string;
    description: string;
    funfact: string;

    rating: number;
    reviewCount: number;
    rarity: CardRarity;
    isShiny: boolean;
};
