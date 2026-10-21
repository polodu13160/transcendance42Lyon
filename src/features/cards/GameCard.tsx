import { FaStar } from "react-icons/fa";
import { GiBouncingSword } from "react-icons/gi";
import { FaShieldAlt } from "react-icons/fa";
import { cardThemes } from "./cardThemes";
import { TiltCard } from "./TiltCard";
import { SparkleParticles } from '@/components/lightswind/sparkle-particles';
import { BackgroundBeams } from "@/components/ui/beams";

type GameCardProps = {
    rarity: keyof typeof cardThemes; 
    name: string,
    rating: number,
    resume: string,
    image: string,
    isShiny: boolean,
    isGame: boolean
}

export default function GameCard({ rarity, name, rating, image , resume, isShiny, isGame}: GameCardProps) {

    const theme = cardThemes[rarity]
    
    return (
        <TiltCard max={16}>
                <div className={`${theme.cardBorder} relative w-75 overflow-hidden rounded-2xl p-1.5`}>
                    <div className={`relative z-10 flex aspect-2/3 flex-col overflow-hidden rounded-xl ${theme.backGround}`}>
                    {
                        isShiny && 
                        <>
                           <BackgroundBeams color={theme.beamColor} />
                            <SparkleParticles className="absolute inset-0"  baseDensity={150} maxParticleSize={1.5} opacityAnimationSpeed={5} enableCollisions={true}   particleShape="star"/>
                        </>
                    }
                        <div className={`relative flex-1 min-h-0 overflow-hidden m-0.5 rounded-xl border shadow-xl  border-[#3F3F46]`}>
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
                                {
                                    isGame
                                    ? <span className="font-light text-gray-400">Game</span>
                                    : <span className="font-light text-gray-400">DLC</span>
                                }
                            </div>
                            <div className="mt-2">
                                <p className="mx-4 font-normal text-xs text-[#B7C0CD]">{resume}</p>
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