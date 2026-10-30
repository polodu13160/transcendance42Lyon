import { FiChevronDown } from "react-icons/fi";
import { FaArrowDownShortWide } from "react-icons/fa6";


const buttonClass = "border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500"

export default function CollectionFilters() {
    return(
        <div>
            <div className="w-full">
                <label> </label>
                <input 
                    className="text-violet-100 font-medium  w-full border-2 bg-zinc-800 border-zinc-500 rounded-xl placeholder:text-zinc-500 p-4 focus:border-violet-300 focus:outline-none focus:ring-none focus:border-0.5"
                    type="search" 
                    name="search"
                    id="collection-search"
                    placeholder="Search for cards in my collection..."
                />
                <div></div>
            </div>
            <div className="w-full mt-6 gap-2 flex flex-row">
                <button className="border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500">View All</button>
                <button className={buttonClass}>Shiny</button>
                <button className={buttonClass}>Duplicates</button>
                <div className="relative">
                    <select className="border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500 appearance-none pr-8" >
                        <option>Most recent</option>
                        <option>A - Z</option>
                        <option>Z - A</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500" />
                </div>
            </div>
        </div>
    )
}