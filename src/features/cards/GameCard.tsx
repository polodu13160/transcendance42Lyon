import { FaStar } from "react-icons/fa";
import { GiBouncingSword } from "react-icons/gi";
import { FaShieldAlt } from "react-icons/fa";
import { cardThemes } from "./cardThemes";
import { TiltCard } from "./TiltCard";
import { GiPolarStar } from "react-icons/gi";

import "./CardEffects.css"


export type GameCardProps = {
    rarity: keyof typeof cardThemes; 
    name: string,
    rating: number,
    resume: string,
    image: string,
    isShiny: boolean,
    isGame: boolean
}

const shinyBorder = "animate-background bg-linear-to-br from-red-500 via-orange-500 select-none via-yellow-500 via-green-500 via-blue-500 via-indigo-500 to-purple-500 relative w-75 overflow-hidden rounded-2xl p-1.5 bg-size-[300%_200%] [animation-duration:2s]"

export default function GameCard({ rarity, name, rating, image , resume, isShiny, isGame}: GameCardProps) {

    const theme = cardThemes[rarity]
    
    return (
        <TiltCard max={25} select-none>
                <div className={ !isShiny ?
                                 `${theme.cardBorder} relative w-75 overflow-hidden rounded-2xl p-1.5 select-none`
                                : shinyBorder
                                }>
                    <div className={ !isShiny ?
                            `relative z-10 flex aspect-2/3 flex-col overflow-hidden rounded-xl ${theme.backGround}`
                            : `relative z-10 flex aspect-2/3 flex-col overflow-hidden rounded-xl ${theme.shinyBack} `
                        }>
                        {isShiny && (
                            <>
                                <div className="shiny-waves" aria-hidden="true" />
                                <div className="shiny-sweep" aria-hidden="true" />
                            </>
                        )}
                        {isShiny && (
                            <div className="pointer-events-none absolute inset-0 z-20 overflow-hidden">
                                <div className="shiny-sweep" />
                            </div>
                        )}
                        <div className={`relative z-5 flex-1 min-h-0 overflow-hidden m-0.5 rounded-xl border shadow-xl  border-[#3F3F46]`}>
                            <img
                                src={image}
                                alt={name}  
                                draggable={false}
                                className="h-full w-full object-cover"
                            />
                            <div className={`z-10 absolute flex flex-row justify-center items-center bottom-2 gap-1 right-2 bg-[#2D2D32] py-1 px-2 rounded-lg border ${theme.badge} font-bold text-base`}>
                                <span>{theme.rarityName}</span>
                                {   
                                    isShiny &&
                                    <GiPolarStar className="white"/>
                                }
                            </div>
                        </div>

                        <div className="flex-1 min-h-0 flex flex-col">
                            <h2 className="text-2xl text-white font-bold ml-4 mt-2" >{name}</h2>
                            <div className="flex flex-row justify-left items-center ml-4">
                                <FaStar className="text-[#FFC637]"/>
                                <span className="ml-1 font-bold text-white text-xl">{rating}</span>
                                <span className="mx-4 h-4 w-px bg-gray-500"/>
                                {
                                    isGame
                                    ? <span className="font-light text-gray-400">Game</span>
                                    : <span className="font-light text-gray-400">DLC</span>
                                }
                            </div>
                            <div className="mt-2">
                                <p className="mx-4 font-normal text-xs text-white">{resume}</p>
                            </div>

                            <div className="m-4 flex-1 flex flex-row justify-between items-center text-base font-bold text-white">
                                <div className="border rounded-3xl p-2 flex flex-row gap-1 justify-center items-center">
                                    <GiBouncingSword className="text-white" />
                                    <span>9000</span>
                                </div>                                
                                <div className="border rounded-3xl p-2 flex flex-row gap-1 justify-center items-center">
                                    <FaShieldAlt className="text-white" />
                                    <span>7432</span>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
        </TiltCard>
    )
}