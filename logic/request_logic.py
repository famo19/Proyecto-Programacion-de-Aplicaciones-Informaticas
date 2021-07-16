from core.pyba_logic import PybaLogic


class RequestLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertRequest(self,User_name,User_email,Book_name,Book_year,Book_author,message):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `request`(`idrequest`,`User_name`,`User_email`,`Book_name`,`Book_year`,`Book_author`,`message`)"
            + f"VALUES(0,'{User_name}','{User_email}',{Book_name}','{Book_year}','{Book_author}','{message}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
    
    def getRequestByBook(self, Book_name):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `User_name`,`User_email`,`Book_name`,`Book_year`,`Book_author`,`message`"
            + f"FROM request where `Book_name` like '{Book_name}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
        
    def deleteRequestByBook(self, Book_name, idrequest):
        database = self.createDatabaseObj()
        sql = (
            "DELETE FROM `request`"
            + f"WHERE `Book_name` like '{Book_name}' and `idrequest` like '{idrequest}';"
        )
        rows = database.executeNonQueryRows(sql)
        return rows