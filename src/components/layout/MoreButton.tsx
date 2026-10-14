import { NavLink, useLocation } from "react-router";
import { useState } from "react";

import profilImg from "../../assets/icons/user-round.svg"

interface MoreButtonProps {

    imgSrc: string;
    pageName: string;
}

// en gros on recup la page actuelle avec useLocation
// menuState garde si le menu est ouvert et sur quelle page on l'a ouvert
// dropDown verifie si le menu est ouvert ET si on est tjr sur la meme page
// qd on clique sur More ca inverse l'etat du menu
// si on change de page les url correspondent plus donc le menu se ferme tout seul


export default function MoreButton(props: MoreButtonProps) {

    const location = useLocation();

    const [menuState, setMenuState] = useState({
        isOpen: false,
        pathname: location.pathname,
    });

    const dropDown =
        menuState.isOpen && menuState.pathname === location.pathname;

    function changeDropState(): void {
        setMenuState(prev => ({
            isOpen: !dropDown,
            pathname: location.pathname,
        }));
    }

    function getNavLinkClass({isActive}: {isActive : boolean}) {

        const basics = "flex flex-row justify-start items-center w-full min-w-0 gap-1 transition-colors duration-200 ease-in-out";

        return isActive
            ? basics + " text-[#7C3AED] md:dark:text-[#C4B5FD] dark:text-white bg-[#F3EEFF] dark:bg-[#352B48] border-[#A78BFA]"
            : basics + " text-[#71717A] dark:text-[#A1A1AA] hover:text-[#7C3AED] dark:hover:text-[#C4B5FD] hover:bg-[#F3EEFF] dark:hover:bg-[#352B48]/50 border-transparent";
    }

    function getMoreClass(): string {

        const basics = "flex md:flex-row flex-col justify-center md:justify-start items-center text-center md:text-left w-full min-w-0 gap-1 md:gap-2 p-1 scale-90 md:scale-100 md:p-3 text-[12px] md:text-xl rounded-xl border transition-colors duration-200 ease-in-out";

        return dropDown
            ? basics + " text-[#7C3AED] md:dark:text-[#C4B5FD] dark:text-white bg-[#F3EEFF] dark:bg-[#352B48] border-[#A78BFA]"
            : basics + " text-[#71717A] dark:text-[#A1A1AA] hover:text-[#7C3AED] dark:hover:text-[#C4B5FD] hover:bg-[#F3EEFF] dark:hover:bg-[#352B48]/50 border-transparent";
    }

    return (

        <div className="relative w-full">
            <button onClick={changeDropState} className={getMoreClass()}>
                <img
                    className="w-6 h-6 shrink-0"
                    src={props.imgSrc}
                    alt=""
                />
                <span className="min-w-0 block md:hidden">{props.pageName}</span>
            </button>
            {
                    dropDown 
                    ?   <div className="items-start p-2 text-[#A78BFA] text-[14px] dark:bg-[#2D2D32] border-4 border-[#3F3F46] gap-2 rounded-xl w-[40vw] flex flex-col absolute bottom-full right-0">
                            <NavLink to="/profil" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={profilImg}
                                    alt=""
                                />
                                <span>Profil</span>
                            </NavLink>
                            <NavLink to="/" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={profilImg}
                                    alt=""
                                />
                                <span>Profil</span>
                            </NavLink>
                            <NavLink to="/" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={profilImg}
                                    alt=""
                                />
                                <span>Profil</span>
                            </NavLink>
                            <NavLink to="/" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={profilImg}
                                    alt=""
                                />
                                <span>Profil</span>
                            </NavLink>
                            <NavLink to="/" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={profilImg}
                                    alt=""
                                />
                                <span>Profil</span>
                            </NavLink>
                        </div> 
                    : null
            }
        </div>
    );
}