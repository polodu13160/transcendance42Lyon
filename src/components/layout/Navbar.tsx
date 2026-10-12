import { NavLink } from "react-router";

export default function NavBar() {
    return (
        <nav>
            <NavLink to="/" className="text-red-500 font-bold text-Xl" >Accueil</NavLink>
            <NavLink to="/collection" className={({isActive}) => isActive ? "active" : ""} >Collection</NavLink>
            <NavLink to="/market">Market</NavLink>
            <NavLink to="/browse-all">Browse all cards</NavLink>
            <NavLink to="/profil">Profil</NavLink>
        </nav>
    )
}