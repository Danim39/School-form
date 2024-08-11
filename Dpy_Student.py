from DataAccessLayer import DataAccessLayer

class Student:
    dal = DataAccessLayer()

    def SelectInfo(self):
        query = "SELECT * FROM TBLDpy"
        rows = self.dal.ExecuteQuery(query)
        return rows

    def SearchInfo(self, value, filter, condition):
    
        match condition:
            case "Starts With":
                query = f"SELECT * FROM TBLDpy WHERE {filter} like '{value}%'"
            case "Ends With":
                query = f"SELECT * FROM TBLDpy WHERE {filter} like '%{value}'"
            case "Contains":
                query = f"SELECT * FROM TBLDpy WHERE {filter} like '%{value}%'"
            case "Equals With":
                query = f"SELECT * FROM TBLDpy WHERE {filter} = '{value}'"
        if filter == "Id":
            query = f"SELECT * FROM TBLDpy WHERE {filter} = {value}"
        rows = self.dal.ExecuteQuery(query)
        return rows

    def AddInfo(self, id, name, family, age , score):
        query = f"INSERT INTO TBLDpy ('id','name','family','age' ,'score') VALUES ({id},'{name}','{family}','{age}' ,'{score}')"
        message = self.dal.ExecuteQuery(query)
        return message

    def EditInfo(self, id, name, family, age , score):
        query = f"UPDATE TBLDpy SET 'name'='{name}', 'family'='{family}', 'age'={age} , 'score'={score} WHERE id={id}"
        message = self.dal.ExecuteQuery(query)
        return message
       

    def DeleteInfo(self, id):
        query = f"DELETE FROM TBLDpy WHERE id={id}"
        message = self.dal.ExecuteNonQuery(query)
        return message