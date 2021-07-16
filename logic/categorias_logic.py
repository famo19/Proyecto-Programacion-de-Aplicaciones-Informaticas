from core.pyba_logic import PybaLogic


class CategoriasLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    # INSERTAR CATEGORIA
    def insertCat(self, nombre, id_Usuario):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `categories` "
            + "(`id`,`nombre`,`idUsuario`) "
            + f"VALUES(0,'{nombre}',{id_Usuario});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    # OBTENER TODAS LAS CATEGORIAS
    def getAllCats(self):
        database = self.createDatabaseObj()
        sql = (
            "SELECT id, nombre, idUsuario FROM categories;"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    # OBTENER CATEGORIA POR ID
    def getCatById(self, idCat):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `nombre`"
            + f"FROM `categories` where `id` like '{idCat}';"
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
            "DELETE FROM `categories` "
            + f"WHERE id={id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
