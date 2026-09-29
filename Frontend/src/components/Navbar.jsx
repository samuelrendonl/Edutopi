import Logo from "./logo";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getParent } from "../api";
import "./../Styles/navbar.css";
import Icon from "./Icon";

const THEME_KEY = "edutopia-theme";

function applyTheme(theme) {
  const root = document.documentElement;
  root.dataset.theme = theme;
  root.style.colorScheme = theme;
}

function Navbar() {
  const [parent, setParent] = useState(() => getParent());
  const [theme, setTheme] = useState(() =>
    localStorage.getItem(THEME_KEY) === "dark" ? "dark" : "light",
  );
  useEffect(() => {
    applyTheme(theme);
    localStorage.setItem(THEME_KEY, theme);
  }, [theme]);
  useEffect(() => {
    const refreshSession = () => setParent(getParent());
    window.addEventListener("edutopia-auth-change", refreshSession);
    window.addEventListener("storage", refreshSession);
    return () => {
      window.removeEventListener("edutopia-auth-change", refreshSession);
      window.removeEventListener("storage", refreshSession);
    };
  }, []);
  return (
    <nav className="navbar">
      <Logo variant="navbar" />

      <div className="navbar-actions">
        {parent ? (
          <Link to="/Dashboard" className="nav-login">
            Mi familia
          </Link>
        ) : (
          <Link to="/login" className="nav-login">
            Iniciar sesión
          </Link>
        )}

        <button
          type="button"
          className="theme-toggle"
          aria-label={`Tema actual: ${theme === "dark" ? "oscuro" : "claro"}. Cambiar tema`}
          title={`Tema: ${theme === "dark" ? "oscuro" : "claro"}`}
          onClick={() =>
            setTheme((current) => (current === "dark" ? "light" : "dark"))
          }
        >
          <Icon name={theme === "dark" ? "sun" : "cloud"} size={18} />
          <span>{theme === "dark" ? "Oscuro" : "Claro"}</span>
        </button>
      </div>
    </nav>
  );
}

export default Navbar;
