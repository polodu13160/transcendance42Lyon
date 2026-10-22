import GameCard from "../features/cards/GameCard";
import { useState } from "react";
import { motion } from "motion/react";

const cards = [0, 1, 2, 3, 4];
const rayon = 320;

export default function CollectionPage() {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <div className="min-h-dvh overflow-auto bg-neutral-100 dark:bg-[#18181B]">
            <div className="relative h-[1000px] min-w-[1000px]">
                {cards.map((id, index) => {
                    // Cinq positions espacées régulièrement.
                    // On commence en haut avec -Math.PI / 2.
                    const angle =
                        (index / cards.length) * Math.PI * 2 - Math.PI / 2;

                    const x = Math.cos(angle) * rayon;
                    const y = Math.sin(angle) * rayon;

                    return (
                        <motion.div
                            key={id}
                            className="absolute left-1/2 top-1/2 cursor-pointer"
                            initial={false}
                            onClick={() => setIsOpen(true)}
                            animate={{
                                x: isOpen ? x : 0,
                                y: isOpen ? y : 0,
                            }}
                            transition={{
                                type: "spring",
                                stiffness: 100,
                                damping: 20,
                            }}
                        >
                            {/* Centre la carte sur sa position */}
                            <div className="h-[280px] w-[180px] -translate-x-1/2 -translate-y-1/2">
                                {/* Réduit la carte sans modifier GameCard */}
                                <div className="w-[300px] origin-top-left scale-[0.6]">
                                    <GameCard
                                        name="Stardew Valley"
                                        resume="Transforme une ferme abandonnée en un petit paradis : cultures, pêche, exploration et rencontres au village."
                                        rating={9.2}
                                        image="https://wallpapers.com/images/featured/stardew-valley-ltuynqpjb7c95ffq.jpg"
                                        rarity="common"
                                        isShiny={true}
                                        isGame={false}
                                    />
                                </div>
                            </div>
                        </motion.div>
                    );
                })}
            </div>
        </div>
    );
}



  // <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-6 xl:scale-50 justify-between justify-items-center gap-20 min-h-dvh bg-neutral-100 dark:bg-[#18181B]">
            // <GameCard
            //     name="Stardew Valley"
            //     resume="Transforme une ferme abandonnée en un petit paradis : cultures, pêche, exploration et rencontres au village."
            //     rating={9.2}
            //     image="https://wallpapers.com/images/featured/stardew-valley-ltuynqpjb7c95ffq.jpg"
            //     rarity="common"
            //     isShiny={true}
            //     isGame={false}
            // />
        //     <GameCard
        //         name="Stardew Valley"
        //         resume="Transforme une ferme abandonnée en un petit paradis : cultures, pêche, exploration et rencontres au village."
        //         rating={9.2}
        //         image="https://wallpapers.com/images/featured/stardew-valley-ltuynqpjb7c95ffq.jpg"
        //         rarity="common"
        //         isShiny={false}
        //         isGame={false}
        //     />
        //     <GameCard
        //         name="Hollow Knight"
        //         resume="Explore un royaume souterrain oublié, affronte des créatures redoutables et découvre les secrets de Hallownest."
        //         rating={9.5}
        //         image="https://cdn.gamekult.com/optim/images/news/30/3050819133/tournez-manettes-hollow-knight-26ced2bf__1920_1080__0-52-1600-569.jpg"
        //         rarity="uncommon"
        //         isShiny={true}
        //         isGame={true}

        //     />
        //     <GameCard
        //         name="Hollow Knight"
        //         resume="Explore un royaume souterrain oublié, affronte des créatures redoutables et découvre les secrets de Hallownest."
        //         rating={9.5}
        //         image="https://cdn.gamekult.com/optim/images/news/30/3050819133/tournez-manettes-hollow-knight-26ced2bf__1920_1080__0-52-1600-569.jpg"
        //         rarity="uncommon"
        //         isShiny={false}
        //         isGame={true}

        //     />
        //     <GameCard
        //         name="Cyberpunk 2077"
        //         resume="Deviens mercenaire à Night City, une mégalopole où implants cybernétiques, pouvoir et trahisons façonnent ton destin."
        //         rating={8.8}
        //         image="https://gamegpu.com/images/1_2026/NEWS/Q4/okt/20/image_80yu354qthg78hy58qyuthg_ggpu.webp"
        //         rarity="rare"
        //         isShiny={true}
        //         isGame={false}

        //     />
        //                 <GameCard
        //         name="Cyberpunk 2077"
        //         resume="Deviens mercenaire à Night City, une mégalopole où implants cybernétiques, pouvoir et trahisons façonnent ton destin."
        //         rating={8.8}
        //         image="https://gamegpu.com/images/1_2026/NEWS/Q4/okt/20/image_80yu354qthg78hy58qyuthg_ggpu.webp"
        //         rarity="rare"
        //         isShiny={false}
        //         isGame={false}

        //     />

        //     <GameCard
        //         name="The Witcher 3"
        //         resume="Incarne Geralt de Riv et traque des monstres dans un monde où chaque contrat cache des choix difficiles."
        //         rating={9.7}
        //         image="https://c4.wallpaperflare.com/wallpaper/764/375/783/the-witcher-3-wild-hunt-dragon-sword-geralt-of-rivia-wallpaper-preview.jpg"
        //         rarity="epic"
        //         isShiny={true}
        //         isGame={false}

        //     />
        //                 <GameCard
        //         name="The Witcher 3"
        //         resume="Incarne Geralt de Riv et traque des monstres dans un monde où chaque contrat cache des choix difficiles."
        //         rating={9.7}
        //         image="https://c4.wallpaperflare.com/wallpaper/764/375/783/the-witcher-3-wild-hunt-dragon-sword-geralt-of-rivia-wallpaper-preview.jpg"
        //         rarity="epic"
        //         isShiny={false}
        //         isGame={false}

        //     />

        //     <GameCard
        //         name="Elden Ring"
        //         resume="Parcours l’Entre-terre, défie des demi-dieux déchus et forge ta légende dans un vaste monde de dark fantasy."
        //         rating={9.8}
        //         image="https://cdn-uploads.gameblog.fr/img/news/440610_64c90201c5cfd.jpg"
        //         rarity="legendary"
        //         isShiny={true}
        //         isGame={true}

        //     />
        //     <GameCard
        //         name="Elden Ring"
        //         resume="Parcours l’Entre-terre, défie des demi-dieux déchus et forge ta légende dans un vaste monde de dark fantasy."
        //         rating={9.8}
        //         image="https://cdn-uploads.gameblog.fr/img/news/440610_64c90201c5cfd.jpg"
        //         rarity="legendary"
        //         isShiny={false}
        //         isGame={true}

        //     />
        // </div>