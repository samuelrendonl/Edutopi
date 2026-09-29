import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { api, saveParent } from "../api";
import Icon from "../components/Icon";

export default function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  async function submit(event) {
    event.preventDefault(); setError(""); setLoading(true);
    try { const data = await api("/auth/login", { method: "POST", body: JSON.stringify(form) }); saveParent({ ...data.parent, token: data.token }); navigate("/Dashboard"); }
    catch (err) { setError(err.message); } finally { setLoading(false); }
  }
  return <div className="auth-page"><Navbar /><main className="auth-container"><div className="auth-card"><div className="auth-emoji"><Icon name="hand" size={52} /></div><span className="eyebrow">ZONA PARA FAMILIAS</span><h1>¡Hola, familia!</h1><p>Inicia sesión para acompañar cada aventura de aprendizaje.</p>{error && <div className="form-error">{error}</div>}<form onSubmit={submit}><div className="form-group"><label htmlFor="email">Correo del papá o mamá</label><input id="email" type="email" required value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} placeholder="familia@ejemplo.com" /></div><div className="form-group"><label htmlFor="password">Contraseña</label><input id="password" type="password" required value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} placeholder="Mínimo 6 caracteres" /></div><button className="auth-button" disabled={loading}>{loading ? "Entrando…" : "Entrar a mi familia"} <Icon name="rocket" size={18} /></button></form><p className="auth-footer">¿Primera vez en Edutopia? <Link to="/register">Crea tu cuenta</Link></p></div></main></div>;
}
