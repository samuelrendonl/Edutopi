import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./App.jsx";
import "./Styles/global.css";
import { getParent, API_URL } from "./api";

// El token se revoca al cerrar o recargar la pestaña; no queda una sesión abierta.
window.addEventListener("pagehide", () => {
  const parent = getParent();
  if (parent?.token && navigator.sendBeacon) {
    navigator.sendBeacon(`${API_URL}/auth/logout`, new Blob([JSON.stringify({ token: parent.token })], { type: "application/json" }));
  }
  localStorage.removeItem("edutopia_parent");
});

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
