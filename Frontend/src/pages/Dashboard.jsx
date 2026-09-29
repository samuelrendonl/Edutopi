import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import "../Styles/dashboard.css";
import { api, getParent, logout } from "../api";
import Icon from "../components/Icon";

export default function Dashboard() {
  const navigate = useNavigate();
  const [parent] = useState(() => getParent());
  const [children, setChildren] = useState([]);
  const [error, setError] = useState("");
  useEffect(() => {
    if (!parent) {
      navigate("/login");
      return;
    }
    api("/children")
      .then(async (data) => {
        const withProgress = await Promise.all(
          data.children.map(async (child) => {
            try {
              return {
                ...child,
                learning: await api(`/learning/children/${child.id}/progress`),
              };
            } catch {
              return child;
            }
          }),
        );
        setChildren(withProgress);
      })
      .catch((err) => {
        if (err.status === 401) navigate("/login");
        else setError(err.message);
      });
  }, [navigate, parent]);
  function exit() {
    logout();
    navigate("/");
  }
  const allPoints = children.reduce(
    (sum, child) => sum + (child.learning?.points || 0),
    0,
  );
  return (
    <div className="dashboard-page">
      <Navbar />
      <main className="dashboard-container">
        <header className="dashboard-header">
          <div>
            <span className="dashboard-label">PANEL DE FAMILIA</span>
            <h1>
              ¡Hola, {parent?.name?.split(" ")[0] || "familia"}!{" "}
              <Icon name="hand" size={34} className="title-icon" />
            </h1>
            <p>
              Administra los perfiles y acompaña el aprendizaje de tus niños.
            </p>
          </div>
          <div className="dashboard-header-actions">
            <Link to="/aprende" className="dashboard-learn-button">
              <Icon name="game" size={19} /> Ver actividades
            </Link>
            <button className="logout-button" onClick={exit}>
              Salir
            </button>
          </div>
        </header>
        {error && <div className="form-error">{error}</div>}
        <section className="dashboard-section">
          <div className="section-heading">
            <div>
              <h2>Mis hijos</h2>
              <p>Cada perfil tiene actividades adaptadas a su grado.</p>
            </div>
            <Link to="/register-child" className="outline-button">
              <span aria-hidden="true">+</span> Agregar niño/niña
            </Link>
          </div>
          {children.length ? (
            <div className="children-list">
              {children.map((child) => {
                const childProgress = child.learning?.progress || 0;
                return (
                  <article className="child-card" key={child.id}>
                    <div className="child-avatar">
                      <Icon name="star" size={29} />
                    </div>
                    <div className="child-info">
                      <span className="child-label">ESTUDIANTE</span>
                      <h3>{child.name}</h3>
                      <p>
                        {child.grade}.º grado · {child.age} años ·{" "}
                        {child.learning?.points || 0} puntos
                      </p>
                    </div>
                    <div className="child-progress">
                      <div className="progress-header">
                        <span>Progreso</span>
                        <strong>{childProgress}%</strong>
                      </div>
                      <div className="progress-bar">
                        <div
                          className="progress-value"
                          style={{ width: `${childProgress}%` }}
                        />
                      </div>
                    </div>
                    <Link
                      to={`/aprende?child=${child.id}`}
                      className="primary-action"
                    >
                      Aprender ahora
                    </Link>
                  </article>
                );
              })}
            </div>
          ) : (
            <div className="empty-state">
              <Icon name="rainbow" size={50} />
              <h3>Aún no hay perfiles</h3>
              <p>Agrega a tu primer niñ@ para empezar la aventura.</p>
              <Link to="/register-child" className="primary-action">
                Crear primer perfil
              </Link>
            </div>
          )}
        </section>
        <section className="stats-grid">
          <article className="stat-card">
            <span>Materias</span>
            <strong>2</strong>
            <p>Matemáticas y Lengua</p>
          </article>
          <article className="stat-card">
            <span>Actividades</span>
            <strong>15</strong>
            <p>11 aprendizajes y 4 juegos</p>
          </article>
          <article className="stat-card">
            <span>Niños</span>
            <strong>{children.length}</strong>
            <p>Perfiles activos</p>
          </article>
          <article className="stat-card">
            <span>Puntos acumulados</span>
            <strong>{allPoints}</strong>
            <p>Mejor puntaje por actividad</p>
          </article>
        </section>
      </main>
    </div>
  );
}
