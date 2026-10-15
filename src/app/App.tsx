import HomePage from "../pages/HomePage"
import CollectionPage from "../pages/CollectionPage"
import Browse from "../pages/BrowsePage"
import MarketPage from "../pages/MarketPage"
import TradePage from "../pages/TradePage"
import SettingsPage from "../pages/SettingsPage"
import ProfilPage from "../pages/ProfilePage"
import PlayPage from "../pages/PlayPage"
import FormModal from "../features/auth/FormModal"

import NavBar from "../components/layout/Navbar"
import { BrowserRouter, Routes, Route } from "react-router"

export default function App () {
    return(
        <BrowserRouter>
            <div className="flex min-h-dvh bg-[#18181B]">
                <NavBar />
                <FormModal />
                <main className="flex-1 min-w-0">
                    <Routes>
                        <Route path="/" element={<HomePage />} />
                        <Route path="/collection" element={<CollectionPage />} />
                        <Route path="/market" element={<MarketPage />} />
                        <Route path="/browse-all" element={<Browse />} />
                        <Route path="/profil" element={<ProfilPage />} />
                        <Route path="/settings" element={<SettingsPage />} />
                        <Route path="/trade" element={<TradePage />} />
                        <Route path="/play" element={<PlayPage />} />
                    </Routes>
                </main>
            </div>
        </BrowserRouter>
    )
}