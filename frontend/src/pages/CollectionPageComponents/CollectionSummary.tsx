export default function CollectionSummary() {
    return (
        <div>
            <header className="mt-4">
                <h1 className="text-4xl text-foreground font-bold">My collection</h1>
                <p className="text-foreground text-base mt-2">Your games album. Each card tells an adventure.</p>
            </header>

            <div className="w-full rounded-2xl border border-border bg-panel p-4 md:p-6 mt-4">
                <p className="text-xl text-foreground font-bold">Statistics</p>
                <h2 className="text-3xl text-foreground mt-3">100 / 14809 cards discovered.</h2>

                <div className="mt-4 h-2 overflow-hidden rounded-full bg-accent-surface">
                    <div className="h-full rounded-full bg-accent" style={{ width: `${(100 / 14809) * 100}%`}}></div>
                </div>

                <p className="text-xs italic text-muted mt-4">X% of cards discovered | XXXXX cards left to complete the collection.</p>
            </div>

            <div className="grid grid-cols-3 gap-2 md:gap-4 w-full">
                <div className="w-full rounded-2xl border border-border bg-panel p-4 md:p-6 mt-2 md:mt-6">
                    <h2 className="text-foreground text-4xl font-bold">128</h2>
                    <p className="text-muted text-base">Unique cards</p>
                </div>
                <div className="w-full rounded-2xl border border-border bg-panel p-4 md:p-6 mt-2 md:mt-6">
                    <h2 className="text-foreground text-4xl font-bold">24</h2>
                    <p className="text-muted text-base">Duplicates</p>
                </div>
                <div className="w-full rounded-2xl border border-border bg-panel p-4 md:p-6 mt-2 md:mt-6">
                    <h2 className="text-foreground text-4xl font-bold">3</h2>
                    <p className="text-muted text-base">Shiny</p>
                </div>
            </div>
        </div>
    )
}