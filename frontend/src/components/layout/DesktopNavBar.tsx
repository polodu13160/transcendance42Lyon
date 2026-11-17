import NavButton from "../ui/NavButton";

// Images
import logo_dark from "../../assets/logo/logo_dark.svg";
import packImg from "../../assets/icons/pack_dark.svg";
import collectionImg from "../../assets/icons/collection_night.svg";
import storeImg from "../../assets/icons/store.svg";
import profilImg from "../../assets/icons/user-round.svg";
import arrowImg from "../../assets/icons/arrow-left-right.svg";
import settingsImg from "../../assets/icons/settings.svg"
import playImg from "../../assets/icons/swords.svg"

interface DesktopNavBarProps {
    onOpenLogin: () => void;
    onOpenSignup: () => void;
}

export default function DesktopNavBar(props: DesktopNavBarProps) {

    return (
        <div className="flex flex-col items-center p-4 sticky top-0 w-60 h-dvh bg-surface shrink-0 z-9">

            <img
                src={logo_dark}
                className="w-full h-auto pb-10 pt-5 scale-90"
                alt="GatchaGames"
            />

            <nav className="flex flex-col w-full gap-2 p-2">

                <NavButton linkTo="/" imgSrc={packImg} pageName="Open Pack" />
                <NavButton linkTo="/collection" imgSrc={collectionImg} pageName="Collection" />
                <NavButton linkTo="/market" imgSrc={storeImg} pageName="Market" />
                <NavButton linkTo="/trade" imgSrc={arrowImg} pageName="Trade" />
                <NavButton linkTo="/play" imgSrc={playImg} pageName="Play" />

                <hr className="border-t border-accent-soft my-2 scale-90" />

                <NavButton linkTo="/profil" imgSrc={profilImg} pageName="My Profil" />
                <NavButton linkTo="/settings" imgSrc={settingsImg} pageName="Settings" />
            </nav>

            <div className="flex flex-col w-full gap-4 mt-auto">

                <button
                    type="button"
                    onClick={props.onOpenLogin}
                    className="flex w-full items-center justify-center rounded-xl button-primary p-3 text-sm font-medium transition-colors"
                >
                    Login
                </button>

                <button
                    type="button"
                    onClick={props.onOpenSignup}
                    className="flex w-full items-center justify-center rounded-xl border border-border p-3 text-sm text-muted transition-colors hover:border-accent hover:text-accent"
                >
                    Sign-Up
                </button>

            </div>

        </div>
    );
}