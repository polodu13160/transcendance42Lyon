import HomePage from "../pages/HomePage"
import CollectionPage from "../pages/CollectionPage"
import Browse from "../pages/BrowsePage"
import MarketPage from "../pages/MarketPage"
import ProfilPage from "../pages/ProfilePage"

import NavBar from "../components/layout/Navbar"
import { BrowserRouter, Routes, Route } from "react-router"

export default function App () {
    return(
        <BrowserRouter>
            <NavBar />
            <main>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/collection" element={<CollectionPage />} />
                    <Route path="/market" element={<MarketPage />} />
                    <Route path="/browse-all" element={<Browse />} />
                    <Route path="/profil" element={<ProfilPage />} />
                </Routes>
            </main>
        </BrowserRouter>
    )
}