import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";
import { api, saveParent } from "../api";
import Icon from "../components/Icon";

export default function Register() {
  const navigate = useNavigate(); const [form, setForm] = useState({ name: "", email: "", password: "" }); const [error, setError] = useState(""); const [loading, setLoading] = useState(false);
  async function submit(event) { event.preventDefault(); setError(""); setLoading(true); try { const data = await api("/auth/register", { method: "POST", body: JSON.stringify(form) }); saveParent({ ...data.parent, token: data.token }); navigate("/register-child"); } catch (err) { setError(err.message); } finally { setLoading(false); } }
  return <div className="auth-page"><Navbar /><main className="auth-container"><div className="auth-card"><div className="auth-emoji"><Icon name="users" size={52} /></div><span className="eyebrow">CUENTA DEL ADULTO</span><h1>Comienza la aventura</h1><p>El registro lo realiza el papá, mamá o acudiente.</p>{error && <div className="form-error">{error}</div>}<form onSubmit={submit}><div className="form-group"><label htmlFor="name">Nombre del adulto</label><input id="name" required value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} placeholder="Ej. Laura García" /></div><div className="form-group"><label htmlFor="email">Correo electrónico</label><input id="email" type="email" required value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} placeholder="familia@ejemplo.com" /></div><div className="form-group"><label htmlFor="password">Crea una contraseña</label><input id="password" type="password" minLength="6" required value={form.password} onChange={e => setForm({ ...form, password: e.target.value })} placeholder="Mínimo 6 caracteres" /></div><button className="auth-button" disabled={loading}>{loading ? "Creando…" : "Crear cuenta familiar"} <Icon name="sparkles" size={18} /></button></form><p className="auth-footer">¿Ya tienes cuenta? <Link to="/login">Inicia sesión</Link></p></div></main></div>;
}
