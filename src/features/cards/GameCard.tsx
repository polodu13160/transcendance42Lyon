type GameCardProps = {
    name: string,
    rating: number
    image: string
}

export default function GameCard({name, rating, image}: GameCardProps) {

    return (
        <>
            <h2>{name}</h2>
            <p>{rating}</p>
            <img src={image}/>
        </>
    )
}