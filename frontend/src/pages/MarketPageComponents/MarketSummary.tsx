export default function MarketSummary() {
    return (
        <div>
            <header className="mt-4">
                    <h1 className="text-4xl text-foreground font-bold">Market Place</h1>
                    <p className="text-foreground text-base mt-2">Complete your album by finding the card you’re missing.</p>
            </header>
            <div className="w-full rounded-2xl border border-border bg-panel p-4 md:p-6 mt-4">
                <p className="text-xl text-foreground font-bold">Your GatchaCoins</p>
                <h2 className="text-3xl text-foreground mt-3">12376 GC</h2>
            </div>
        </div>
    )
}