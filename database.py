import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect("data.db", check_same_thread=False)
cur = conn.cursor()

def init_db():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        wallet TEXT,
        points INTEGER DEFAULT 0,
        last_message TIMESTAMP
    )""")
    conn.commit()

def update_points(user_id, username):
    now = datetime.now()
    cur.execute("SELECT last_message FROM users WHERE user_id=?", (user_id,))
    res = cur.fetchone()
    
    if res and res[0]:
        last_time = datetime.fromisoformat(res[0])
        if now - last_time < timedelta(seconds=60):
            return False  # 冷却中，不增加积分

    cur.execute("INSERT OR IGNORE INTO users (user_id, username, points) VALUES (?, ?, 0)", (user_id, username))
    cur.execute("UPDATE users SET points = points + 1, last_message=? WHERE user_id=?", (now, user_id))
    conn.commit()
    return True

def bind_wallet(user_id, wallet):
    cur.execute("UPDATE users SET wallet=? WHERE user_id=?", (wallet, user_id))
    conn.commit()

def get_user(user_id):
    cur.execute("SELECT wallet, points FROM users WHERE user_id=?", (user_id,))
    return cur.fetchone()

def reset_points(user_id):
    cur.execute("UPDATE users SET points=0 WHERE user_id=?", (user_id,))
    conn.commit()

init_db()
