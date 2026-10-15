import ThemeToggle from "../ui/ThemeToggle";
import NavButton from "../ui/NavButton";

// Images
import logo_dark from "../../assets/logo/logo_dark.svg";
import packImg from "../../assets/icons/pack_dark.svg";
import collectionImg from "../../assets/icons/collection_night.svg";
import storeImg from "../../assets/icons/store.svg";
import profilImg from "../../assets/icons/user-round.svg";
import arrowImg from "../../assets/icons/arrow-left-right.svg";

export default function DesktopNavBar() {
    return (
        <div className="flex flex-col items-center p-4 sticky top-0 w-60 h-screen bg-[#E4E4E7] dark:bg-[#232326] shrink-0 z-9">

            <img
                src={logo_dark}
                className="w-full h-auto pb-10 pt-5"
                alt="GatchaGames"
            />

            <nav className="flex flex-col w-full gap-8">
                <NavButton linkTo="/" imgSrc={packImg} pageName="Open Pack" />
                <NavButton linkTo="/collection" imgSrc={collectionImg} pageName="Collection" />
                <NavButton linkTo="/trade" imgSrc={arrowImg} pageName="Trade" />
                <NavButton linkTo="/market" imgSrc={storeImg} pageName="Market" />
                <NavButton linkTo="/profil" imgSrc={profilImg} pageName="My Profil" />
            </nav>

            <div className="mt-auto scale-150">
                <ThemeToggle />
            </div>

        </div>
    );
}