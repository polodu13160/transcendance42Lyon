// import GameCard from "../features/cards/GameCard"
// import testData from "../../test_data/cardsData.json"

export default function HomePage() {



    return (
        <div className="flex flex-col justify-center items-center h-screen gap-14 bg-neutral-100 dark:bg-neutral-800">
            <h1 className="text-2xl font-bold text-violet-500" >Bienvenue sur GatchaGames</h1>
            <p>GatchaGames est une plateforme en ligne de jeu et collection de carte sur l'univers du jeu-vidéo</p>
            <button className="text-white bg-sky-400 hover:bg-sky-500 active:bg-sky-600 border-sky-800 border p-2 rounded font-bold w-48 transition-all duration-300 ease-in-out active:scale-95">Ouvrir un booster</button>

        </div>
    )
}  