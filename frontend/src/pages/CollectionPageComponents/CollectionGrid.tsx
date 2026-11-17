import CollectionItem from "./CollectionItem";
import type { CollectionEntry} from "@/types/card"


interface gridProps {
    cardPage: CollectionEntry[]
}

export default function CollectionGrid(props: gridProps) {
    return (
        <div className="grid w-full grid-cols-2 gap-x-3 gap-y-5 md:grid-cols-3 md:gap-4 xl:grid-cols-4">
            {props.cardPage.map((entry) => (
                <CollectionItem key={entry.card.id} cardInfo={entry} />
            ))}
        </div>
    )
}
