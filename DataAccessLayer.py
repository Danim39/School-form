import sqlite3

class DataAccessLayer:
    path = "Dpy1.db"

  
    def ExecuteQuery(self, query):
        try:
            with sqlite3.connect(self.path) as connection:
                cursor = connection.cursor()
                results = cursor.execute(query)
            rows = results.fetchall()
        except Exception as error:
            rows = f"Error: {error}"
        return rows
    
    
    def ExecuteNonQuery(self, query):
        try:
            with sqlite3.connect(self.path) as connection:
                connection.execute(query)
                connection.commit()
            message = "Operation Was Successfull!!!"
        except Exception as error:
            message = f"Error: {error}"
        return message