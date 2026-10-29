import React from "react"
import { FcGoogle } from "react-icons/fc";


export default function FormModal() {

    const [showModal, setShowModal] = React.useState(true);

    return (
        <>
        
        
        {showModal && (
            <div onClick={() => setShowModal(false)} className="fixed bg-black/50 min-h-screen w-screen z-10 flex justify-center items-center top-0 left">
                
                <div className="bg-[#2D2D32] rounded border-2 text-[#F5F5F5] border-[#3F3F46] px-5 py-8">
                    <div>
                        <h1>Welcome Back</h1>  
                        <p>papapapappafslhfhskflsahlfhlashfhlashflashkkfhlkhlskhfshksf</p>
                        <div className="flex items-center justify-center gap-5 mt-5">
                            <button className="bg-[#A78BFA] hover:bg-blue-400 px-4 py-2 rounded">Sign-in</button>
                            <button className="bg-gray-900 hover:bg-blue-400 px-4 py-2 rounded scale-140"><FcGoogle /></button>
                            <button className="bg-gray-500 hover:bg-gray-400 px-4 py-2 rounded">Cancel</button>
                        </div>
                    </div>
                </div>

            </div>
        )}
        </>
    )
}