import { FaStar } from "react-icons/fa";
import { cardThemes } from "./cardThemes";
import { TiltCard } from "./TiltCard";


type GameCardProps = {
    rarity: keyof typeof cardThemes; 
    name: string,
    rating: number,
    resume: string,
    image: string   
}

export default function GameCard({ rarity, name, rating, image , resume}: GameCardProps) {

    const theme = cardThemes[rarity]
    
    return (
        <TiltCard>
            <div className={`${theme.cardBorder} w-75 rounded-2xl p-1.5`}>
                <div className={`flex flex-col aspect-2/3 overflow-hidden rounded-xl ${theme.backGround}`}>

                    <div className={`relative flex-1 min-h-0 overflow-hidden m-0.5 rounded-xl border  border-[#3F3F46]`}>
                        <img
                            src={image}
                            alt={name}  
                            className="h-full w-full object-cover"
                        />
                        <div className={`z-10 absolute bottom-2 right-2 bg-[#2D2D32] py-1 px-2 rounded-lg border ${theme.badge} font-bold text-base`}>
                            <span>{theme.rarityName}</span> 
                        </div>
                    </div>

                    <div className="flex-1 min-h-0 flex flex-col">
                        <h2 className="text-2xl text-white font-bold ml-4 mt-2" >{name}</h2>
                        <div className="flex flex-row justify-left items-center ml-4">
                            <FaStar className="text-[#FFC637]"/>
                            <span className="ml-1 font-bold text-white text-xl">{rating}</span>
                            <span className="mx-4 h-4 w-px bg-gray-500"/>
                            <span className="font-light text-gray-400">363 248 reviews</span>
                        </div>
                        <div className="mt-2">
                            <p className="mx-4 font-normal text-sm text-[#B7C0CD]">{resume}</p>
                        </div>

                        <div className="mx-4 flex-1 flex flex-row justify-between items-center text-base font-bold text-white">
                            <div className="bg-slate-800 rounded-2xl p-3 border-red-400 border">9000 ATQ</div>
                            <div className="bg-slate-800 rounded-2xl p-3 border-blue-400 border">8500 DEF</div>
                        </div>
                    </div>

                </div>
            </div>
        </TiltCard>
    )
}