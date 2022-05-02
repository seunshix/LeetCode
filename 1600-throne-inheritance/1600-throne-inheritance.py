import collections
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.children = collections.defaultdict(list)
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        res = []
        def dfs(x):
            nonlocal res
            if x not in self.dead:
                res.append(x)
            for child in self.children[x]:
                dfs(child)
        dfs(self.kingName)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()