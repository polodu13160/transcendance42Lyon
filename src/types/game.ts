export type GameCard = {

    id: number;
    name: string;
    imageUrl: string;
    resume: string;
    
    // For rarity and attack/defense power
    rating: number;
    reviewNumber: number;
    rarity: rarity
    isShiny: boolean;
}

export type rarity =  "common" | "uncommon" | "rare" | "ultra-rare" | "legendary";