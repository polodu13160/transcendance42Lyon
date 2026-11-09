// const buttonClass = "border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500"
import { FaArrowDownShortWide } from "react-icons/fa6";


export default function MarketFilters() {
    return(
        <div>
            <div className="w-full">
                <label>

                </label>
                <input
                    className="text-violet-100 font-medium  w-full border-2 bg-zinc-800 border-zinc-500 rounded-xl placeholder:text-zinc-500 p-4 focus:border-violet-300 focus:outline-none focus:ring-none focus:border-0.5"
                    type="search" 
                    name="search"
                    id="market-search"
                    placeholder="Search for cards in the market..."
                />
            </div>
            <div className="w-full mt-6 gap-2 flex flex-row flex-wrap">
                <div className="relative">
                    <select className="border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500 appearance-none pr-8" >
                        <option>All Rarities</option>
                        <option>Common</option>
                        <option>Uncommon</option>
                        <option>Rare</option>
                        <option>Epic</option>
                        <option>Legendary</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500" />
                </div>
                <div className="relative">
                    <select className="border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500 appearance-none pr-8" >
                        <option>All types</option>
                        <option>Game</option>
                        <option>DLC</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500" />
                </div>
                <div className="relative">
                    <select className="border-2 bg-zinc-800 border-zinc-500 px-3 py-2 rounded-lg text-zinc-500 appearance-none pr-8" >
                        <option>Newest First</option>
                        <option>Latest First</option>
                        <option>Price: Low to High</option>
                        <option>Price: High to Low</option>
                        <option>Name: A-Z</option>
                        <option>Name: Z-A</option>
                    </select>
                    <FaArrowDownShortWide className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-zinc-500" />
                </div>
            </div>
        </div>
    )
}
