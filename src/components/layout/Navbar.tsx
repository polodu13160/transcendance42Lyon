import { NavLink } from "react-router";
import ThemeToggle from "../ui/ThemeToggle";
import packImg from "../../assets/icons/pack.svg"

export default function NavBar() {

    function getNavLinkClass({isActive}: {isActive: boolean}) {
        return isActive
            ? "text-violet-500 text-xl border-b-2 border-transparent flex gap-2"
            : "text-gray-600 dark:text-neutral-400  text-xl hover:border-b-2 hover:sticky hover:border-violet-500 flex gap-2"
    }

    return (
        <div className="flex justify-between items-center bg-neutral-100 dark:bg-neutral-800 p-4 w-full sticky top-0 z-10">
            <h1 className="text-violet-500 text-4xl font-extrabold">GatchaGames</h1>
            <nav className="flex gap-6">
                <NavLink to="/" className={getNavLinkClass}><img src={packImg} />Home</NavLink>
                <NavLink to="/collection" className={getNavLinkClass} >Collection</NavLink>
                <NavLink to="/market" className={getNavLinkClass}>Market</NavLink>
                <NavLink to="/browse-all" className={getNavLinkClass}>Browse all cards</NavLink>
                <NavLink to="/profil" className={getNavLinkClass}>Profil</NavLink>
            </nav>
            <ThemeToggle />
        </div>
    )
}