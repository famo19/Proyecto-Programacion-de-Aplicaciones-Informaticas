from core.pyba_logic import PybaLogic

class BusquedaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getResumenByTitle(self,titulo):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `titulo`, `sinopsis`, `recomendación`, `informacionDelAutor`, `contenido`"
            + f"FROM `resumen` where `titulo` like '{titulo}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

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

    
    def getResumenByCategory(self, idcate):
        database = self.createDatabaseObj()
        sql = (
            "SELECT `titulo`, `sinopsis`, `recomendación`, `informacionDelAutor`, `contenido`"
            + f"FROM `resumen` where `idCategoria` like {idcate};"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []