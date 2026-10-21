import type { GameProps } from "../../types/game";

export default function CardDetails(props: GameProps) {
    
    return (
        <div>
            <p>{props.imageUrl}</p>
            <p>{props.name}</p>
            <p>{props.rating}</p>
            <p>{props.reviewCount}</p>
            <p>{props.description}</p>
            <p>{props.funfact}</p>
        </div>
    )

}


