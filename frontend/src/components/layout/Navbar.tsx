import DesktopNavBar from "./DesktopNavBar";
import MobileNavBar from "./MobileNavBar";

interface NavBarProps {
    onOpenLogin: () => void;
    onOpenSignup: () => void;
}

export default function NavBar(props: NavBarProps) {

    return (
        <>
            <div className="hidden md:block">
                <DesktopNavBar
                    onOpenLogin={props.onOpenLogin}
                    onOpenSignup={props.onOpenSignup}
                />
            </div>

            <div className="block md:hidden">
                <MobileNavBar />
            </div>
        </>
    );
}