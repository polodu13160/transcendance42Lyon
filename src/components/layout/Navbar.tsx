import ThemeToggle from "../ui/ThemeToggle";
import NavButton from "../ui/NavButton";


//img
import logo_dark from "../../assets/logo/logo_dark.svg"
import packImg from "../../assets/icons/pack_dark.svg"
import collectionImg from "../../assets/icons/collection_night.svg"
import bookImg from "../../assets/icons/book-open.svg"
import storeImg from "../../assets/icons/store.svg"
import profilImg from "../../assets/icons/user-round.svg"
    


export default function NavBar() {

    return (
        <div className="flex flex-col items-center p-4 sticky border-r h-screen border-[#413b41] bg-[#F8F9FC] dark:bg-[#232326] w-60 shrink-0">
            {/* <h1 className="text-violet-500 text-4xl font-extrabold pb-10">GatchaGames</h1> */}
            <img src={logo_dark} className="w-full h-auto pb-10 pt-5"/>
            <nav className="flex flex-col gap-8 mb-20">

                <NavButton linkTo="/" imgSrc={packImg} pageName="Open Pack"/>
                <NavButton linkTo="/collection" imgSrc={collectionImg} pageName="My Collection" />
                <NavButton linkTo="/browse-all" imgSrc={bookImg} pageName="Browse Cards" />
                <NavButton linkTo="/market" imgSrc={storeImg} pageName="Market" />
                <NavButton linkTo="/profil" imgSrc={profilImg} pageName="My Profil" />
            </nav>
            <div className="mt-auto scale">
                <ThemeToggle />
            </div>
        </div>
    )
}