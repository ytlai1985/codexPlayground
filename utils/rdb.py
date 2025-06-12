import mariadb
import os


def insert_message(message: str) -> None:
    """Insert a message into the `messages` table of the MariaDB database."""
    conn = mariadb.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'example'),
        database=os.getenv('DB_NAME', 'codex')
    )
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, message TEXT)"
    )
    cur.execute(
        "INSERT INTO messages (message) VALUES (?)",
        (message,)
    )
    conn.commit()
    cur.close()
    conn.close()

