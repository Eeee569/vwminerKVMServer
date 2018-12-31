import mysql.connector

#https://www.w3schools.com/python/python_mysql_insert.asp


class mysql:

  def __init__(self,host,user,password,database):
    self.host = host
    self.user = user
    self.passwd = password
    self.database = database


    self.mydb = mysql.connector.connect(
      host="localhost",
      user="yourusername",
      passwd="yourpassword",
      database="mydatabase"

    )
  def __connect(self):
    return mysql.connector.connect(
      host=self.host,
      user=self.user,
      passwd=self.passwd,
      database=self.database
    )

  def exec(self,cmd):
    db = self.__connect(self)
    cursor = db.cursor()
    cursor.execute(cmd)
    db.close()#make sure this doesnt delete cursor data

    return cursor
  def exec(self,cmd,val):
    db = self.__connect(self)
    cursor = db.cursor()
    cursor.execute(cmd,val)
    db.commit()
    db.close()
    return cursor


