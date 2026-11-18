import { FiArrowLeft } from "react-icons/fi";
import { FiArrowRight } from "react-icons/fi";

interface PaginationProps {

    actualPage: number;
    totalPages: number;
    onPageChange: (page: number) => void;

}

export default function Pagination({actualPage, totalPages, onPageChange}: PaginationProps ){

    return (
        <nav className="flex flex-row justify-center items-center gap-3">
            <button className="hover:bg-surface-raised p-3 rounded-lg disabled:opacity-30 disabled:cursor-not-allowed"
                disabled={actualPage <= 1}
                onClick={() => onPageChange(actualPage - 1 )}
            >
                <FiArrowLeft className="text-foreground text-2xl " />
            </button>

            <p className="text-foreground text-2xl p-2 ">
                Page {actualPage}/{totalPages}
            </p>

            <button className="hover:bg-surface-raised p-3 rounded-lg disabled:opacity-30 disabled:cursor-not-allowed"
                disabled={actualPage >= totalPages}
                onClick={() => onPageChange(actualPage + 1)}
            >
                <FiArrowRight className="text-foreground text-2xl  " />
            </button>

        </nav>
    )

}
