class ChildDAO:
    def __init__(self):
        self.childs = children
        self.relation_user_child = relation_user_child

    def getChilds(self, user): 
        # Get IDs from relations
        child_ids = {r['child_id'] 
                     for r in self.relation_user_child if r['user_id'] == user.id}
        # Return Child objects
        return [c.__dict__ for c in self.childs if c.id in child_ids]

cDao = ChildDAO()
u=User(id=1, username="", password="", email="", idrole=1, token="")
listChilds=cDao.getChilds(u)
print(listChilds)