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
    
    