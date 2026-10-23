import GameCard from "../cards/GameCard";
import { motion, type PanInfo } from "motion/react"


export default function BoosterOpening() {

    function dragEnd(event: Event, info: PanInfo): void {
        console.log(info.offset.x)
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
            <GameCard key={1} name="Stardew Valley" resume="Transforme une ferme abandonnée en un petit paradis : cultures, pêche, exploration et rencontres au village."
                rating={9.2} image="https://wallpapers.com/images/featured/stardew-valley-ltuynqpjb7c95ffq.jpg"
                rarity="common" isShiny={true} isGame={true}
            />
        </motion.div>

    )

}