export default function CollectionSummary() {
    return (
        <div>
            <header className="mt-4">
                <h1 className="text-4xl text-[#F5F5F5] font-bold">My collection</h1>
                <p className="text-[#F5F5F5] text-base mt-2">Your game album. Each card tells an adventure.</p>
            </header>

            <div className="w-full rounded-2xl border border-zinc-700 bg-zinc-800 p-4 md:p-6 mt-4">
                <p className="text-xl text-violet-300 font-bold">Statistics</p>
                <h2 className="text-3xl text-[#F5F5F5] mt-3">100 / 14809 cards discovered.</h2>

                <div className="mt-4 h-2 overflow-hidden rounded-full bg-zinc-700">
                    <div className="h-full rounded-full bg-violet-400" style={{ width: `${(100 / 14809) * 100}%`}}></div>
                </div>

                <p className="text-xs italic text-zinc-500 mt-4">X% of cards discovered | XXXXX cards left to complete the collection.</p>
            </div>

            <div className="grid grid-cols-3 gap-2 md:gap-4 sm:grid-cols-3 w-full">
                <div className="w-full rounded-2xl border border-zinc-700 bg-zinc-800 p-4 md:p-6 mt-2 md:mt-4">
                    <h2 className="text-violet-300 text-4xl font-bold">128</h2>
                    <p className="text-zinc-500 text-base">Unique cards</p>
                </div>
                <div className="w-full rounded-2xl border border-zinc-700 bg-zinc-800 p-4 md:p-6 mt-2 md:mt-4">
                    <h2 className="text-violet-300 text-4xl font-bold">24</h2>
                    <p className="text-zinc-500 text-base">Duplicates</p>
                </div>
                <div className="w-full rounded-2xl border border-zinc-700 bg-zinc-800 p-4 md:p-6 mt-2 md:mt-4">
                    <h2 className="text-violet-300 text-4xl font-bold">3</h2>
                    <p className="text-zinc-500 text-base">Shiny</p>
                </div>
            </div>
        </div>
    )
}