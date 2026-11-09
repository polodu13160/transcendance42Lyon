import MarketSummary from "./MarketPageComponents/MarketSummary"

export default function MarketPage() {
    return (
        <main className="mx-auto flex w-full max-w-6xl flex-col gap-6 p-4 pb-[calc(env(safe-area-inset-bottom)+6rem)] md:p-8">
            <MarketSummary />
        </main>
    )
}
