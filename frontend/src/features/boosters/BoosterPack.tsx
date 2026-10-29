import boosterImg from "../../assets/Booster.svg"

export default function BoosterPack() {
    return (
        <div className="w-75 aspect-2/3">
            <img
                src={boosterImg}
                className="block h-full w-full"
                alt="Booster"
            />
        </div>
    )
}