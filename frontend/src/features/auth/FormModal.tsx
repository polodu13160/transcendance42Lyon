import React from "react"
import { FcGoogle } from "react-icons/fc";

export default function FormModal() {

    const [showModal, setShowModal] = React.useState(true);

    return (
        <>

        {showModal && (
            <div onClick={() => setShowModal(false)} className="fixed bg-black/50 min-h-screen w-screen z-10 flex justify-center items-center top-0 left-0">

                <div className="bg-surface-raised rounded border-2 text-foreground border-border px-5 py-8">
                    <div>
                        <h1>Welcome Back</h1>  
                        <p>papapapappafslhfhskflsahlfhlashfhlashflashkkfhlkhlskhfshksf</p>
                        <div className="flex items-center justify-center gap-5 mt-5">
                            <button className="button-primary px-4 py-2 rounded">Sign-in</button>
                            <button className="bg-surface hover:bg-accent-soft px-4 py-2 rounded scale-140"><FcGoogle /></button>
                            <button className="bg-surface-raised hover:bg-border px-4 py-2 rounded">Cancel</button>
                        </div>
                    </div>
                </div>

            </div>
        )}
        </>
    )
}