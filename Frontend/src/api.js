export const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000/api";

export async function api(path, options = {}) {
  const parent = getParent();
  const response = await fetch(`${API_URL}${path}`, {
    headers: { "Content-Type": "application/json", ...(parent?.token ? { "X-Auth-Token": parent.token } : {}), ...options.headers },
    ...options,
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    if (response.status === 401 && parent) logout();
    const error = new Error(data.error || "No pudimos completar la solicitud.");
    error.status = response.status;
    throw error;
  }
  return data;
}

export const saveParent = (parent) => {
  localStorage.setItem("edutopia_parent", JSON.stringify(parent));
  window.dispatchEvent(new Event("edutopia-auth-change"));
};
export function getParent() {
  try {
    const parent = JSON.parse(localStorage.getItem("edutopia_parent") || "null");
    if (parent?.token) return parent;
    if (parent) localStorage.removeItem("edutopia_parent");
  } catch {
    localStorage.removeItem("edutopia_parent");
  }
  return null;
}
export const logout = () => {
  localStorage.removeItem("edutopia_parent");
  window.dispatchEvent(new Event("edutopia-auth-change"));
};

const LEARNING_CACHE_KEY = "edutopia_learning_catalog_v3";
const CACHE_MAX_AGE = 6 * 60 * 60 * 1000;

export function getCachedLearningCatalog(grade = 3) {
  try {
    const all = JSON.parse(localStorage.getItem(LEARNING_CACHE_KEY) || "{}");
    const cache = all[grade];
    return cache && Date.now() - cache.savedAt < CACHE_MAX_AGE ? cache.activities : null;
  } catch {
    return null;
  }
}

export function cacheLearningCatalog(activities, grade = 3) {
  try {
    const all = JSON.parse(localStorage.getItem(LEARNING_CACHE_KEY) || "{}");
    all[grade] = { savedAt: Date.now(), activities };
    localStorage.setItem(LEARNING_CACHE_KEY, JSON.stringify(all));
  } catch {
    // El catálogo siempre está disponible desde la API aunque el almacenamiento esté lleno.
  }
}
