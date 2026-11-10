import ThemeToggle from "../ui/ThemeToggle";
import NavButton from "../ui/NavButton";

// Images
import logo_dark from "../../assets/logo/logo_dark.svg";
import packImg from "../../assets/icons/pack_dark.svg";
import collectionImg from "../../assets/icons/collection_night.svg";
import storeImg from "../../assets/icons/store.svg";
import profilImg from "../../assets/icons/user-round.svg";
import arrowImg from "../../assets/icons/arrow-left-right.svg";
// import bookImg from "../../assets/icons/book-open.svg"
import settingsImg from "../../assets/icons/settings.svg"
import playImg from "../../assets/icons/swords.svg"

interface DesktopNavBarProps {
    onOpenLogin: () => void;
    onOpenSignup: () => void;
}

export default function DesktopNavBar(props: DesktopNavBarProps) {

    return (
        <div className="flex flex-col items-center p-4 sticky top-0 w-60 h-dvh bg-[#E4E4E7] dark:bg-[#232326] shrink-0 z-9">

            <img
                src={logo_dark}
                className="w-full h-auto pb-10 pt-5 scale-90"
                alt="GatchaGames"
            />

            <nav className="flex flex-col w-full gap-2 p-2">

                <p></p>

                <NavButton linkTo="/" imgSrc={packImg} pageName="Open Pack" />
                <NavButton linkTo="/collection" imgSrc={collectionImg} pageName="Collection" />
                <NavButton linkTo="/market" imgSrc={storeImg} pageName="Market" />
                <NavButton linkTo="/trade" imgSrc={arrowImg} pageName="Trade" />
                {/* <NavButton linkTo="/browse-all" imgSrc={bookImg} pageName="Browse Cards" /> */}
                <NavButton linkTo="/play" imgSrc={playImg} pageName="Play" />

                <hr className="border-t border-[#C4B5FD] my-2 scale-90" />

                <NavButton linkTo="/profil" imgSrc={profilImg} pageName="My Profil" />
                <NavButton linkTo="/settings" imgSrc={settingsImg} pageName="Settings" />
            </nav>

            <div className="flex flex-col w-full gap-4 mt-auto">

                <button
                    type="button"
                    onClick={props.onOpenLogin}
                    className="text-[#71717A] dark:bg-[#C4B5FD] dark:text-white hover:text-[#7C3AED]
                    dark:hover:text-[#C4B5FD] hover:bg-[#F3EEFF] dark:hover:bg-[#352B48]/50 border cursor-pointer
                    flex md:flex-row flex-col justify-center md:justify-center items-center text-center md:text-left w-full min-w-0 gap-1
                    md:gap-2 p-1 scale-0 md:scale-100 md:p-3 text-[12px] md:text-sm rounded-xl transition-colors duration-200 ease-in-ou"
                >
                    Login
                </button>

                <button
                    type="button"
                    onClick={props.onOpenSignup}
                    className="text-[#71717A] dark:text-[#A1A1AA] hover:text-[#7C3AED]
                    dark:hover:text-[#C4B5FD] hover:bg-[#F3EEFF] dark:hover:bg-[#352B48]/50 border cursor-pointer
                    flex md:flex-row flex-col justify-center md:justify-center items-center text-center md:text-left w-full min-w-0 gap-1
                    md:gap-2 p-1 scale-90 md:scale-100 md:p-3 text-[12px] md:text-sm rounded-xl transition-colors duration-200 ease-in-out"
                >
                    Sign-Up
                </button>

                {/* <div className="flex justify-center py-4">
                    <div className="scale-150">
                        <ThemeToggle />
                    </div>
                </div> */}

            </div>

        </div>
    );
}