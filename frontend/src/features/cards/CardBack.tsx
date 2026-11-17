import logoImg from "../../assets/logo/logo_dark_back.svg"

import type { CardRarity } from "@/types/card";
import { cardThemes } from "./cardThemes";

interface CardBackProps {
    rarity: CardRarity
    isActive: boolean
}

export default function CardBack(props: CardBackProps) {

    const themeShadow = cardThemes[props.rarity].shadow 

    return (
        <div className="relative w-75 rounded-2xl bg-card-back-border select-none p-1.5">

            <div
                className={`
                    absolute inset-0 rounded-2xl pointer-events-none
                    ${props.isActive ? ` ${themeShadow}` : ""}
                `}
            />

            <div className="relative aspect-2/3 rounded-xl bg-accent-surface flex justify-center">
                <img src={logoImg} draggable={false} className="scale-80 select-none" />
            </div>

        </div>
    );
}