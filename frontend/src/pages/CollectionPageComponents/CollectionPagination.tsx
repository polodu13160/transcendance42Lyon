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

    if (totalPages > 5 && actualPage <=4) {
        pageButtons.push(1, 2, 3, 4);
        pageButtons.push("...");
        pageButtons.push(totalPages);
    }

    if (totalPages > 5 && actualPage > 4) {
        pageButtons.push(1);
        pageButtons.push("...");
        pageButtons.push(actualPage, actualPage + 1, actualPage + 2, actualPage + 3);
        pageButtons.push("...");
        pageButtons.push(totalPages);
    }

    return (
        <div className="flex flex-row justify-center items-align gap-1">
            {
                pageButtons.map((page: number | string) => {

                    if (page === "...") {
                        return (
                            <button className="text-[#f5f5f5] h-5 w-5 flex justify-center items-center p-5">{page}</button>
                        )
                    }
                    return (
                        <button className="text-[#f5f5f5] h-5 w-5 hover:border-zinc-900  hover:bg-zinc-700 hover:rounded-lg flex justify-center items-center p-5">{page}</button>
                    )
                })
            }
            {/* <h2>{actualPage}</h2> */}
            
        </div>
    )

}