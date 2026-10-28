import React from "react"
import { motion } from "motion/react"


interface RevealProps {

    front: React.ReactNode;
    back: React.ReactNode;
    swapFunction: () => void;

}

export default function RevealCard({front, back, swapFunction} : RevealProps) {

    const [flip, setFlip] = React.useState(false)

    function flipCard() {
        if (flip === false) {
            setFlip((prevFlip) => !prevFlip)
            swapFunction();
        }
    }
    
    return (
        <div className="flex flex-row relative w-75 aspect-2/3 perspective-normal" onClick={flipCard}>
            <motion.div 
                className="transform-3d w-75 aspect-2/3"
                animate={{rotateY : flip ? 180 : 0}}
                transition={{type: "tween"}}
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