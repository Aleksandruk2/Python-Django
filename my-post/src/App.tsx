import './App.css'
import { Routes, Route } from "react-router-dom";
import HomePage from "./pages/homePage";
import AddCityPage from "./pages/addCityPage";
import MainLayout from "./MainLayout";

function App() {

    return (
        <>
            <Routes>
                <Route path="/"  element={<MainLayout/>}>
                    <Route index element={<HomePage />} />
                    <Route path="add-city" element={<AddCityPage />} />
                    {/*<Route path="edit-city/:id" element={<EditCity />} />*/}
                </Route>
            </Routes>
        </>
    );
}

export default App


