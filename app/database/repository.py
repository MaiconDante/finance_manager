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
            payment_method TEXT,
            status TEXT
                    )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS finance_settings (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            setting_type TEXT,

            name TEXT

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
            payment_method,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        transaction.date.isoformat(),
        transaction.description,
        transaction.value,
        transaction.category,
        transaction.transaction_type,
        transaction.payment_method,
        transaction.status
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
                payment_method=row[6],
                status=row[7],
                id=row[0]
            )
        )

    return transactions


def update_transaction(transaction):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        UPDATE transactions

        SET
            description = ?,
            value = ?,
            category = ?,
            transaction_type = ?,
            payment_method = ?,
            status = ?

        WHERE id = ?

        """,
        (
            transaction.description,
            transaction.value,
            transaction.category,
            transaction.transaction_type,
            transaction.payment_method,
            transaction.status,
            transaction.id
        )
    )


    conn.commit()

    conn.close()


def delete_transaction(transaction):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM transactions
        WHERE id = ?
        """,
        (
            transaction.id,
        )
    )

    conn.commit()

    conn.close()
    
def insert_setting(setting_type, name):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO finance_settings
        (
            setting_type,
            name
        )

        VALUES (?, ?)

        """,
        (
            setting_type,
            name
        )
    )


    conn.commit()

    conn.close()

def get_settings(setting_type):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT name

        FROM finance_settings

        WHERE setting_type = ?

        """,
        (
            setting_type,
        )
    )


    rows = cursor.fetchall()


    conn.close()


    return [

        row[0]

        for row in rows

    ]

def delete_setting(name, setting_type):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM finance_settings

        WHERE name = ?

        AND setting_type = ?

        """,
        (
            name,
            setting_type
        )
    )


    conn.commit()

    conn.close()