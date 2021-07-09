from core.pyba_logic import PybaLogic

class HighlightsLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertHighlight(self, titulo, texto, idUsuario):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `highlight` "
            + "(`id`,`titulo`,`texto`,`idUsuario`) "
            + f"VALUES(0,'{titulo}','{texto}','{idUsuario}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows