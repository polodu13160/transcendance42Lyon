// import type { GameCardProps } from "@/types/card";
import type { GameCardProps } from "@/types/card";
import GameCard from "./GameCard";
import { motion } from "motion/react"


interface CardsResultProps {
    
    cards: GameCardProps[]
    resetFunction: () => void;

}


export default function CardsResult(props: CardsResultProps) {

    return (
        <motion.div 
            className="flex w-full max-w-[312px] flex-wrap justify-center gap-3 md:max-w-[678px] md:gap-6"
            initial={{opacity: 0, y: 20}}
            animate={{opacity: 1, y: 0}}
            transition={{ease: "easeOut", duration: 0.5}}
        >
            {props.cards.map((card, index) => (
                <div key={index} className="h-[222px] w-[150px] shrink-0 md:h-[311px] md:w-[210px]">
                    <div className="origin-top-left scale-50 md:scale-[0.7]">
                        <GameCard {...card} />
                    </div>
                </div>
            ))}
        </motion.div>
    )

}
