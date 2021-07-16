from core.pyba_logic import PybaLogic

class LibreriaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertBook(self, titulo, sinopsis, recomendacion, informacionDelAutor, contenido, idUsuario, idCategoria, idResumen):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `libreria` "
            + "(`idlibreria`,`titulo`,`sinopsis`,`recomendacion`,`informacionDelAutor`, `contenido`, `idUsuario`, `idCategoria`, `idResumen`) "
            + f"VALUES(0,'{titulo}','{sinopsis}','{recomendacion}','{informacionDelAutor}','{contenido}','{idUsuario}','{idCategoria}','{idResumen}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getLibroByUserId(self, userId):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `titulo`, `sinopsis`, `recomendacion`, `informacionDelAutor`, `contenido`"
            + f"FROM `libreria` where `idUsuario` like '{userId}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def getLibroByTitle(self, title):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `titulo`, `sinopsis`, `recomendación`, `informacionDelAutor`, `contenido`, `idCategoria`"
            + f"FROM `resumen` where `titulo` like '{title}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []     
    
    def deleteBookByTitle(self, titulo, idUsuario):
        database = self.createDatabaseObj()
        sql = (
            "DELETE"
            + f" FROM `libreria` where `titulo` like '{titulo}'and `idUsuario` like '{idUsuario}';"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    """def getRowByUser(self, user):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM user where user_name like '{user}';"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []"""