import mysql.connector
import time

print("Veritabanına bağlanılıyor...")

for _ in range(10):
    try:
        db = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="notes"
        )
        print("Bağlandı")
        break
    except:
        print("MySQL hazır değil, bekleniyor...")
        time.sleep(3)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    note VARCHAR(255)
)
""")

cursor.execute(
    "INSERT INTO notes (note) VALUES (%s)",
    ("DevOps tekrar projesi",)
)

db.commit()
print("Kayıt eklendi")
db.close()