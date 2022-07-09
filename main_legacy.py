from fastapi import FastAPI
from mysql.connector import MySQLConnection, connect
from mysql.connector.cursor import MySQLCursor
import queries

app = FastAPI()


def get_connection() -> MySQLConnection:
    return connect(
        user="admin",
        password="!Dallantsea992213",
        port=3306,
        host="dallant-music-develop.c8ki1rplwmad.us-east-1.rds.amazonaws.com",
        database="dallantmusic",
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/instructor/student_list/{inst_id}")
async def instructor_student_list(inst_id):
    cnx: MySQLConnection = get_connection()
    cursor: MySQLCursor = cnx.cursor()

    cursor.execute(queries.INSTRUCTOR_STUDENTS_LIST, (inst_id,))
    result = cursor.fetchall()

    return {"message": result}
