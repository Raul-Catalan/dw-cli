import sqlite3
from datetime import date

def connection(filename="data.db"):
        try:
            con = sqlite3.connect(filename)
            cur = con.cursor()
            return con, cur
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to open DB: {e}") from e

def init_database():
        log_table = """
            CREATE TABLE IF NOT EXISTS deepwork (
            id INTEGER PRIMARY KEY,
            date,
            total_time,
            start_time,
            end_time,
            type_of_work,
            description
            );
        """
        con, cur = connection()
        if cur is None:
            print("Current is None")
            return None

        cur.execute(log_table)
        con.close()

def create(data):
    con, cur = connection()
    if cur is None:
        print("Error Accessing Database. \nCheck if Database is initialized")
        return 0
    sql = """
        INSERT INTO deepwork ( date, total_time, start_time, end_time, type_of_work, description )
        VALUES ( ?, ?, ?, ?, ?, ?)
    """
    cur.execute(sql, data)
    con.commit()
    con.close()

def read(id):
    con, cur = connection()
    sql = """
        SELECT * FROM deepwork
        WHERE id = ?
    """
    cur.execute(sql, id)
    rows = cur.fetchall()
    con.close()
    return rows

def read_all():
    con, cur = connection()
    sql = """
        SELECT * FROM deepwork
        """
    cur.execute(sql)
    rows = cur.fetchall()

    # print("Rows: ")
    # for row in rows:
    #    print(row)
    con.close()
    return rows

def update(id, data):
    con, cur = connection()
    if cur is None:
        print("Error Accessing Database. \nCheck if Database is initialized")
        return 0
    sql = """
        UPDATE deepwork 
        SET date = ?, total_time = ?, start_time = ?, end_time = ?, type_of_work = ?, description = ?
        WHERE id = ?
    """
    cur.execute(sql, data + (id,))
    num_rows = cur.rowcount
    con.commit()
    con.close()
    return num_rows

def delete(id):
    con, cur = connection()
    if cur is None:
        print("Error Accessing Database. \nCheck if Database is initialized")
        return 0
    sql = """
        DELETE FROM deepwork 
        WHERE id = ?
        RETURNING id, date
    """
    cur.execute(sql,(id,))
    deleted = cur.fetchall()
    con.commit()
    con.close()
    return deleted
