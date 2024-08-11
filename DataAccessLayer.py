import sqlite3

class DataAccessLayer:
    path = "Dpy1.db"

    # برای انجام عملیاتی که خروجی دارند مثل سلکت
    def ExecuteQuery(self, query):
        try:
            with sqlite3.connect(self.path) as connection:
                cursor = connection.cursor()
                results = cursor.execute(query)
            rows = results.fetchall()
        except Exception as error:
            rows = f"Error: {error}"
        return rows
    
    # برای انجام دستوراتی که خروجی ندارند: اینسرت، آپدیت، دیلیت
    def ExecuteNonQuery(self, query):
        try:
            with sqlite3.connect(self.path) as connection:
                connection.execute(query)
                connection.commit()
            message = "Operation Was Successfull!!!"
        except Exception as error:
            message = f"Error: {error}"
        return message