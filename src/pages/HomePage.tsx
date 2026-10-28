// import GameCard from "../features/cards/GameCard"
// import testData from "../../test_data/cardsData.json"
// import BoosterOpening from "@/features/boosters/BoosterOpening"
// import logo_dark from "../assets/logo/logo_dark.svg"
import { useState } from "react"
import type { CollectionCard } from "../types/card";

import "../features/boosters/boosterStyle.css"

import cardsData from "../../test_data/cardsData.json";
import BoosterOpening from "@/features/boosters/BoosterOpening";
import boosterImg from "../assets/Booster.svg"



const cards = cardsData as CollectionCard[];

function getRandomCards(): CollectionCard[] {
    return [...cards]
        .sort(() => Math.random() - 0.5)
        .slice(0, 5);
}




export type BoosterTiming = "idle" | "opening" | "revealed"

const enabledButtonClass = "text-[#F5F5F5] bg-[#A78BFA] hover:bg-[#A78BFA]/80 active:bg-[#352B48] border-sky-800 border p-2 rounded cursor-pointer select-none font-bold w-48 transition-all duration-200 ease-in-out active:scale-95"
const disabledButtonClass = "text-[#71717A] bg-[#352B48]/40 border border-[#352B48] p-2 rounded cursor-not-allowed select-none font-bold w-48 opacity-50"


const boosterAnimated = "scale-120 m-5 booster-shake brightness-50"
const boosterWait = "scale-120 m-5"


export default function HomePage() {
    
    const [boosterState, setBoosterState] = useState<BoosterTiming>("idle")
    const [buttonState, setButtonState] = useState(false) 
    const [incrementPacks, setIncrementPack] = useState(0)    
    const [boosterCards, setBoosterCards] = useState<CollectionCard[]>([]);

    function handleBoosterState() {

        if (boosterState === "idle") {
            setBoosterState("opening")
            setButtonState((prevState) => !prevState)
            setTimeout(() => {
                setBoosterState("revealed")
                setBoosterCards(getRandomCards());
                setIncrementPack(prevpack => prevpack + 1)
            }, 1000)
        }
        return;
    }

    function showNewPack() {
        setButtonState(false);
        setBoosterState("idle")
    }

    function boosterClass() {

        if (boosterState === "idle")
            return boosterWait
        else if (boosterState === "opening")
            return boosterAnimated
    }



    return (
        <div className="scale-70 md:scale-100 relative flex min-h-dvh flex-col items-center justify-center gap-6 px-4 py-8">
            {/* <img src={logo_dark} className="md:block w-full h-auto pb-10 pt-5 scale-90"/> */}

            <div className="booster-stage relative z-10 flex w-full items-center justify-center">
                {
                    boosterState === "revealed"
                    ?           <div className="relative">
                                <BoosterOpening cardsPack={boosterCards} resetFunction={showNewPack} key={incrementPacks} />
                            </div>
                    :           <img src={boosterImg} className={boosterClass()} />
                }
            </div>

            <div className="relative z-10 flex flex-col items-center gap-3 text-center">
                <h1 className="text-xl font-bold text-[#C4B5FD]" >Bienvenue sur GatchaGames</h1>
                <p className="max-w-xl text-[#D4D4D8]">GatchaGames est une plateforme en ligne de jeu et collection de carte sur l'univers du jeu-vidéo</p>
                <button disabled={buttonState} onClick={handleBoosterState} className={buttonState ? disabledButtonClass : enabledButtonClass} >Ouvrir un booster</button>
            </div>
        </div>
    )
}
