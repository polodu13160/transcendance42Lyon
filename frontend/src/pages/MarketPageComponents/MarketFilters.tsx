// const buttonClass = "border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted"
import { FaArrowDownShortWide } from "react-icons/fa6";

export default function MarketFilters() {
    return(
        <div>
            <div className="w-full">
                <label>

                </label>
                <input
                    className="text-foreground font-medium  w-full border-2 bg-panel border-input-border rounded-xl placeholder:text-muted p-4 focus:border-accent focus:outline-none focus:ring-0"
                    type="search" 
                    name="search"
                    id="market-search"
                    placeholder="Search for cards in the market..."
                />
            </div>
            <div className="w-full mt-6 gap-2 flex flex-row flex-wrap">
                <div className="relative">
                    <select className="border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted appearance-none pr-8" >
                        <option>All Rarities</option>
                        <option>Common</option>
                        <option>Uncommon</option>
                        <option>Rare</option>
                        <option>Epic</option>
                        <option>Legendary</option>
                        <option>Shiny</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-muted" />
                </div>
                <div className="relative">
                    <select className="border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted appearance-none pr-8" >
                        <option>All types</option>
                        <option>Game</option>
                        <option>DLC</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-muted" />
                </div>
                <div className="relative">
                    <select className="border-2 bg-panel border-input-border px-3 py-2 rounded-lg text-muted appearance-none pr-8" >
                        <option>Newest First</option>
                        <option>Latest First</option>
                        <option>Price: Low to High</option>
                        <option>Price: High to Low</option>
                        <option>Name: A-Z</option>
                        <option>Name: Z-A</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-muted" />
                </div>
            </div>
        </div>
    )
}
