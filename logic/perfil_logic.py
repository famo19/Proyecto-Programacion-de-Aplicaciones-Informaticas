from core.pyba_logic import PybaLogic


class PerfilLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertPerfil(self, nombre, edad, pais, iduser):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `perfil` "
            + "(`idperfil`, `nombre`, `edad`, `pais`, `iduser`)  "
            + f"VALUES(0,'{nombre}','{edad}','{pais}','{iduser}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getPerfil(self, iduser):
        database = self.createDatabaseObj()
        sql = (
            "SELECT * FROM `perfil` "
            + f"where `iduser` like '{iduser}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result
        else:
            return []

    def updatePerfil(self, nombre, edad, pais, iduser):
        database = self.createDatabaseObj()
        sql = (
            "UPDATE `perfil` SET "
            + f"`nombre`='{nombre}', `edad`='{edad}', `pais`='{pais}'"
            + f"where `iduser` like '{iduser}';"
        )
        rows = database.executeNonQueryRows(sql)
        return rows
    