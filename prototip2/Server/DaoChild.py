from dadesServer import children, relation_user_child, User

class ChildDAO:
    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child

    def getChilds(self, user): 
        
        child_ids = {r['child_id'] for r in self.relation_user_child if r['user_id'] == user.id}
        
        return [c.__dict__ for c in self.childs if c.id in child_ids]

if __name__ == "__main__":
    cDao = ChildDAO()
    u = User(id=1, username="test", password="", email="", idrole=1)
    listChilds = cDao.getChilds(u)
    print(f"Hijos del usuario 1: {listChilds}")