import { useState } from "react"

interface MoreButtonProps {

    imgSrc: string;
    pageName: string;
}


export default function MoreButton(props: MoreButtonProps) {

    const [dropDown, setDropDown] = useState(false);

    function changeDropState(): void {
        setDropDown(prevDropDown => !prevDropDown);
    }

    function getNavLinkClass(): string {

        const basics = "flex md:flex-row flex-col justify-center md:justify-start items-center text-center md:text-left w-full min-w-0 gap-1 md:gap-2 p-1 scale-90 md:scale-100 md:p-3 text-[12px] md:text-xl rounded-xl border transition-colors duration-200 ease-in-out";

        return dropDown
            ? basics + " text-[#7C3AED] md:dark:text-[#C4B5FD] dark:text-white bg-[#F3EEFF] dark:bg-[#352B48] border-[#A78BFA]"
            : basics + " text-[#71717A] dark:text-[#A1A1AA] hover:text-[#7C3AED] dark:hover:text-[#C4B5FD] hover:bg-[#F3EEFF] dark:hover:bg-[#352B48]/50 border-transparent";
    }

    return (

        <div className="relative w-full">
            <button onClick={changeDropState} className={getNavLinkClass()}>
                <img
                    className="w-6 h-6 shrink-0"
                    src={props.imgSrc}
                    alt=""
                />
                <span className="min-w-0 block md:hidden">{props.pageName}</span>
            </button>
            {
                    dropDown ? <h1>Ouvert</h1> : null
            }
        </div>
    );
}