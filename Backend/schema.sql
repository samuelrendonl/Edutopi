CREATE DATABASE IF NOT EXISTS edutopia CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE edutopia;

CREATE TABLE IF NOT EXISTS parents (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(180) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS children (
  id INT AUTO_INCREMENT PRIMARY KEY,
  parent_id INT NOT NULL,
  name VARCHAR(120) NOT NULL,
  age TINYINT NOT NULL,
  grade TINYINT NOT NULL,
  avatar VARCHAR(10) DEFAULT '🌟',
  progress TINYINT DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_children_parent FOREIGN KEY (parent_id) REFERENCES parents(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS activities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  subject VARCHAR(60) NOT NULL,
  icon VARCHAR(10) NOT NULL,
  color VARCHAR(20) NOT NULL,
  grade TINYINT NOT NULL,
  title VARCHAR(140) NOT NULL,
  description VARCHAR(255) NOT NULL,
  type VARCHAR(40) NOT NULL,
  points SMALLINT DEFAULT 10
);

-- Puntaje y avances independientes por niño y actividad.
CREATE TABLE IF NOT EXISTS child_activity_progress (
  id INT AUTO_INCREMENT PRIMARY KEY,
  child_id INT NOT NULL,
  activity_key VARCHAR(80) NOT NULL,
  best_score SMALLINT UNSIGNED NOT NULL DEFAULT 0,
  attempts SMALLINT UNSIGNED NOT NULL DEFAULT 1,
  completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY uq_child_activity (child_id, activity_key),
  INDEX idx_progress_child (child_id),
  CONSTRAINT fk_progress_child FOREIGN KEY (child_id) REFERENCES children(id) ON DELETE CASCADE
) ENGINE=InnoDB;

INSERT INTO activities (subject, icon, color, grade, title, description, type, points)
SELECT * FROM (SELECT 'Matemáticas','🔢','#5b5ce2',1,'Suma con estrellas','Resuelve sumas y alcanza la luna.','Reto',20) AS seed
WHERE NOT EXISTS (SELECT 1 FROM activities);
INSERT INTO activities (subject, icon, color, grade, title, description, type, points) VALUES
('Matemáticas','🔢','#5b5ce2',3,'Detectives de fracciones','Encuentra la fracción que falta.','Juego',30),
('Lenguaje','📚','#f28c28',1,'Caza de palabras','Forma palabras con las letras mágicas.','Juego',20),
('Lenguaje','📚','#f28c28',4,'Historias viajeras','Ordena las escenas de un cuento.','Lectura',25),
('Ciencias','🌱','#21c7a8',2,'Mi laboratorio','Descubre cómo crecen las plantas.','Experimento',30),
('Ciencias','🌱','#21c7a8',5,'Viaje al sistema solar','Explora los planetas y sus secretos.','Explorar',25),
('Sociales','🌎','#ef6685',3,'Mi comunidad','Conoce los lugares que nos rodean.','Misión',20),
('Inglés','🌈','#45a5e8',1,'Colors around me','Aprende los colores jugando.','Quiz',20);
