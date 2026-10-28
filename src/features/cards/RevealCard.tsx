
import React from "react"
import { motion } from "motion/react"
import { cardThemes } from "./cardThemes"
import type { CardRarity } from "@/types/card"

interface RevealProps {
    front: React.ReactNode;
    back: React.ReactNode;
    rarity: CardRarity;
    isActive: boolean;
    isShiny: boolean
    swapFunction?: () => void;
}

export default function RevealCard({
    front,
    back,
    rarity,
    isActive,
    swapFunction,
    isShiny
}: RevealProps) {

    const [flip, setFlip] = React.useState(false)

    const themeShadow = cardThemes[rarity].shadow

    function flipCard() {
        if (flip === false) {
            setFlip(true)
            swapFunction?.()
        }
    }

    return (
        <div
            className="relative w-75 h-111 perspective-normal"
            onClick={flipCard}
        >
            {isActive && (
                <div
                    aria-hidden="true"
                    className={`
                        absolute inset-0 rounded-2xl pointer-events-none
                        halo-pulse
                        ${themeShadow}
                    `}
                    style={{
                        opacity: flip ? 0 : undefined,
                        transition: "opacity 500ms ease-out"
                    }}
                />
            )}

            {isActive && isShiny && (
                <div
                    aria-hidden="true"
                    className={`shiny-halo ${flip ? "shiny-halo-hidden" : ""}`}
                />
            )}

            <motion.div
                className="relative transform-3d w-75 h-111"
                animate={{ rotateY: flip ? 180 : 0 }}
                transition={{ type: "tween" }}
            >
                <div className="absolute backface-hidden rotate-y-180">
                    {front}
                </div>

                <div className="absolute backface-hidden">
                    {back}
                </div>
            </motion.div>
        </div>
    )
}
