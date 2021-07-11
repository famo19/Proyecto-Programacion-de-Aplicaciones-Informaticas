from core.pyba_logic import PybaLogic

class HighlightsLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertHighlight(self, titulo, texto, notas, idUsuario):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `highlight` "
            + "(`idhighlight`,`titulo`,`texto`,`notas`,`idUsuario`) "
            + f"VALUES(0,'{titulo}','{texto}','{notas}','{idUsuario}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteHighlightByText(self, texto, idUsuario):
        database = self.createDatabaseObj()
        sql = (
            "DELETE"
            + f" FROM `highlight` where `texto` like '{texto}'and `idUsuario` like '{idUsuario}';"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getHighlightByUserId(self, userId):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `texto`"
            + f"FROM `highlight` where `idUsuario` like '{userId}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def getAllHighlightsByUserId(self, userId):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `titulo`,`texto`,`notas`"
            + f"FROM `highlight` where `idUsuario` like '{userId}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []
