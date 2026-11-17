import { FaStar } from "react-icons/fa";
import { GiBouncingSword } from "react-icons/gi";
import { FaShieldAlt } from "react-icons/fa";
import { cardThemes } from "./cardThemes";
import { TiltCard } from "./TiltCard";
import { GiPolarStar } from "react-icons/gi";
import type { GameCardProps } from "../../types/card";

import "./CardEffects.css"
import "./GameCardResponsive.css"

const shinyBorder = "animate-background bg-linear-to-br from-red-500 via-orange-500 select-none via-yellow-500 via-green-500 via-blue-500 via-indigo-500 to-purple-500 relative overflow-hidden rounded-2xl p-1.5 bg-size-[300%_200%] [animation-duration:2s]"

type CardDisplayProps = GameCardProps & {
    className?: string;
    responsive?: boolean;
};

export default function GameCard({ rarity, name, rating, image , resume, isShiny, isGame, className = "w-75", responsive = false }: CardDisplayProps) {

    const theme = cardThemes[rarity]

    return (
        <TiltCard max={8} className={responsive ? "w-full @container touch-pan-y!" : "w-fit"}>
                <div style={{ fontFamily: '"Ubuntu", sans-serif' }} className={`${className} ${responsive ? "game-card-responsive" : ""} ${!isShiny ?
                                 `${theme.cardBorder} relative overflow-hidden rounded-2xl p-1.5 select-none`
                                : shinyBorder
                                }`}>
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
                        <div className={`relative z-5 flex-1 min-h-0 overflow-hidden m-0.5 rounded-xl border shadow-xl  border-border`}>
                            <img
                                src={image}
                                alt={name}  
                                draggable={false}
                                className="h-full w-full object-cover"
                            />
                            <div className={`card-rarity z-10 absolute flex flex-row justify-center items-center bottom-2 gap-1 right-2 bg-surface-raised py-1 px-2 rounded-lg border ${theme.badge} font-bold text-base`}>
                                <span>{theme.rarityName}</span>
                                {   
                                    isShiny &&
                                    <GiPolarStar className="text-white"/>
                                }
                            </div>
                        </div>

                        <div className="card-content flex-1 min-h-0 flex flex-col">
                            <h2
                                className={`mx-4 mt-2 flex h-7 shrink-0 items-center justify-start whitespace-nowrap text-center font-bold text-white ${
                                    name.length > 30
                                    ? "text-sm"
                                    : name.length > 20
                                        ? "text-base"
                                        : "text-lg"
                                }`}
                            >{name}</h2>
                            <div className="card-rating flex flex-row justify-start items-center ml-4">
                                <FaStar className="text-[#FFC637]"/>
                                <span className="ml-1 font-bold text-white text-xl">{rating}</span>
                                <span className="mx-4 h-4 w-px bg-border"/>
                                {
                                    isGame
                                    ? <span className="font-light text-muted">Game</span>
                                    : <span className="font-light text-muted">DLC</span>
                                }
                            </div>
                            <div className="card-description mt-2 h-12 shrink-0">
                                <p className="mx-4 font-normal text-xs leading-4 italic text-white line-clamp-3">{resume}</p>
                            </div>

                            <div className="card-stats m-4 flex-1 flex flex-row justify-between items-center text-base font-bold text-white">
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
