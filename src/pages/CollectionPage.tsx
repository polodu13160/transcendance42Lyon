import GameCard from "../features/cards/GameCard"

export default function CollectionPage() {
    return (
        <div className="flex flex-col justify-center items-center w-auto h-dvh gap-14 bg-neutral-100 dark:bg-[#18181B]">
            <GameCard name="GTA V" resume="Un RPG en monde ouvert dans un univers dark fantasy riche et immersif." rating={9.8} image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTdbwG1Ea1fmYnXN44vKHOMbS2Yo8duuDe-cqaihJaS3hXKWJ4PsC7zUo&s=10"/>
        </div>
    )
}