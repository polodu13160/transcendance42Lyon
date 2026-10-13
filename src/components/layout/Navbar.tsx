import ThemeToggle from "../ui/ThemeToggle";
import NavButton from "../ui/NavButton";


//img
import packImg from "../../assets/icons/pack.svg"
import collectionImg from "../../assets/icons/collection_night.svg"
import bookImg from "../../assets/icons/book-open.svg"
import storeImg from "../../assets/icons/store.svg"
import profilImg from "../../assets/icons/user-round.svg"
    

export default function NavBar() {

    return (
        <div className="flex-col items-center p-4 sticky border-r bg-neutral-100 dark:bg-neutral-800">
            <h1 className="text-violet-500 text-4xl font-extrabold mb-10">GatchaGames</h1>
            <nav className="flex flex-col gap-8">

                <NavButton linkTo="/" imgSrc={packImg} pageName="Home"/>
                <NavButton linkTo="/collection" imgSrc={collectionImg} pageName="Collection" />
                <NavButton linkTo="/market" imgSrc={storeImg} pageName="Market" />
                <NavButton linkTo="/browse-all" imgSrc={bookImg} pageName="Browse all cards" />
                <NavButton linkTo="/profil" imgSrc={profilImg} pageName="Profil" />
            </nav>
            <ThemeToggle />
        </div>
    )
}