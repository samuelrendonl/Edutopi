import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/home";
import Login from "./pages/login";
import Register from "./pages/Register";
import Aprende from "./pages/Aprende";
import Dashboard from "./pages/Dashboard";
import RegisterChild from "./pages/RegisterChild";
import Subject from "./pages/Subject";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/login" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route path="/aprende" element={<Aprende />} />
        <Route path="/materia/:name" element={<Subject />} />

        <Route path="/dashboard/*" element={<Dashboard />} />

        {/* Alias con mayúscula para conservar la URL que usas en tu proyecto. */}
        <Route path="/Dashboard/*" element={<Dashboard />} />

        <Route path="/register-child" element={<RegisterChild />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
