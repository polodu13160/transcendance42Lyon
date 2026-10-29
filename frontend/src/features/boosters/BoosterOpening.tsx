import type { GameCardProps } from "../../types/card";
import { type PanInfo } from "motion/react"
import { useState } from "react"
import { AnimatePresence } from "motion/react";
import SwipeCard from "./SwipeCard";

interface openingProps {

    cardsPack: GameCardProps[]
    resetFunction: () => void;
}


export default function BoosterOpening(props: openingProps) {

    const [visibleIndex, setVisibleIndex] = useState(4);
    const [dragOn, setDragOn] = useState(false);
    const [swapDirection, setSwapDirection] = useState(true);
    const [isClosing, setIsClosing] = useState(false);




    function dragEnd(_event: Event, info: PanInfo): void {
        if (info.offset.x < 0) {
            setSwapDirection(true);
        } else {
            setSwapDirection(false);
        }
        
        if (info.offset.x > 100 || info.offset.x < -100) {

            setDragOn(false)

            if (visibleIndex === 0) {
                setIsClosing(true);
            }

            setVisibleIndex(prevIndex => prevIndex - 1);
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

    return (    
        <AnimatePresence
            custom={swapDirection}
            onExitComplete={() => {
                if (isClosing) props.resetFunction();
            }}
        >
            {props.cardsPack.map((card, index) => {
                if (index <= visibleIndex) {
                    return (
                        <SwipeCard
                            key={index}
                            card={card}
                            index={index}
                            drag={dragIsActive(index)}
                            dragEnd={dragEnd}
                            swapFunction={changeDragActive}
                            isActive={index === visibleIndex ? true : false}
                        />
                )}
            })}
        </AnimatePresence>

    )

}
