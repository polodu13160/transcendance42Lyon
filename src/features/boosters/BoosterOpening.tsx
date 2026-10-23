import GameCard from "../cards/GameCard";
import { motion } from "motion/react"


export default function BoosterOpening() {

    return (
        <motion.div drag="x" dragMomentum={false}     dragConstraints={{
    top: -50,
    left: -50,
    right: 50,
    bottom: 50,
  }}>
            <GameCard key={1} name="Stardew Valley" resume="Transforme une ferme abandonnée en un petit paradis : cultures, pêche, exploration et rencontres au village."
                rating={9.2} image="https://wallpapers.com/images/featured/stardew-valley-ltuynqpjb7c95ffq.jpg"
                rarity="common" isShiny={true} isGame={true}
            />
        </motion.div>

    )

}