from core.pyba_logic import PybaLogic


class AdminLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUser(self, userName, userEmail, password):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `admin` "
            + "(`id`,`admin_name`,`admin_email`,`password`) "
            + f"VALUES(0,'{userName}','{userEmail}','{password}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getAdminByEmail(self, userEmail):
        database = self.createDatabaseObj()
        sql = (
            "SELECT admin_email, password "
            + f"FROM user where admin_email like '{userEmail}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getRowByAdmin(self, user):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM admin where admin_name like '{user}';"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []