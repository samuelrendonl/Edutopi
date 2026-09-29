USE edutopia;

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
