from db_interface import get_connection

conn = get_connection()
if conn:
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for table in cursor.fetchall():
        print(table)
    cursor.close()
    conn.close()
