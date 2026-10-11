export type Rarity =
    | "common"
    | "uncommon"
    | "rare"
    | "ultra-rare"
    | "legendary";

export type GameCard = {
    id: number;
    name: string;
    imageUrl: string;
    description: string;
    funfact: string;

    rating: number;
    reviewCount: number;
    rarity: Rarity;
    isShiny: boolean;
};