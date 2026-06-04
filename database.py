import sqlite3


def getconn():
    return sqlite3.connect("patients.db")


def createdb():

    conn = getconn()

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS patients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            dob TEXT,
            email TEXT,
            glucose REAL,
            hemoglobin REAL,
            cholestrol REAL,
            disease TEXT,
            remarks TEXT
        )
    """)

    conn.commit()
    conn.close()


def addpatient(fullname, dob, email, glucose, hemoglobin, cholestrol,disease, remarks):

    conn = getconn()

    cur = conn.cursor()

    cur.execute("""
        INSERT INTO patients
        (
            fullname,
            dob,
            email,
            glucose,
            hemoglobin,
            cholestrol,
            disease,
            remarks
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        fullname,
        dob,
        email,
        glucose,
        hemoglobin,
        cholestrol,
        disease,
        remarks
    ))

    conn.commit()
    conn.close()


def getpatients():

    conn = getconn()

    cur = conn.cursor()

    cur.execute("SELECT * FROM patients")

    rows = cur.fetchall()

    conn.close()

    return rows


def getpatient(pid):

    conn = getconn()

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM patients WHERE id=?",
        (pid,)
    )

    row = cur.fetchone()

    conn.close()

    return row


def updatepatient(pid, fullname, dob, email, glucose, hemoglobin, cholestrol, disease, remarks):

    conn = getconn()

    cur = conn.cursor()

    cur.execute("""
        UPDATE patients
        SET fullname=?,
            dob=?,
            email=?,
            glucose=?,
            hemoglobin=?,
            cholestrol=?,
            disease=?,
            remarks=?
        WHERE id=?
    """,
    (
        fullname,
        dob,
        email,
        glucose,
        hemoglobin,
        cholestrol,
        disease,
        remarks,
        pid
    ))

    conn.commit()
    conn.close()


def deletepatient(pid):

    conn = getconn()

    cur = conn.cursor()

    cur.execute(
        "DELETE FROM patients WHERE id=?",
        (pid,)
    )

    conn.commit()
    conn.close()


createdb()