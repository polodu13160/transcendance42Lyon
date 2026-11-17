import { NavLink, useLocation } from "react-router";
import { useState } from "react";

import profilImg from "../../assets/icons/user-round.svg"
import bookImg from "../../assets/icons/book-open.svg"
import settingsImg from "../../assets/icons/settings.svg"
import playImg from "../../assets/icons/swords.svg"

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
        setMenuState(({
            isOpen: !dropDown,
            pathname: location.pathname,
        }));
    }

    function getNavLinkClass({isActive}: {isActive : boolean}) {

        const basics = "flex flex-row justify-start items-center w-full h-10 min-w-0 gap-1 transition-colors duration-200 ease-in-out";

        return isActive
            ? basics + " text-action bg-accent-surface border-accent"
            : basics + " text-muted hover:text-accent hover:bg-accent-surface/50 border-transparent";
    }

    function getMoreClass(): string {

        const basics = "flex md:flex-row flex-col justify-center md:justify-start items-center text-center md:text-left w-full min-w-0 gap-1 md:gap-2 p-1 scale-90 md:scale-100 md:p-3 text-[12px] md:text-xl rounded-xl border transition-colors duration-200 ease-in-out";

        return dropDown
            ? basics + " text-action bg-accent-surface border-accent"
            : basics + " text-muted hover:text-accent hover:bg-accent-surface/50 border-transparent";
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
                    ?   <div className="items-start p-2 text-accent text-[14px] bg-surface-raised border-4 border-border gap-2 rounded-xl w-[40vw] flex flex-col absolute bottom-full right-0">
                            <NavLink to="/play" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={playImg}
                                    alt=""
                                />
                                <span>Play</span>
                            </NavLink>
                            <NavLink to="/browse-all" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={bookImg}
                                    alt=""
                                />
                                <span>Browse All</span>
                            </NavLink>
                            <NavLink to="/profil" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={profilImg}
                                    alt=""
                                />
                                <span>Profil</span>
                            </NavLink>
                            <NavLink to="/settings" className={getNavLinkClass}>
                                <img
                                    className="w-6 h-6 shrink-0"
                                    src={settingsImg}
                                    alt=""
                                />
                                <span>Settings</span>
                            </NavLink>

                        </div> 
                    : null
            }
        </div>
    );
}