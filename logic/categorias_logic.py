from core.pyba_logic import PybaLogic


class CategoriasLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # INSERTAR CATEGORIA
    def insertCat(self, nombre, id_Usuario):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `viajeentrelibros`.`categories` "
            + "(`id`,`nombre`,`idUsuario`) "
            + f"VALUES(0,'{nombre}',{id_Usuario});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # OBTENER TODAS LAS CATEGORIAS
    def getAllCats(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT id, nombre, idUsuario FROM viajeentrelibros.categories;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    # ELIMINAR CATEGORIA
    def deleteCat(self, id):
        database = self.createDatabaseObj()
        sql = sql = (
            "DELETE FROM `viajeentrelibros`.`categories` "
            + f"WHERE id={id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
