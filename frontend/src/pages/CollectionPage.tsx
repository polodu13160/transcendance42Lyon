export default function CollectionPage() {
    return (
        <main className="mx-auto flex w-full max-w-6xl flex-col gap-6 p-4 md:p-8">
            <header>
                <h1 className="text-4xl text-[#F5F5F5] ">My collection</h1>
            </header>

            <div className="w-full rounded-2xl border border-zinc-700 bg-zinc-800 p-4 md:p-6">
                <p className="text-xl text-violet-300">Statistics</p>
                <h2 className="text-3xl text-[#F5F5F5] mt-3">100 / 14809 cards discovered.</h2>

                <div className="mt-4 h-2 overflow-hidden rounded-full bg-zinc-700">
                    <div className="h-full rounded-full bg-violet-400" style={{ width: `${(100 / 14809) * 100}%`}}></div>
                </div>

                <p className="text-xs italic text-zinc-500 mt-4">X% of cards discovered | XXXXX cards left to complete the collection.</p>
            </div>
        </main>
    )
}