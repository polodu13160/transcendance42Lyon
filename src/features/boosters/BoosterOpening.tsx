import GameCard, { type GameCardProps } from "../cards/GameCard";
import { motion, type PanInfo } from "motion/react"
import { useState } from "react"

interface openingProps {

    cardsPack: GameCardProps[]
}


export default function BoosterOpening(props: openingProps) {

    const [visibleIndex, setVisibleIndex] = useState(4);

    function dragEnd(event: Event, info: PanInfo): void {
        if (info.offset.x > 40 || info.offset.x < -40) {
            setVisibleIndex(prevIndex => prevIndex - 1);
        }
    }

    return (    
        <div>
            {props.cardsPack.map((card, index) => (
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
                ))}
        </div>

    )

}