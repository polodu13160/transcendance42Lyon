// import GameCard from "../features/cards/GameCard"
// import testData from "../../test_data/cardsData.json"
// import BoosterOpening from "@/features/boosters/BoosterOpening"
// import logo_dark from "../assets/logo/logo_dark.svg"
import { useState } from "react"

import boosterImg from "../assets/Booster.svg"


export type BoosterTiming = "idle" | "opening" | "revealed"

const enabledButtonClass = "text-[#F5F5F5] bg-[#A78BFA] hover:bg-[#A78BFA]/80 active:bg-[#352B48] border-sky-800 border p-2 rounded cursor-pointer select-none font-bold w-48 transition-all duration-200 ease-in-out active:scale-95"
const disabledButtonClass = "text-[#71717A] bg-[#352B48]/40 border border-[#352B48] p-2 rounded cursor-not-allowed select-none font-bold w-48 opacity-50"



export default function HomePage() {
    
    const [boosterState, setBoosterState] = useState<BoosterTiming>("idle")
    const [buttonState, setButtonState] = useState(false) 

    function handleBoosterState() {

        if (boosterState === "idle") {
            setButtonState((prevState) => !prevState)
            setBoosterState("opening")
        }
        return;
    }



    return (
        <div className="flex flex-col justify-center items-center w-auto h-dvh gap-6 bg-neutral-100 dark:bg-[#18181B]">
            {/* <img src={logo_dark} className="md:block w-full h-auto pb-10 pt-5 scale-90"/> */}
            <img src={boosterImg} />
            <h1 className="text-xl font-bold text-[#A78BFA]" >Bienvenue sur GatchaGames : {boosterState} {buttonState ? "true" : "false"}</h1>
            <p className="text-[#F5F5F5]">GatchaGames est une plateforme en ligne de jeu et collection de carte sur l'univers du jeu-vidéo</p>
            <button disabled={buttonState} onClick={handleBoosterState} className={buttonState ? disabledButtonClass : enabledButtonClass} >Ouvrir un booster</button>
        </div>
    )
}  