from flask import Flask
import sqlite3

app=Flask(__name__)
DB="student.db"

def init_db():
    conn= sqlite3.connect(DB)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students(
    
    );
    """)