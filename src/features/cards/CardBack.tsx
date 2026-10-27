import logoImg from "../../assets/logo/logo_dark_back.svg"

export default function CardBack() {
    return (
        <div className="relative w-75 overflow-hidden rounded-2xl p-1.5 bg-[#F3EEFF] select-none">
            <div className="aspect-2/3 rounded-xl bg-[#6D28D9] flex justify-center select-non ">
                <img src={logoImg} className="scale-80" draggable={false}/>
            </div>
        </div>
    );
}