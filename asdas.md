Crea un diagra de arquitectura en Mermaid:
Bloc Cliente:
Vista : (Input Nom) <-> DaoClient (getUserName) <- http ->
Bloc Servidor:
WebService (getUserByName) <-> Dao (getUserByName) <-> List Data Users
