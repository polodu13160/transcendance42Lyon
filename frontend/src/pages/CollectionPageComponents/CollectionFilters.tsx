import { FaArrowDownShortWide } from "react-icons/fa6";

const buttonClass = "border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted"

export default function CollectionFilters() {
    return(
        <div>
            <div className="w-full">

                <input 
                    className="text-foreground font-medium  w-full border-2 bg-panel border-input-border rounded-xl placeholder:text-muted p-4 focus:border-accent focus:outline-none focus:ring-0"
                    type="search" 
                    name="search"
                    id="collection-search"
                    placeholder="Search for cards in my collection..."
                />

            </div>
            <div className="w-full mt-6 gap-2 flex flex-row flex-wrap">
                <button className="border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted">View All</button>
                <button className={buttonClass}>Shiny</button>
                <button className={buttonClass}>Duplicates</button>
                <div className="relative">
                    <select className="border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted appearance-none pr-8" >
                        <option>Most recent</option>
                        <option>A - Z</option>
                        <option>Z - A</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-muted" />
                </div>
            </div>
        </div>
    )
}