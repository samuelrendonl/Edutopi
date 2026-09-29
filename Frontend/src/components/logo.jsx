import logo from "../assets/Edutopia.svg";
import "../Styles/logo.css";

function Logo({ variant = "default", className = "" }) {
  return (
    <img
      src={logo}
      alt="Edutopia"
      className={`logo logo-${variant} ${className}`}
    />
  );
}

export default Logo;
