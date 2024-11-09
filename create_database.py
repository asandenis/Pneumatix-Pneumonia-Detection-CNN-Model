import cx_Oracle
import config

def create_table():
    dsn_tns = cx_Oracle.makedsn(config.DB_CONFIG['host'], config.DB_CONFIG['port'], sid=config.DB_CONFIG['sid'])

    connection = cx_Oracle.connect(
        user=config.DB_CONFIG['username'],
        password=config.DB_CONFIG['password'],
        dsn=dsn_tns
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE chest_xray (
            id NUMBER PRIMARY KEY,
            image BLOB,
            label VARCHAR2(20)
        )
    """)

    cursor.execute("""
        CREATE SEQUENCE chest_xray_seq START WITH 1 INCREMENT BY 1
    """)

    cursor.execute("""
        CREATE OR REPLACE TRIGGER chest_xray_trigger
        BEFORE INSERT ON chest_xray
        FOR EACH ROW
        WHEN (NEW.id IS NULL)
        BEGIN
            SELECT chest_xray_seq.NEXTVAL INTO :NEW.id FROM dual;
        END;
    """)

    connection.commit()

    cursor.close()
    connection.close()

    print("Database table and supporting sequence/trigger created successfully.")

create_table()