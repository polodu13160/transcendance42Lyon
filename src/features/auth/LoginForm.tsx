import { FcGoogle } from "react-icons/fc";
import { FaApple } from "react-icons/fa6";
import { FaGithub } from "react-icons/fa";



export default function LoginForm() {


    const oAuthClasses = "border rounded py-2 px-4 cursor-pointer hover:bg-[#C4B5FD]/10 active:bg-[#C4B5FD]/30"

    return (



        <div className="flex flex-col items-center justify-center"> 
            <h1 className="text-[#A78BFA] font-medium text-xl mt-10 mb-5">Login to your account</h1>


            <div className="flex flex-row gap-8 justify-center items-center mt-5">
                <button className={oAuthClasses} ><FcGoogle size={25}></FcGoogle></button>
                <button className={oAuthClasses}><FaApple size={25}></FaApple></button>
                <button className={oAuthClasses}><FaGithub size={25}></FaGithub></button>
            </div>

            <div className="inline-flex items-center justify-center w-full">
                 <hr className="w-32 h-px my-8 bg-gray-500  border-0"/>
                <span className="px-3 font-medium text-heading">or</span>
                 <hr className="w-32 h-px my-8 bg-gray-500  border-0"/>
            </div>

            <form>

            </form>
        </div>
    )
}