import sqlite3
import json
from datetime import datetime

DB_PATH = "drishit_cases.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_id TEXT UNIQUE,
            io_name TEXT,
            case_type TEXT,
            status TEXT DEFAULT 'In Progress',
            created_at TEXT,
            updated_at TEXT,
            files_count INTEGER DEFAULT 0,
            entities_count INTEGER DEFAULT 0,
            prime_suspect TEXT,
            risk_score INTEGER DEFAULT 0,
            total_amount REAL DEFAULT 0,
            report_json TEXT
        )
    """)
    c.execute("CREATE INDEX IF NOT EXISTS idx_case_id ON cases(case_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_status ON cases(status)")
    conn.commit()
    conn.close()

def save_case(case_id, io_name, case_type, files_count, entities_count, prime, risk, amount, report_data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.now().isoformat()
    c.execute("""
        INSERT OR REPLACE INTO cases 
        (case_id, io_name, case_type, created_at, updated_at, files_count, entities_count, prime_suspect, risk_score, total_amount, report_json, status)
        VALUES (?, ?, ?, COALESCE((SELECT created_at FROM cases WHERE case_id=?), ?), ?, ?, ?, ?, ?, ?, ?, 'In Progress')
    """, (case_id, io_name, case_type, case_id, now, now, files_count, entities_count, prime, risk, amount, json.dumps(report_data)))
    conn.commit()
    conn.close()

def get_all_cases():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT case_id, io_name, case_type, status, updated_at, files_count, entities_count, prime_suspect, risk_score, total_amount FROM cases ORDER BY updated_at DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    return rows

def get_case(case_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM cases WHERE case_id=?", (case_id,))
    row = c.fetchone()
    conn.close()
    return row

def delete_case(case_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM cases WHERE case_id=?", (case_id,))
    conn.commit()
    conn.close()

def get_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*), SUM(files_count), SUM(entities_count), AVG(risk_score) FROM cases")
    row = c.fetchone()
    conn.close()
    return {
        "total_cases": row[0] or 0,
        "total_files": row[1] or 0,
        "total_entities": row[2] or 0,
        "avg_risk": round(row[3] or 0, 1)
    }

init_db()