import GameCard, { type GameCardProps } from "../cards/GameCard";
import { motion, type PanInfo } from "motion/react"
import { useState } from "react"

interface openingProps {

    cardsPack: GameCardProps[]
}


export default function BoosterOpening(props: openingProps) {

    const [visibleIndex, setVisibleIndex] = useState(0);

    function dragEnd(event: Event, info: PanInfo): void {

    }

    return (    
        <motion.div drag="x" dragMomentum={false} 
            dragConstraints={{
                top: -50,
                left: -50,
                right: 50,
                bottom: 50,}
            }
            onDragEnd={(event, info) => dragEnd(event, info)}
        >
            {props.cardsPack.map((card, index) => (
                    <motion.div
                        className={index === 0 ? "" : "absolute top-0"}
                        key={index}
                        drag="x" dragMomentum={false} 
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
        </motion.div>

    )

}