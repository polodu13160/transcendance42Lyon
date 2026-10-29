import { FcGoogle } from "react-icons/fc";
import { FaApple } from "react-icons/fa6";
import { FaGithub } from "react-icons/fa";



export default function LoginForm() {


    const oAuthClasses = "flex-row gap-1 justify-center items-center flex border rounded py-2 px-4 cursor-pointer hover:bg-[#C4B5FD]/10 active:bg-[#C4B5FD]/30 text-[14px] border-[#C4B5FD]"

    return (



        <div className="flex flex-col items-center justify-center"> 
            <h1 className="text-[#A78BFA] font-medium text-xl mt-10 mb-5">Log In with</h1>


            <div className="flex flex-row justify-center items-center mt-5 gap-2">
                <button className={oAuthClasses} ><FcGoogle size={17}></FcGoogle>Google</button>
                <button className={oAuthClasses}><FaApple size={17}></FaApple>Apple</button>
                <button className={oAuthClasses}><FaGithub size={17}></FaGithub>GitHub</button>
            </div>

            <div className="inline-flex items-center justify-center w-full">
                 <hr className="w-32 h-px my-8 bg-gray-500  border-0"/>
                <span className="px-3 font-medium text-heading">or</span>
                 <hr className="w-32 h-px my-8 bg-gray-500  border-0"/>
            </div>

            <form action="#" className="flex flex-col justify-center items-center gap-3">
                <div className="border border-[#C4B5FD] px-2 py-1">
                    <input type="mail" placeholder="Email address" required  />
                </div>
                <div className="border border-[#C4B5FD] px-2 py-1">
                    <input type="password" placeholder="Password" required  />
                </div>
                <a href="#" >Forgot your password ?</a>

                <button className="border border-[#C4B5FD] hover:bg-[#C4B5FD]/10 active:bg-[#C4B5FD]/30 px-2 py-1 cursor-pointer" >Login</button>

                <a className="text-xs text-[#A78BFA]" href="#" >Don't have an account yet ? Sign-up here</a>
            </form>
        </div>
    )
}