import sqlite3

def create_connection():
    conn = sqlite3.connect('resume_optimizer.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        original_resume BLOB,
        optimized_resume BLOB,
        job_description TEXT,
        similarity_score REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    conn.commit()
    conn.close()

def save_resume(user_id, original_resume, optimized_resume, job_description, similarity_score):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO resumes (user_id, original_resume, optimized_resume, job_description, similarity_score)
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, original_resume, optimized_resume, job_description, similarity_score))
    
    conn.commit()
    conn.close()
