from core.pyba_logic import PybaLogic


class ResumenLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # INSERTAR RESUMEN
    def insertRes(self, titulo, sinopsis, recomendacion, informacionDelAutor, contenido, idUsuario, idCategoria):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `resumen` "
            + "(`id`,`titulo`,`sinopsis`,`recomendación`,`informacionDelAutor`,`contenido`,`idUsuario`,`idCategoria`) "
            + f"VALUES(0,'{titulo}','{sinopsis}','{recomendacion}','{informacionDelAutor}','{contenido}',{idUsuario},{idCategoria});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # INSERTAR RESUMEN
    def updateRes(self, titulo, sinopsis, recomendacion, informacionDelAutor, contenido, idUsuario, idCategoria, id):
        database = self.createDatabaseObj()
        sql = (
            "UPDATE `resumen` SET "
            + f"`titulo` = '{titulo}',`sinopsis` = '{sinopsis}',`recomendación` = '{recomendacion}',`informacionDelAutor` = '{informacionDelAutor}',`contenido` = '{contenido}',`idUsuario` = {idUsuario },`idCategoria` = {idCategoria} WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # OBTENER TODOS LOS RESUMENES
    def getAllResumes(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * FROM resumen;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    # OBTENER SOLO UN RESUMEN
    def getResumenById(self, id):
        database = self.createDatabaseObj()
        sql = (
            f"SELECT * FROM resumen WHERE id={id};"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
    
    # OBTENER UN RESUMEN POR TITULO
    def getResumenByTitle(self, titulo):
        database = self.createDatabaseObj()
        sql = (
            f"SELECT * FROM resumen WHERE titulo='{titulo}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    # ELIMINAR RESUMEN
    def deleteResu(self, id):
        database = self.createDatabaseObj()
        sql = (
            "DELETE FROM `resumen` "
            + f"WHERE id={id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
