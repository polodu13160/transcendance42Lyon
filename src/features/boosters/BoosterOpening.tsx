import GameCard, { type GameCardProps } from "../cards/GameCard";
import { motion, useMotionValue, type PanInfo } from "motion/react"
import { useState } from "react"
import { AnimatePresence } from "motion/react";
import RevealCard from "../cards/RevealCard";
import CardBack from "../cards/CardBack";

interface openingProps {

    cardsPack: GameCardProps[]
    resetFunction: () => void;
}


export default function BoosterOpening(props: openingProps) {

    const [visibleIndex, setVisibleIndex] = useState(4);
    const [dragOn, setDragOn] = useState(false);
    const [swapDirection, setSwapDirection] = useState(true);




    function dragEnd(event: Event, info: PanInfo): void {
        if (info.offset.x < 0) {
            setSwapDirection(true);
        } else {
            setSwapDirection(false);
        }
        
        if (info.offset.x > 100 || info.offset.x < -100) {

            setVisibleIndex(prevIndex => prevIndex - 1);
            setDragOn(false)


            if (visibleIndex === 0) {
                props.resetFunction();
            }
        }
    }

    function changeDragActive() {
        setDragOn(!dragOn);
    }

    function dragIsActive(index: number): false | "x" {
        if (index === visibleIndex && dragOn) {
            return "x"
        }
        return false;
    }

    const variants = {
        exit: 
            function exit(direction: boolean) {
                return (direction ? {opacity: 0, x: -100, rotate:"-20deg"} : {opacity:0, x: 100, rotate:"20deg"})
            }
    }

    const motionValue = useMotionValue(0);



    return (    
        <AnimatePresence custom={swapDirection}>
            {props.cardsPack.map((card, index) => {
                if (index <= visibleIndex) {
                    return (
                        <motion.div
                            className={index === 0 ? "" : "absolute top-0"}
                            key={index}
                            drag={dragIsActive(index)}
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
                            style={{x: motionValue}}
                        >
                            <RevealCard
                                front={<GameCard
                                    name={card.name}
                                    resume={card.resume}
                                    rating={card.rating}
                                    image={card.image}
                                    rarity={card.rarity}
                                    isShiny={card.isShiny}
                                    isGame={card.isGame}
                                    />}
                                back={<CardBack />}
                                swapFunction={changeDragActive}
                            />
                        </motion.div>
                )}
            })}
        </AnimatePresence>

    )

}