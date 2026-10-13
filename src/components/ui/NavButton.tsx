import { NavLink } from "react-router";

interface NavProps {
    linkTo: string;
    imgSrc: string;
    pageName: string;
}

export default function NavButton(props: NavProps) {

    function getNavLinkClass({ isActive }: { isActive: boolean }) {

        const basics = "flex items-center w-full min-w-0 gap-2 p-3 text-xl rounded-xl border transition-colors duration-200 ease-in-out";

        return isActive
            ? basics + " text-[#7C3AED] dark:text-[#C4B5FD] bg-[#F3EEFF] dark:bg-[#352B48] border-[#A78BFA]"
            : basics + " text-[#71717A] dark:text-[#A1A1AA] hover:text-[#7C3AED] dark:hover:text-[#C4B5FD] hover:bg-[#F3EEFF] dark:hover:bg-[#352B48]/50 border-transparent";
    }

    return (
        <NavLink to={props.linkTo} className={getNavLinkClass}>
            <img
                className="w-6 h-6 shrink-0"
                src={props.imgSrc}
                alt=""
            />
            <span className="min-w-0">{props.pageName}</span>
        </NavLink>
    );
}