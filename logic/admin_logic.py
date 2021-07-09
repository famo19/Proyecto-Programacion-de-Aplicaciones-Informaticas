from core.pyba_logic import PybaLogic


class AdminLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # OBTENER ID ADMIN
    def getIdAdmin(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT id FROM viajeentrelibros.admin;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
