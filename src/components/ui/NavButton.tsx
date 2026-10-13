import { NavLink } from "react-router";

interface NavProps {
    linkTo: string;
    imgSrc: string;
    pageName: string;
}


export default function NavButton(props: NavProps) {

    function getNavLinkClass({isActive}: {isActive: boolean}) {

        const basics = " text-xl hover:dark:bg-neutral-700/20 p-3 rounded-xl flex gap-2"
        return isActive
            ? "text-violet-500 border-b-2 border-transparent" + basics
            : "text-gray-600 dark:text-neutral-400 text-xl hover:sticky" + basics
    }

    return (
        <NavLink to={props.linkTo} className={getNavLinkClass}><img className="w-6 h-6" src={props.imgSrc} />{props.pageName}</NavLink>
    )
}