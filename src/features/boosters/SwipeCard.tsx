import GameCard from "../cards/GameCard";
import type { GameCardProps } from "../../types/card";
import { motion, useMotionValue, useTransform, type PanInfo } from "motion/react"
import RevealCard from "../cards/RevealCard";
import CardBack from "../cards/CardBack";

interface SwipeCardProps {

    isActive: boolean
    card: GameCardProps
    index: number
    drag: false | "x"
    dragEnd: (event: Event, info: PanInfo) => void;
    swapFunction: () => void;
}

export default function SwipeCard({card, index, drag, dragEnd, swapFunction, isActive}: SwipeCardProps) {

    const variants = {
        exit: 
            function exit(direction: boolean) {
                return (direction ? {opacity: 0, x: -100} : {opacity:0, x: 100})
            }
    }

    const motionValue = useMotionValue(0);

    const rotate = useTransform(motionValue, [-150, 0, 150], [-20, 0, 20])

    return (
        <motion.div
            className={index === 0 ? "" : "absolute top-0"}
            drag={drag}
            dragMomentum={false} 
            dragConstraints={{
                top: -50,
                left: -50,
                right: 50,
                bottom: 50,}
            }
            onDragEnd={(event, info) => dragEnd(event, info)}
            variants={variants}
            exit="exit"
            style={{x: motionValue, rotate: rotate}}
            dragSnapToOrigin
        >
            <RevealCard
                rarity={card.rarity}
                isActive={isActive}
                front={<GameCard {...card} />}
                back={<CardBack rarity={card.rarity} isActive={false} />}
                swapFunction={swapFunction}
                isShiny={card.isShiny}
            />
        </motion.div>
    )
}
