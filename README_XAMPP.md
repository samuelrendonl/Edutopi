# Edutopia con XAMPP y MySQL

1. Abre XAMPP y enciende **Apache** y **MySQL**.
2. Para una instalación nueva, entra a `http://localhost/phpmyadmin`, pulsa **Importar** y selecciona `Backend/schema.sql`. Si ya tienes Edutopia instalada, conserva tus datos e importa únicamente `Backend/migrations/001_child_activity_progress.sql`.
3. En `Backend/.env` (o en el `.env` de la raíz) revisa:
   - `MYSQL_USER=root`
   - `MYSQL_PASSWORD=` (vacío si XAMPP no tiene contraseña)
   - `MYSQL_DATABASE=edutopia`
   - `SECRET_KEY`: opcional. Si no la defines, Edutopia crea una clave local privada en `.secret_key` para mantener activa la sesión entre reinicios. No publiques ese archivo.
4. Instala dependencias del backend y ejecútalo:

```bash
cd Backend
pip install -r requirements.txt
python app.py
```

5. En otra terminal inicia el frontend:

```bash
cd Frontend
npm install
npm run dev
```

La API queda en `http://localhost:5000/api` y el frontend en la dirección que muestre Vite.

## Aprendizajes y juegos

La pantalla **Aprender** trae exactamente cinco actividades iniciales: tres aprendizajes y dos juegos de Matemáticas y Lengua Castellana. Al entrar con una cuenta, elige el perfil infantil para guardar sus mejores puntajes y actividades completadas en MySQL. Cada nuevo perfil podrá usar automáticamente las cinco actividades.

Las visitas sin sesión pueden escoger un grado y practicar sin consultar perfiles familiares. Las lecciones se pueden completar en modo de prueba; cada juego ofrece tres rondas y los resultados no se guardan. Al iniciar sesión y elegir un perfil, se habilitan las actividades completas y el guardado de progreso. Sociales, Biología e Inglés aparecen como módulos próximos.

Al actualizar desde la versión anterior, cada adulto debe iniciar sesión una vez de nuevo. La sesión ahora usa una firma segura y la versión anterior no tenía ese dato.
