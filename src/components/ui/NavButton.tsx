import { NavLink } from "react-router";

interface NavProps {
    linkTo: string;
    imgSrc: string;
    pageName: string;
}


export default function NavButton(props: NavProps) {

    function getNavLinkClass({isActive}: {isActive: boolean}) {

        const basics = "flex items-center text-xl p-3 rounded-xl flex gap-2"
        return isActive
            ? "text-violet-500 dark:text-[#C4B5FD] dark:bg-neutral-700/50" + basics
            : "text-gray-600 dark:text-[#C4B5FD] text-xl hover:bg-neutral-700/20 hover:sticky" + basics
    }

    return (
        <NavLink to={props.linkTo} className={getNavLinkClass}><img className="w-6 h-6" src={props.imgSrc} />{props.pageName}</NavLink>
    )
}