export type CardRarity =
    | "common"
    | "uncommon"
    | "rare"
    | "epic"
    | "legendary";

export interface GameCardProps {
    rarity: CardRarity;
    name: string,
    rating: number,
    resume: string,
    image: string,
    isShiny: boolean,
    isGame: boolean
}

export type CollectionCard = GameCardProps & {
    id: string;
};
