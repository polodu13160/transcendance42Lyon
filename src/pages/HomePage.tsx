// import GameCard from "../features/cards/GameCard"
// import testData from "../../test_data/cardsData.json"
import logo_dark from "../assets/logo/logo_dark.svg"
export default function HomePage() {



    return (
        <div className="flex flex-col justify-center items-center w-auto h-dvh gap-6 bg-neutral-100 dark:bg-[#18181B]">
            <img src={logo_dark} className="md:block w-full h-auto pb-10 pt-5 scale-90"/>
            <h1 className="text-xl font-bold text-[#A78BFA]" >Bienvenue sur GatchaGames</h1>
            <p className="text-[#F5F5F5]">GatchaGames est une plateforme en ligne de jeu et collection de carte sur l'univers du jeu-vidéo</p>
            <button className="text-[#F5F5F5] bg-[#A78BFA] hover:bg-[#A78BFA]/80 active:bg-[#352B48] border-sky-800 border p-2 rounded cursor-pointer select-none font-bold w-48 transition-all duration-200 ease-in-out active:scale-95">Ouvrir un booster</button>
        </div>
    )
}  