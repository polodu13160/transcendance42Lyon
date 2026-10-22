import { cardThemes } from "./cardThemes";

type GameCardProps = {
    rarity: keyof typeof cardThemes; 
    name: string,
    rating: number,
    resume: string,
    image: string,
    isShiny: boolean,
    isGame: boolean
}

export default function CardBack({ rarity, name, rating, image , resume, isShiny, isGame}: GameCardProps) {

    <div className="relative w-75 overflow-hidden rounded-2xl p-1.5">

        <div className="relative z-10 flex aspect-2/3 flex-col overflow-hidden rounded-xl bg-purple-400">
        
        </div>

    </div>


}