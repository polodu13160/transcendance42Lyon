import type { ReactNode, MouseEvent } from "react";
import { RxCross2 } from "react-icons/rx";

interface ModalProps {
    onClose: () => void;
    children: ReactNode;
}

export default function Modal(props: ModalProps) {

    function handleOverlayClick(event: MouseEvent<HTMLDivElement>): void {
        if (event.target === event.currentTarget) {
            props.onClose();
        }
    }

    return (
        <div
            onClick={handleOverlayClick}
            className="fixed inset-0 z-50 flex h-dvh items-center justify-center bg-black/50 p-4"
        >

            <div
                role="dialog"
                aria-modal="true"
                className="relative max-h-full max-w-full overflow-y-auto rounded border-2 border-[#3F3F46] bg-[#2D2D32] px-5 py-8 text-[#F5F5F5]"
            >

                <button
                    type="button"
                    onClick={props.onClose}
                    className="absolute top-4 right-4 flex h-8 w-8 cursor-pointer items-center justify-center rounded-full border hover:bg-black/30 active:bg-black/50"
                >
                    <RxCross2 />
                </button>

                {props.children}

            </div>

        </div>
    );
}