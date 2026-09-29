import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { useSearchParams } from "react-router-dom";
import Navbar from "../components/Navbar";
import Icon from "../components/Icon";
import { api, cacheLearningCatalog, getCachedLearningCatalog, getParent } from "../api";
import "../Styles/learning.css";

const subjects = ["Todas", "Matemáticas", "Lengua Castellana", "Sociales", "Biología", "Inglés"];
const availableSubjects = new Set(["Matemáticas", "Lengua Castellana"]);
const subjectModules = [
  { name: "Matemáticas", icon: "calculator", color: "#5b5ce2", description: "Operaciones, problemas y retos." },
  { name: "Lengua Castellana", icon: "book", color: "#f28c28", description: "Lectura, escritura y palabras." },
  { name: "Sociales", icon: "globe", color: "#e66a9b", description: "Un espacio preparado para conocer el mundo." },
  { name: "Biología", icon: "leaf", color: "#21a889", description: "Un espacio preparado para descubrir la vida." },
  { name: "Inglés", icon: "rainbow", color: "#3ba9dd", description: "Un espacio preparado para aprender otro idioma." },
];
const validGrade = value => Number(value) >= 1 && Number(value) <= 5 ? Number(value) : 3;

export default function Aprende() {
  const [params, setParams] = useSearchParams();
  const initialChild = useRef(params.get("child"));
  const initialActivity = useRef(params.get("activity"));
  const [parent] = useState(() => getParent());
  const [children, setChildren] = useState([]);
  const [profilesLoaded, setProfilesLoaded] = useState(() => !getParent());
  const [childId, setChildId] = useState(params.get("child") || "");
  const [grade, setGrade] = useState(() => validGrade(params.get("grade")));
  const initialGrade = useRef(validGrade(params.get("grade")));
  const [catalog, setCatalog] = useState(() => getCachedLearningCatalog(validGrade(params.get("grade"))) || []);
  const [progress, setProgress] = useState(null);
  const [subject, setSubject] = useState(params.get("subject") || "Todas");
  const [active, setActive] = useState(null);
  const [step, setStep] = useState(0);
  const [answers, setAnswers] = useState([]);
  const [result, setResult] = useState(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [gameStats, setGameStats] = useState({ lives: 3, score: 0, streak: 0 });
  const [gameFeedback, setGameFeedback] = useState(null);
  const catalogRequest = useRef(0);

  useEffect(() => {
    if (!parent) {
      window.location.href = "/login";
      return;
    }
    api("/children")
      .then(data => {
        setChildren(data.children);
        setProfilesLoaded(true);
        const selected = initialChild.current;
        const selectedChild = data.children.find(child => String(child.id) === selected);
        if (selectedChild) setGrade(Number(selectedChild.grade));
        else if (selected) {
          setChildId("");
          setParams({ grade: String(initialGrade.current) }, { replace: true });
        }
      })
      .catch(err => { setProfilesLoaded(true); setError(err.message); });
  }, [parent, setParams]);

  useEffect(() => {
    const requestId = ++catalogRequest.current;
    api(`/learning/activities?grade=${grade}`)
      .then(data => {
        if (requestId === catalogRequest.current) setCatalog(data.activities);
        cacheLearningCatalog(data.activities, grade);
      })
      .catch(err => { if (requestId === catalogRequest.current) setError(err.message); });
  }, [grade]);

  useEffect(() => {
    if (!childId || !children.some(child => String(child.id) === childId)) return;
    api(`/learning/children/${childId}/progress`)
      .then(setProgress)
      .catch(err => setError(err.message));
  }, [childId, children]);

  const filtered = useMemo(
    () => catalog.filter(item => (item.grades || [grade]).includes(Number(grade)) && (subject === "Todas" || item.subject === subject)),
    [catalog, subject, grade],
  );
  const chosenChild = children.find(child => String(child.id) === childId);
  useEffect(() => {
    const key = initialActivity.current;
    const item = catalog.find(activity => activity.key === key);
    if (item && chosenChild && Number(chosenChild.grade) === Number(grade)) {
      initialActivity.current = null;
      startActivity(item);
    }
  }, [catalog, childId, grade, children]);
  const fullAccess = Boolean(parent && chosenChild);
  const currentProgress = progress?.child?.id === Number(childId) ? progress : null;

  function chooseGrade(value) {
    const nextGrade = validGrade(value);
    setGrade(nextGrade);
    setActive(null);
    setSubject("Todas");
    const cached = getCachedLearningCatalog(nextGrade);
    if (cached) setCatalog(cached);
    setChildId("");
    setProgress(null);
    setParams({ grade: String(nextGrade) });
  }

  function chooseChild(value) {
    const child = children.find(item => String(item.id) === value);
    setChildId(value);
    setProgress(null);
    if (child) {
      setGrade(Number(child.grade));
      const cached = getCachedLearningCatalog(Number(child.grade));
      if (cached) setCatalog(cached);
      setParams({ child: value, grade: String(child.grade) });
    } else {
      setParams({ grade: String(grade) });
    }
  }

  function startActivity(activity) {
    const run = activity;
    setActive(run);
    setStep(activity.kind === "Aprendizaje" ? -1 : 0);
    setAnswers([]);
    setResult(null);
    setError("");
    setGameStats({ lives: 3, score: 0, streak: 0 });
    setGameFeedback(null);
  }

  const closeActivity = useCallback(() => {
    setActive(null);
    setResult(null);
    setAnswers([]);
  }, []);

  useEffect(() => {
    if (!active) return undefined;
    function onKeyDown(event) {
      if (event.key === "Escape") closeActivity();
    }
    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [active, closeActivity]);

  async function selectAnswer(optionIndex) {
    setAnswers(current => {
      const next = [...current];
      next[step] = optionIndex;
      return next;
    });
    if (active?.kind !== "Juego" || gameFeedback || busy) return;
    try {
      const checked = await api("/games/check", { method: "POST", body: JSON.stringify({ key: active.key, grade, round: step, answer: optionIndex }) });
      setGameFeedback(checked);
      setGameStats(current => checked.correct
        ? { ...current, score: current.score + 10 + current.streak * 2, streak: current.streak + 1 }
        : { ...current, lives: Math.max(0, current.lives - 1), streak: 0 });
    } catch (err) { setError(err.message); }
  }

  async function nextQuestion() {
    if (answers[step] === undefined) return;
    if (step < active.questions.length - 1) {
      setStep(current => current + 1);
      setGameFeedback(null);
      return;
    }
    setBusy(true);
    setError("");
    try {
      const submission = await api(`/learning/children/${childId}/submit`, {
      method: "POST", body: JSON.stringify({ activity_key: active.key, answers }),
    });
      setResult(submission);
      if (fullAccess) {
        const updated = await api(`/learning/children/${childId}/progress`);
        setProgress(updated);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="learn-page">
      <Navbar />
      <main className="learn-container">
        <div className="learn-hero">
          <div>
            <span className="eyebrow">AVENTURAS PARA APRENDER</span>
            <h1>¡Cada reto te hace crecer! <Icon name="rocket" size={34} /></h1>
            <p>Explora las materias, sigue la guía de aprendizaje y registra el progreso del estudiante.</p><div className="selected-grade-pill">Contenido de {grade}.º grado</div>
          </div>
          <div className="learn-mascot"><Icon name="sparkles" size={92} /></div>
        </div>

        <div className="learning-toolbar">
          <label className="child-picker">Perfil del niño
            <select value={childId} onChange={event => chooseChild(event.target.value)}>
              <option value="">Selecciona un estudiante</option>
              {children.map(child => <option key={child.id} value={child.id}>{child.name} · {child.grade}.º</option>)}
            </select>
          </label>
          <label className="child-picker">Grado
            <select value={grade} disabled={fullAccess} onChange={event => chooseGrade(event.target.value)}>
              {[1, 2, 3, 4, 5].map(number => <option key={number} value={number}>{number}.º grado</option>)}
            </select>
          </label>
          {currentProgress && <div className="learning-score"><Icon name="star" size={19} /> <strong>{currentProgress.points}</strong> puntos <span>·</span> {currentProgress.completed}/{currentProgress.total} actividades</div>}
        </div>

        <div className="grade-filter-status" aria-live="polite">Actividades para <strong>{grade}.º grado</strong></div>

        <div className="filters">
          <div className="subject-tabs" aria-label="Materias">
            {subjects.map(item => <button type="button" className={subject === item ? "active" : ""} onClick={() => setSubject(item)} key={item}>{item}</button>)}
          </div>
          {currentProgress && <div className="overall-progress"><span>Progreso de {chosenChild?.name}</span><strong>{currentProgress.progress}%</strong><div className="progress-bar"><div className="progress-value" style={{ width: `${currentProgress.progress}%` }} /></div></div>}
        </div>

        {error && <div className="form-error" role="alert">{error}</div>}
        
        {fullAccess && <p className="select-child-hint">El progreso se guardará en el perfil de {chosenChild.name}.</p>}

        {subject === "Todas" && <section className="subject-module-grid" aria-label="Módulos de materias">
          {subjectModules.map(module => <button type="button" key={module.name} className={`subject-module ${availableSubjects.has(module.name) ? "" : "upcoming"}`} onClick={() => availableSubjects.has(module.name) ? window.location.href=`/materia/${encodeURIComponent(module.name)}?child=${childId}` : setSubject(module.name)}>
            <span className="module-icon" style={{ color: module.color, background: `${module.color}18` }}><Icon name={module.icon} size={25} /></span>
            <span className="module-copy"><strong>{module.name}</strong><small>{availableSubjects.has(module.name) ? module.description : "Próximamente · módulo en preparación"}</small></span>
            <Icon name="arrowRight" size={18} className="module-arrow" />
          </button>)}
        </section>}

        {!availableSubjects.has(subject) ? <section className="subject-coming-soon"><div className="coming-icon"><Icon name={subject === "Sociales" ? "globe" : subject === "Biología" ? "leaf" : "rainbow"} size={40} /></div><span className="eyebrow">PRÓXIMAMENTE</span><h2>{subject} llegará a Edutopia</h2><p>Este módulo ya aparece en la plataforma, pero todavía no tiene actividades disponibles.</p></section>
          : <section className="activity-grid" aria-label="Actividades de aprendizaje">
            {filtered.map(item => {
              const saved = currentProgress?.activities?.[item.key];
              return <article className="activity-card" key={item.key}>
                <div className="activity-art" style={{ background: item.color }}><Icon name={item.icon} size={52} /></div>
                <div className="activity-body">
                  <div className="activity-meta"><span>{item.subject}</span><b>{item.kind}</b></div>
                  <h2>{item.title}</h2><p>{item.description}</p>
                  <div className="activity-card-details"><span><Icon name="clock" size={15} /> {item.kind === "Juego" && !fullAccess ? "3 min de prueba" : `${item.minutes} min`}</span><span><Icon name="star" size={15} /> Hasta {item.points} puntos</span><span>{item.kind === "Juego" && !fullAccess ? "3 rondas de prueba" : `${item.questions.length} preguntas`}</span></div>
                  {saved && <div className="saved-score">Completada · mejor puntaje: <strong>{saved.best_score}</strong></div>}
                  <div className="activity-footer"><small>{item.kind === "Juego" && !fullAccess ? "Versión de prueba · 3 rondas" : item.kind === "Juego" ? "Juego completo" : "Lección + práctica"}</small><button type="button" disabled={Boolean(parent && !profilesLoaded)} onClick={() => startActivity(item)}>{saved ? "Volver a jugar" : "Empezar"} <Icon name="rocket" size={15} /></button></div>
                </div>
              </article>;
            })}
          </section>}
        {fullAccess && <div className="learn-note"><span><Icon name="lightbulb" size={25} /></span><p><strong>Tu avance queda guardado:</strong> puedes volver a intentar una actividad para superar tu mejor puntaje.</p></div>}
      </main>
      {active && <div className="activity-overlay" role="presentation" onMouseDown={event => { if (event.target === event.currentTarget) closeActivity(); }}>
        <section className="activity-modal" role="dialog" aria-modal="true" aria-labelledby="activity-title">
          <button className="modal-close" type="button" aria-label="Cerrar actividad" onClick={closeActivity}>×</button>
          <div className="modal-topline"><span>{active.subject}</span><span>{active.kind === "Juego" ? "Juego" : "Aprendizaje"}{active.limited ? " · versión de prueba" : ""}</span></div>
          <h2 id="activity-title">{active.title}</h2>
          {result ? <div className="activity-result"><div className="result-medal"><Icon name="star" size={38} /></div><h3>{result.message}</h3><p>Respondiste bien <strong>{result.correct} de {result.total}</strong> preguntas.</p><div className="result-points">+{result.earned} puntos</div><p className="result-best">{result.saved === false ? "Este puntaje es de prueba y no se guardó." : `Tu mejor puntaje: ${result.best_score} puntos`}</p>{!fullAccess && <p className="result-best">Inicia sesión y selecciona un perfil para guardar el progreso.</p>}<button className="activity-next-button" type="button" onClick={closeActivity}>Volver a las actividades</button></div>
            : step === -1 ? <div className="lesson-intro">{active.passage && <blockquote>{active.passage}</blockquote>}<h3>Lo que vas a aprender</h3><ul>{active.lesson.map(line => <li key={line}>{line}</li>)}</ul><button className="activity-next-button" type="button" onClick={() => setStep(0)}>¡Vamos a practicar! <Icon name="rocket" size={17} /></button></div>
              : <div className={`quiz-panel ${active.game || "lesson"}`}>
                <div className="quiz-progress"><span>Pregunta {step + 1} de {active.questions.length}</span><div className="progress-bar"><div className="progress-value" style={{ width: `${((step + 1) / active.questions.length) * 100}%` }} /></div></div>
                {active.game === "race" && <div className="race-track" aria-label={`Cohete avanzó ${Math.round((step / active.questions.length) * 100)} por ciento`}><Icon name="rocket" size={28} /><div><span style={{ width: `${(step / active.questions.length) * 100}%` }} /></div><Icon name="target" size={22} /></div>}
                <div className="game-hud"><span>❤️ {gameStats.lives}</span><span>⭐ {gameStats.score}</span><span>🔥 {gameStats.streak}</span><b>Nivel {Math.floor(step / 3) + 1}</b></div>
                {gameFeedback && <div className={`game-feedback ${gameFeedback.correct ? "good" : "bad"}`}>{gameFeedback.correct ? "¡Muy bien! +10 puntos" : "Casi. Observa la explicación."}</div>}
                <h3>{active.questions[step].prompt}</h3>
                <div className={active.game === "balloons" || active.game === "word-balloons" ? "balloon-field" : "answer-options"}>
                  {active.questions[step].options.map((option, index) => <button type="button" className={active.game === "balloons" || active.game === "word-balloons" ? `answer-balloon balloon-${index}` : answers[step] === index ? "selected" : ""} key={`${option}-${index}`} onClick={() => selectAnswer(index)}>{option}</button>)}
                </div>
                {error && <div className="form-error" role="alert">{error}</div>}
                <button className="activity-next-button" type="button" disabled={answers[step] === undefined || busy || (active.kind === "Juego" && !gameFeedback)} onClick={nextQuestion}>{busy ? "Guardando…" : step === active.questions.length - 1 ? fullAccess ? "Terminar y guardar puntos" : "Terminar prueba" : "Siguiente pregunta"} <Icon name="arrowRight" size={17} /></button>
              </div>}
        </section>
      </div>}
    </div>
  );
}
