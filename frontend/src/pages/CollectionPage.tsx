import CollectionSummary from "./CollectionPageComponents/CollectionSummary"

export default function CollectionPage() {
    return (
        <main className="mx-auto flex w-full max-w-6xl flex-col gap-6 p-4 md:p-8">
            <CollectionSummary />
        </main>
    )
}