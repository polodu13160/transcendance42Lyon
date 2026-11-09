import MarketSummary from "./MarketPageComponents/MarketSummary"
import MarketFilters from "./MarketPageComponents/MarketFilters"
import MarketGrid from "./MarketPageComponents/MarketGrid"
import Pagination from "@/components/ui/Pagination"
import { useState } from "react"


export default function MarketPage() {
    const [actualPage, setActualPage] = useState(1);

    return (
        <main className="mx-auto flex w-full max-w-6xl flex-col gap-6 p-4 pb-[calc(env(safe-area-inset-bottom)+6rem)] md:p-8">
            <MarketSummary />
            <MarketFilters />
            <MarketGrid />
            <Pagination actualPage={actualPage} totalPages={1} onPageChange={setActualPage} />
        </main>
    )
}
