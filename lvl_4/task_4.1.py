import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_name(school_id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sqlquery = 'SELECT * FROM School WHERE School_Id = ?'
    cursor.execute(sqlquery, (school_id,))
    school_info = cursor.fetchone()
    name = school_info[1]
    close_connection(con)
    return name
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка вида ", error)



def get_students_data(school_id):
  try:
    con = get_connection()
    cursor = con.cursor()
    sqlquery = 'SELECT * FROM Students WHERE Student_Id = ?'
    cursor.execute(sqlquery, (school_id,))
    students_info = cursor.fetchall()
    for row in students_info:
      print ("ID Студента:", row[0])
      print ("Имя Студента:", row[1])
      print ("ID школы:", row[2])
      print ("Название школы:", get_school_name(row[2]))
      
      
    close_connection(con)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка вида ", error)


get_students_data(202)