import { useState } from "react"
import type { CollectionCard } from "../types/card";
import { motion } from "motion/react"

import "../features/boosters/boosterStyle.css"

import cardsData from "../../test_data/cardsData.json";
import BoosterOpening from "@/features/boosters/BoosterOpening";
import boosterImg from "../assets/Booster.svg"
import CardsResult from "@/features/cards/CardsResult";

const cards = cardsData as CollectionCard[];

function getRandomCards(): CollectionCard[] {
    return [...cards]
        .sort(() => Math.random() - 0.5)
        .slice(0, 5);
}

export type BoosterTiming = "idle" | "opening" | "revealed" | "resume"

const enabledButtonClass = "button-primary border-action border p-2 rounded cursor-pointer select-none font-bold w-48 transition-[color,background-color,transform] duration-200 ease-in-out active:scale-95"
const disabledButtonClass = "text-muted bg-accent-surface/40 border border-accent-surface p-2 rounded cursor-not-allowed select-none font-bold w-48 opacity-50"

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

    function showResume() {
        setButtonState(false);
        setBoosterState("resume")
    }

    function boosterClass() {

        if (boosterState === "idle")
            return boosterWait
        else if (boosterState === "opening")
            return boosterAnimated
    }

    function renderHomePage() {

        if (boosterState === "revealed") {
            return (
                <div className="relative scale-70 md:scale-100">
                    <BoosterOpening cardsPack={boosterCards} resetFunction={showResume} key={incrementPacks} />
                </div>
            )
        } else if (boosterState === "resume") {
            return (
                <div className="w-full flex justify-center ">
                    <CardsResult cards={boosterCards} resetFunction={showNewPack}/>
                </div>
            )
        } else {
            return (
                <motion.div 
                    initial={{opacity: 0, y: 20}}
                    animate={{opacity: 1, y: 0}}
                    transition={{ease: "easeOut", duration: 0.5}}
                >
                    <img src={boosterImg} className={boosterClass()} />
                </motion.div>
            )
        }
    }

    return (
        <div className={`home-page relative flex min-h-dvh flex-col items-center gap-6 overflow-visible px-4 pt-[calc(env(safe-area-inset-top)+2rem)] pb-[calc(env(safe-area-inset-bottom)+5.5rem)] md:p-8 ${boosterState === "resume" ? "home-results justify-center" : "justify-center overscroll-none"}`}>

            <div className="booster-stage relative z-10 flex w-full items-center justify-center">
                {renderHomePage()}
            </div>

            <div className="relative z-10 flex flex-col items-center gap-3 text-center">

                <button disabled={buttonState} onClick={boosterState === "resume" ? showNewPack : handleBoosterState} className={buttonState ? disabledButtonClass : enabledButtonClass} >{boosterState === "resume" ? "Open another booster" : "Open a booster"}</button>
            </div>
        </div>
    )
}
