import sqlite3

def create_table():

    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()

    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS patients(

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            dob TEXT,
            email TEXT,
            glucose REAL,
            haemoglobin REAL,
            cholesterol REAL,
            remarks TEXT

        )
        '''
    )

    conn.commit()
    conn.close()


def add_patient(
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
):
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()

    cur.execute(
        '''
        INSERT INTO patients
        (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        VALUES(?,?,?,?,?,?,?)
        ''',

        (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )
    )
    conn.commit()
    conn.close()


def view_patients():

    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM patients"
    )

    data = cur.fetchall()
    
    conn.close()

    return data

def delete_patient(id):

    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM patients WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()


def update_patient(
        id,
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        remarks
):
    
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()

    cur.execute(
        '''
        UPDATE patients
        
        SET

        full_name=?,
        dob=?,
        email=?,
        glucose=?,
        haemoglobin=?,
        cholesterol=?,
        remarks=?

        WHERE id=?

        ''',

        (
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks,
            id

        )
    )

    conn.commit()
    conn.close()
