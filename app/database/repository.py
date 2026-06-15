from datetime import date
from app.models.transaction import Transaction
from app.database.database import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            description TEXT,
            value REAL,
            category TEXT,
            transaction_type TEXT,
            payment_method TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_transaction(transaction):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions (
            date,
            description,
            value,
            category,
            transaction_type,
            payment_method
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        transaction.date.isoformat(),
        transaction.description,
        transaction.value,
        transaction.category,
        transaction.transaction_type,
        transaction.payment_method
    ))

    conn.commit()
    conn.close()

def get_all_transactions():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()

    conn.close()

    transactions = []

    for row in rows:
        transactions.append(
            Transaction(
                date=date.fromisoformat(row[1]),
                description=row[2],
                value=row[3],
                category=row[4],
                transaction_type=row[5],
                payment_method=row[6]
            )
        )

    return transactions
