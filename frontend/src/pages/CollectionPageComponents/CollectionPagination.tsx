import React from "react"

interface paginationProps {

    actualPage: number;
    totalPages: number;
    onPageChange: (page: number) => void;

}


export default function CollectionPagination({actualPage, totalPages, onPageChange}: paginationProps ){
    
    const pageButtons: (number | string)[] = [];

    if (totalPages <= 5) {
        pageButtons.push(1, 2, 3, 4, 5);
    }

    return (
        <div className="flex flex-row justify-center items-align gap-1">
            {
                pageButtons.map((page: number | string) => {
                    return (
                        <button className="text-[#f5f5f5] h-5 w-5 hover:border-zinc-900  hover:bg-zinc-700 hover:rounded-lg flex justify-center items-center p-5">{page}</button>
                    )
                })
            }
            {/* <h2>{actualPage}</h2> */}
            
        </div>
    )

}