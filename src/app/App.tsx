import { useState } from "react";
import { BrowserRouter, Routes, Route } from "react-router";

// Pages
import HomePage from "../pages/HomePage";
import CollectionPage from "../pages/CollectionPage";
import Browse from "../pages/BrowsePage";
import MarketPage from "../pages/MarketPage";
import TradePage from "../pages/TradePage";
import SettingsPage from "../pages/SettingsPage";
import ProfilPage from "../pages/ProfilePage";
import PlayPage from "../pages/PlayPage";

// Components
import NavBar from "../components/layout/Navbar";
import Modal from "../components/ui/Modal";

// Auth
import LoginForm from "../features/auth/LoginForm";

// Types
type ModalType = "login" | "signup" | null;

export default function App() {

    const [activeModal, setActiveModal] = useState<ModalType>(null);

    function closeModal(): void {
        setActiveModal(null);
    }

    return (
        <BrowserRouter>
            <div className="flex min-h-dvh bg-[#18181B]">

                <NavBar
                    onOpenLogin={() => setActiveModal("login")}
                    onOpenSignup={() => setActiveModal("signup")}
                />

                {activeModal !== null && (
                    <Modal onClose={closeModal}>

                        {activeModal === "login" && (
                            <LoginForm />
                        )}

                        {activeModal === "signup" && (
                            <h2>Signup à créer</h2>
                        )}

                    </Modal>
                )}

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
    );
}