import CollectionFilters from "./CollectionPageComponents/CollectionFilters"
import CollectionGrid from "./CollectionPageComponents/CollectionGrid"
import CollectionSummary from "./CollectionPageComponents/CollectionSummary"

export default function CollectionPage() {
    return (
        <main className="mx-auto flex w-full max-w-6xl flex-col gap-6 p-4 pb-[calc(env(safe-area-inset-bottom)+6rem)] md:p-8">
            <CollectionSummary />
            <CollectionFilters />
            <CollectionGrid />
        </main>
    )
}
