// import GameCard from "../features/cards/GameCard"
// import testData from "../../test_data/cardsData.json"

export default function HomePage() {



    return (
        <div className="flex flex-col justify-center items-center w-auto h-screen gap-14 bg-neutral-100 dark:bg-[#18181B]">
            <h1 className="text-7xl font-bold text-[#A78BFA]" >Bienvenue sur GatchaGames</h1>
            <p className="text-[#F5F5F5]">GatchaGames est une plateforme en ligne de jeu et collection de carte sur l'univers du jeu-vidéo</p>
            <button className="text-[#F5F5F5] bg-[#A78BFA] hover:bg-[#A78BFA]/80 active:bg-[#352B48] border-sky-800 border p-2 rounded cursor-pointer select-none font-bold w-48 transition-all duration-200 ease-in-out active:scale-95">Ouvrir un booster</button>
        </div>
    )
}  