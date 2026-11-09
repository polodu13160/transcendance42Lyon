import React from "react"

import { FiArrowLeft } from "react-icons/fi";
import { FiArrowRight } from "react-icons/fi";


interface paginationProps {

    actualPage: number;
    totalPages: number;
    onPageChange: (page: number) => void;

}


export default function CollectionPagination({actualPage, totalPages, onPageChange}: paginationProps ){
    

    return (
        <nav className="flex flex-row justify-center items-align gap-3">
            <button className="hover:bg-zinc-700 p-3 rounded-lg disabled:opacity-30 disabled:cursor-not-allowed"
                disabled={actualPage <= 1}
                onClick={() => onPageChange(actualPage - 1 )}
            >
                <FiArrowLeft className="text-white text-2xl " />
            </button>

            <p className="text-white text-2xl p-2 ">
                Page {actualPage}/{totalPages}
            </p>

            <button className="hover:bg-zinc-700 p-3 rounded-lg disabled:opacity-30 disabled:cursor-not-allowed"
                disabled={actualPage >= totalPages}
                onClick={() => onPageChange(actualPage + 1)}
            >
                <FiArrowRight className="text-white text-2xl  " />
            </button>
            
        </nav>
    )

}