// import ThemeToggle from "../ui/ThemeToggle";
import NavButton from "../ui/NavButton";
import MoreButton from "./MoreButton";

// Images
// import logo_dark from "../../assets/logo/logo_dark.svg";
import packImg from "../../assets/icons/pack_dark.svg";
import collectionImg from "../../assets/icons/collection_night.svg";
import storeImg from "../../assets/icons/store.svg";
import circleImg from "../../assets/icons/circle_plus.svg"
import arrowImg from "../../assets/icons/arrow-left-right.svg";


export default function MobileNavBar() {
    return (
        <div className="flex flex-row items-center border-t-2 border-t-[#3F3F46] p-2 fixed bottom-0 w-screen bg-[#E4E4E7] dark:bg-[#232326] shrink-0 z-50">
            <nav className="flex w-full gap-2">
                <div className="flex-1 min-w-0">
                    <NavButton linkTo="/collection" imgSrc={collectionImg} pageName="Collection" />
                </div>

                <div className="flex-1 min-w-0">
                    <NavButton linkTo="/trade" imgSrc={arrowImg} pageName="Trade" />
                </div>

                <div className="flex-1 min-w-0">
                    <NavButton linkTo="/" imgSrc={packImg} pageName="Open Pack" />
                </div>  

                <div className="flex-1 min-w-0">
                    <NavButton linkTo="/market" imgSrc={storeImg} pageName="Market" />
                </div>

                <div className="flex-1 min-w-0">
                    <MoreButton imgSrc={circleImg} pageName="More" />
                </div>
            </nav>
        </div>
    )
}