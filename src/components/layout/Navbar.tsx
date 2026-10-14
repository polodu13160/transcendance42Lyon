import DesktopNavBar from "./DesktopNavBar";
import MobileNavBar from "./MobileNavBar";
    


export default function NavBar() {

    return (
        <>
            <div className="md:block hidden">
                <DesktopNavBar />
            </div>
            <div className="md:hidden block">
                <MobileNavBar />
            </div>
        </>
    )
}