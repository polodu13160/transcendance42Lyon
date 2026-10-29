import GameCard from "../cards/GameCard";
import type { GameCardProps } from "../../types/card";
import { motion, useMotionValue, useTransform, type PanInfo, type Variants } from "motion/react"
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

    const variants: Variants = {
        initial: { opacity: 0, scale: 0.96, y: 18 },
        visible: {
            opacity: 1,
            scale: 1,
            y: 0,
            transition: { duration: 0.32, ease: "easeOut" },
        },
        exit: function exit(direction: boolean) {
            return {
                opacity: 0,
                x: direction ? -340 : 340,
                scale: 0.96,
                transition: { duration: 0.28, ease: "easeIn" },
            }
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
            initial={isActive ? "initial" : false}
            animate="visible"
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
