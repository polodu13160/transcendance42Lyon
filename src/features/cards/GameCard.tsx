import { FaStar } from "react-icons/fa";
import { FaRegLightbulb } from "react-icons/fa";


type GameCardProps = {
    name: string,
    rating: number,
    resume: string,
    image: string
}

export default function GameCard({ name, rating, image , resume}: GameCardProps) {
    return (
        <div className="flex flex-col w-75 aspect-2/3 overflow-hidden rounded-2xl border-6 border-[#C3CBD8] bg-[#2D2D32]">

            <div className="flex-1 min-h-0 overflow-hidden m-0.5 rounded-lg border border-[#3F3F46]">
                <img
                    src={image}
                    alt={name}
                    className="h-full w-full object-cover"
                />
            </div>

            <div className="flex-1 min-h-0 flex flex-col">
                <h2 className="text-2xl text-white font-bold ml-4 mt-2" >{name}</h2>
                <div className="flex flex-row justify-left items-center ml-4">
                    <FaStar className="text-[#FFC637]"/>
                    <span className="ml-1 font-bold text-white text-xl">{rating}</span>
                    <span className="mx-4 h-4 w-px bg-gray-500"/>
                    <span className="font-light text-gray-400">363 248 reviews</span>
                </div>
                <div className="mt-2">
                    <p className="mx-4 font-normal text-sm text-[#B7C0CD]">{resume}</p>
                </div>

                <div className="bg-[#232326] mb-1.5 mt-2 mx-1.5 rounded-lg flex-1  flex flex-row">
                    <div className="flex ml-2 scale-125 text-[#B7C0CD] justify-center items-center">
                        <FaRegLightbulb className=""/>
                    </div>
                    <div className="flex flex-col ml-3 justify-center">
                        <span className="text-[#B7C0CD] font-bold">Fun Fact</span>
                        <span className="text-white font-light text-xs">Le jeu contient plus de 200 heures de contenu.</span>
                    </div>
                </div>
            </div>

        </div>
    )
}