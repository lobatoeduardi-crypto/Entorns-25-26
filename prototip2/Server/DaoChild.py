from dadesServer import children, relation_user_child, User

class ChildDAO:
    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child

    def getChilds(self, user): 
        # Sacamos los IDs de los niños relacionados con ese usuario
        child_ids = {r['child_id'] for r in self.relation_user_child if r['user_id'] == user.id}
        
        # Devolvemos los diccionarios de esos niños
        return [c.__dict__ for c in self.childs if c.id in child_ids]

# --- Bloque de prueba (lo que pedía el profe) ---
if __name__ == "__main__":
    cDao = ChildDAO()
    # Creamos un usuario de prueba con ID 1
    u = User(id=1, username="test", password="", email="", idrole=1)
    listChilds = cDao.getChilds(u)
    print(f"Hijos del usuario 1: {listChilds}")