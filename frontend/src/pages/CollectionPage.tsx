import CollectionFilters from "./CollectionPageComponents/CollectionFilters"
import CollectionGrid from "./CollectionPageComponents/CollectionGrid"
import CollectionSummary from "./CollectionPageComponents/CollectionSummary"

import cardsData from "../../test_data/cardsData.json";
import type { CollectionCard, CollectionEntry } from "@/types/card";
import { act, useState } from "react"
import CollectionPagination from "./CollectionPageComponents/CollectionPagination";


export default function CollectionPage() {

    const cards = cardsData as CollectionCard[];

    const testCollection: CollectionEntry[] = cards.slice(0, 12).map((card) => ({
        card,
        quantity: 4,
        isFavorite: true
    }));

    const [actualPage, setActualPage] = useState(1);

    function setPagination(index : number) {
        setActualPage(index);
    }

    return (
        <main className="mx-auto flex w-full max-w-6xl flex-col gap-6 p-4 pb-[calc(env(safe-area-inset-bottom)+6rem)] md:p-8">
            <CollectionSummary />
            <CollectionFilters />
            <CollectionGrid cardPage={testCollection}/>
            <CollectionPagination actualPage={actualPage} totalPages={5} onPageChange={setPagination} />
        </main>
    )
}
