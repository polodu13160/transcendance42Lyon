import { NavLink } from "react-router";

export default function NavBar() {

    function getNavLinkClass({isActive}: {isActive: boolean}) {
        return isActive
            ? "text-violet-500 font-bold"
            : "text-gray-500 hover:text-violet-500"
    }

    return (
        <nav className="flex gap-6">
            <NavLink to="/" className={getNavLinkClass} >Accueil</NavLink>
            <NavLink to="/collection" className={getNavLinkClass} >Collection</NavLink>
            <NavLink to="/market" className={getNavLinkClass}>Market</NavLink>
            <NavLink to="/browse-all" className={getNavLinkClass}>Browse all cards</NavLink>
            <NavLink to="/profil" className={getNavLinkClass}>Profil</NavLink>
        </nav>
    )
}