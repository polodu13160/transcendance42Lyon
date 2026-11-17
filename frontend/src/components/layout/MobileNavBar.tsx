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
        <div className="fixed inset-x-0 bottom-0 z-50 flex shrink-0 flex-row items-center border-t-2 border-t-border bg-surface p-2 pb-[calc(env(safe-area-inset-bottom)+0.5rem)]">
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
