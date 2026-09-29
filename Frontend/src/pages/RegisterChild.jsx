import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";
import Navbar from "../components/Navbar";
import "../Styles/child.css";
import { api } from "../api";

function RegisterChild() {
  const navigate = useNavigate();

  const [error, setError] = useState("");
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    try { await api("/children", { method: "POST", body: JSON.stringify({ name: data.get("childName"), age: data.get("childAge"), grade: data.get("childGrade") }) }); navigate("/Dashboard"); }
    catch (err) { setError(err.message); }
  };

  return (
    <div className="child-page">
      <Navbar />

      <main className="child-container">
        <section className="child-form-card">
          <div className="child-form-header">
            <span className="child-form-label">PERFIL DEL ESTUDIANTE</span>

            <h1>Registrar niño</h1>

            <p>
              Completa la información del estudiante para comenzar a
              personalizar su experiencia en Edutopia.
            </p>
          </div>

          {error && <div className="form-error">{error}</div>}
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="childName">Nombre completo</label>

              <input
                type="text"
                id="childName"
                name="childName"
                placeholder="Ej. Juan Pérez"
                required
              />
            </div>

            <div className="form-row">
              <div className="form-group">
                <label htmlFor="childAge">Edad</label>

                <input
                  type="number"
                  id="childAge"
                  name="childAge"
                  placeholder="Ej. 9"
                  min="5"
                  max="12"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="childGrade">Grado</label>

                <select
                  id="childGrade"
                  name="childGrade"
                  defaultValue=""
                  required
                >
                  <option value="" disabled>
                    Seleccionar
                  </option>

                  <option value="1">1.º grado</option>

                  <option value="2">2.º grado</option>

                  <option value="3">3.º grado</option>

                  <option value="4">4.º grado</option>

                  <option value="5">5.º grado</option>
                </select>
              </div>
            </div>

            <div className="child-form-actions">
              <Link to="/Dashboard" className="child-cancel-button">
                Cancelar
              </Link>

              <button type="submit" className="child-submit-button">
                Crear perfil
              </button>
            </div>
          </form>
        </section>
      </main>
    </div>
  );
}

export default RegisterChild;
