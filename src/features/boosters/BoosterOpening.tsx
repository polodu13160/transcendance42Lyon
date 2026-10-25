import GameCard, { type GameCardProps } from "../cards/GameCard";
import { motion, type PanInfo } from "motion/react"
import { useState } from "react"
import { AnimatePresence } from "motion/react";

interface openingProps {

    cardsPack: GameCardProps[]
    resetFunction: () => void;
}


export default function BoosterOpening(props: openingProps) {

    const [visibleIndex, setVisibleIndex] = useState(4);

    function dragEnd(event: Event, info: PanInfo): void {
        if (info.offset.x > 100 || info.offset.x < -100) {
            setVisibleIndex(prevIndex => prevIndex - 1);
        }
        if (visibleIndex === 0) {
            props.resetFunction();
        }
    }

    function dragEvent(event: Event, info: PanInfo) : void {

    }

    return (    
        <AnimatePresence>
            {props.cardsPack.map((card, index) => {
                if (index <= visibleIndex) {
                    return (
                        <motion.div
                            className={index === 0 ? "" : "absolute top-0"}
                            key={index}
                            drag={index === visibleIndex ? "x" : false }
                            dragMomentum={false} 
                            dragConstraints={{
                                top: -50,
                                left: -50,
                                right: 50,
                                bottom: 50,}
                            }
                            onDragEnd={(event, info) => dragEnd(event, info)}
                            onDrag={(event, info) => dragEvent(event, info)}
                            exit={{opacity: 0, x: 100
                                
                            }}
                        >
                            <GameCard
                                name={card.name}
                                resume={card.resume}
                                rating={card.rating}
                                image={card.image}
                                rarity={card.rarity}
                                isShiny={card.isShiny}
                                isGame={card.isGame}
                            />
                        </motion.div>
                )}
            })}
        </AnimatePresence>

    )

}