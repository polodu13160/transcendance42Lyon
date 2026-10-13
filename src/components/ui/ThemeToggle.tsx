import React from "react"

import sunIcon from "../../assets/icons/sun.svg"
import moonIcon from "../../assets/icons/moon-star.svg"

export default function ThemeToggle() {

    const [toggleButton, setToggleButton] = React.useState(false)

    function toggleAction(): void {
        setToggleButton(prevToggleButton => !prevToggleButton);
    }

    React.useEffect(() => {
        document.documentElement.classList.toggle('dark', toggleButton === true);
    }, [toggleButton])

return (
    <>
        <label className="select-none cursor-pointer">
            <input
                type="checkbox"
                onChange={toggleAction}
                className="sr-only peer"
            />

            <span className="border border-stone-800 h-6 w-12 bg-sky-100 peer-checked:border-stone-300 peer-checked:bg-slate-800 peer-checked:[&>span]:bg-indigo-400 transition-colors duration-300 ease-in-out rounded-full flex items-center p-0.5 peer-checked:[&>span]:translate-x-6">
                <span className="h-5 w-5 rounded-full bg-amber-400 flex transition-transform duration-400 ease-in-out items-center justify-center">
                    <img
                        src={toggleButton ? moonIcon : sunIcon} 
                        className="w-3.5 h-3.5"
                    />
                </span>
            </span>
        </label>

        {/* <h3>Button : {toggleButton ? "nuit" : "jour"}</h3>  */}
    </>
)
}   