import { useEffect, useMemo, useState } from "react";
import {
  Link,
  Navigate,
  useNavigate,
  useParams,
  useSearchParams,
} from "react-router-dom";
import Navbar from "../components/Navbar";
import Icon from "../components/Icon";
import { api, getParent } from "../api";
import "../Styles/subject.css";

const subjects = {
  Matemáticas: "calculator",
  "Lengua Castellana": "book",
};

const slug = {
  Matemáticas: "Matematicas",
  "Lengua Castellana": "Lengua_Castellana",
};

export default function Subject() {
  const { name } = useParams();
  const subject = decodeURIComponent(name || "");
  const [params] = useSearchParams();
  const navigate = useNavigate();

  const [children, setChildren] = useState([]);
  const [childId, setChildId] = useState(params.get("child") || "");
  const [catalog, setCatalog] = useState([]);
  const [progress, setProgress] = useState(null);
  const [open, setOpen] = useState(null);
  const [error, setError] = useState("");

  const selected = children.find(
    (child) => String(child.id) === String(childId),
  );

  const grade = Number(selected?.grade || 1);

  useEffect(() => {
    if (!getParent()) {
      navigate("/login", { replace: true });
      return;
    }

    api("/children")
      .then((data) => {
        const childList = data.children || [];
        setChildren(childList);

        const requestedChild = params.get("child");

        const child =
          childList.find(
            (item) => String(item.id) === String(requestedChild),
          ) || childList[0];

        if (child) {
          setChildId(String(child.id));
        }
      })
      .catch((err) => {
        if (err.status === 401) {
          navigate("/login", { replace: true });
        } else {
          setError(err.message);
        }
      });
  }, [navigate, params]);

  useEffect(() => {
    if (!selected) return;

    let cancelled = false;

    Promise.all([
      api(`/learning/activities?grade=${grade}`),
      api(`/learning/children/${selected.id}/progress`),
    ])
      .then(([activityData, progressData]) => {
        if (cancelled) return;

        setCatalog(activityData.activities || []);
        setProgress(progressData);
      })
      .catch((err) => {
        if (!cancelled) {
          setError(err.message);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [selected?.id, grade]);

  const lessons = useMemo(
    () =>
      catalog.filter(
        (item) => item.subject === subject && item.kind === "Aprendizaje",
      ),
    [catalog, subject],
  );

  const games = useMemo(
    () =>
      catalog.filter(
        (item) => item.subject === subject && item.kind === "Juego",
      ),
    [catalog, subject],
  );

  const completed = lessons.filter(
    (item) => progress?.activities?.[item.key],
  ).length;

  if (!getParent()) {
    return <Navigate to="/login" replace />;
  }

  if (!subjects[subject]) {
    return <Navigate to="/aprende" replace />;
  }

  const pdfName = `Guia_${slug[subject]}_${grade}.pdf`;

  return (
    <div className="subject-page">
      <Navbar />

      <main className="subject-container">
        <Link
          className="back-link"
          to={`/aprende${selected ? `?child=${selected.id}` : ""}`}
        >
          ← Volver a materias
        </Link>

        <header className="subject-header">
          <Icon name={subjects[subject]} size={42} />

          <div>
            <span className="eyebrow">RUTA DE APRENDIZAJE</span>

            <h1>{subject}</h1>

            <p>
              Estudia las lecciones, practica las actividades y descarga la guía
              completa correspondiente al grado del estudiante.
            </p>
          </div>
          <div className="guide-download-always">
            <span>
              Guía de {subject} · {grade}.º grado
            </span>

            <a
              className="download-guide"
              href={`/guias/Guia_${
                subject === "Matemáticas" ? "Matematicas" : "Lengua_Castellana"
              }_${grade}.pdf`}
              download
            >
              Descargar guía en PDF
            </a>
          </div>
        </header>

        {error && (
          <p className="form-error" role="alert">
            {error}
          </p>
        )}

        {!children.length && (
          <p>
            Para estudiar, primero agrega un perfil infantil desde{" "}
            <Link to="/Dashboard">Mi familia</Link>.
          </p>
        )}

        {children.length > 0 && (
          <>
            <div className="guide-toolbar">
              <label>
                Estudiante
                <select
                  value={childId}
                  onChange={(event) => {
                    setChildId(event.target.value);
                    setOpen(null);
                  }}
                >
                  {children.map((child) => (
                    <option key={child.id} value={child.id}>
                      {child.name} · {child.grade}.º grado
                    </option>
                  ))}
                </select>
              </label>

              <a className="download-guide" href={`/guias/${pdfName}`} download>
                Descargar guía de {grade}.º en PDF
              </a>
            </div>

            <div className="guide-summary">
              <strong>
                {completed} de {lessons.length}
              </strong>{" "}
              lecciones realizadas · {selected?.name}, {grade}.º grado. Las
              marcas aparecen al terminar las actividades.
            </div>

            <section className="guide-panel">
              <span className="eyebrow">GUÍA DE ESTUDIO</span>

              <h2>Lecciones y actividades</h2>

              <p>
                El contenido corresponde a las actividades reales de Edutopia
                para este grado.
              </p>

              {lessons.length === 0 && (
                <p>No hay lecciones disponibles para esta materia y grado.</p>
              )}

              {lessons.map((item, index) => (
                <article
                  className={`guide-card ${
                    progress?.activities?.[item.key] ? "completed" : ""
                  }`}
                  key={item.key}
                >
                  <div className="guide-card-top">
                    <span className="check">
                      {progress?.activities?.[item.key]
                        ? "✓ Completada"
                        : "○ Pendiente"}
                    </span>

                    <span className="unit-number">LECCIÓN {index + 1}</span>
                  </div>

                  <h3>{item.title}</h3>

                  <p className="guide-objective">{item.description}</p>

                  <button
                    type="button"
                    className="open-guide"
                    onClick={() => setOpen(item)}
                  >
                    Leer guía
                    <Icon name="arrowRight" size={16} />
                  </button>

                  <Link
                    className="open-guide"
                    to={`/aprende?child=${childId}&subject=${encodeURIComponent(
                      subject,
                    )}&activity=${encodeURIComponent(item.key)}`}
                  >
                    Realizar actividad
                  </Link>
                </article>
              ))}
            </section>

            <section className="guide-panel">
              <span className="eyebrow">PRÁCTICA JUGANDO</span>

              <h2>Juegos de {subject}</h2>

              <div className="subject-game-list">
                {games.length === 0 && (
                  <p>No hay juegos disponibles para esta materia.</p>
                )}

                {games.map((game) => (
                  <Link
                    className="guide-card"
                    key={game.key}
                    to={`/aprende?child=${childId}&subject=${encodeURIComponent(
                      subject,
                    )}&activity=${encodeURIComponent(game.key)}`}
                  >
                    <strong>{game.title}</strong>

                    <span>
                      {game.minutes} minutos · {game.questions?.length || 0}{" "}
                      retos
                    </span>
                  </Link>
                ))}
              </div>
            </section>
          </>
        )}
      </main>

      {open && (
        <div
          className="guide-overlay"
          onMouseDown={(event) => {
            if (event.target === event.currentTarget) {
              setOpen(null);
            }
          }}
        >
          <section
            className="guide-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="guide-title"
          >
            <button
              className="modal-close"
              onClick={() => setOpen(null)}
              aria-label="Cerrar guía"
              type="button"
            >
              ×
            </button>

            <span className="eyebrow">
              {subject.toUpperCase()} · {grade}.º GRADO
            </span>

            <h2 id="guide-title">{open.title}</h2>

            <p>{open.description}</p>

            {open.passage && (
              <>
                <h3>Lectura</h3>
                <blockquote>{open.passage}</blockquote>
              </>
            )}

            <h3>Aprende paso a paso</h3>

            {open.lesson?.map((line, index) => (
              <p key={`${open.key}-lesson-${index}`}>{line}</p>
            ))}

            <h3>Comprueba lo aprendido</h3>

            <p>
              La actividad de la plataforma contiene{" "}
              {open.questions?.length || 0} preguntas. Lee cada una, explica tu
              respuesta y comprueba tu avance al terminar.
            </p>

            <Link
              className="activity-next-button"
              to={`/aprende?child=${childId}&subject=${encodeURIComponent(
                subject,
              )}&activity=${encodeURIComponent(open.key)}`}
            >
              Ir a la actividad
            </Link>
          </section>
        </div>
      )}
    </div>
  );
}
