import GameCard from "../features/cards/GameCard"

export default function CollectionPage() {
    return (
        <div className="grid grid-cols-3 justify-items-center gap-14 min-h-dvh p-8 bg-neutral-100 dark:bg-[#18181B]">
            <GameCard name="GTA V" resume="Un RPG en monde ouvert dans un univers dark fantasy riche et immersif. iheuiriehhrihuerhiurhehruihriehuruhreu" 
            rating={9.8} image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/capsule_616x353.jpg?t=1790290043" 
            rarity="common"/>
             <GameCard name="GTA V" resume="Un RPG en monde ouvert dans un univers dark fantasy riche et immersif. iheuiriehhrihuerhiurhehruihriehuruhreu" 
            rating={9.8} image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/capsule_616x353.jpg?t=1790290043" 
            rarity="uncommon"/>
             <GameCard name="GTA V" resume="Un RPG en monde ouvert dans un univers dark fantasy riche et immersif. iheuiriehhrihuerhiurhehruihriehuruhreu" 
            rating={9.8} image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/capsule_616x353.jpg?t=1790290043" 
            rarity="rare"/>
             <GameCard name="GTA V" resume="Un RPG en monde ouvert dans un univers dark fantasy riche et immersif. iheuiriehhrihuerhiurhehruihriehuruhreu" 
            rating={9.8} image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/capsule_616x353.jpg?t=1790290043" 
            rarity="epic"/>
             <GameCard name="GTA V" resume="Un RPG en monde ouvert dans un univers dark fantasy riche et immersif. iheuiriehhrihuerhiurhehruihriehuruhreu" 
            rating={9.8} image="https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1245620/capsule_616x353.jpg?t=1790290043" 
            rarity="legendary"/>
        </div>
    )
}