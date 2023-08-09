class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        
        return level

    def print_tree(self, lvl):
        curr_level = self.get_level()
        if curr_level <= lvl:
            spaces = '   ' * self.get_level()
            prefix = spaces + "|__" if self.parent else ""
            print(prefix,self.data)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree(lvl)


def build_location_tree():
    glb = TreeNode("Global")

    ind = TreeNode("India")
    
    gj = TreeNode("Gujarat")
    gj.add_child(TreeNode("Ahmedabad"))
    gj.add_child(TreeNode("Baroda"))

    ka = TreeNode("Karnataka")
    ka.add_child(TreeNode("Bangluru"))
    ka.add_child(TreeNode("Bangluru"))


    ind.add_child(gj)
    ind.add_child(ka)

    us = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))


    cal = TreeNode("California")
    cal.add_child(TreeNode("San Francisco"))
    cal.add_child(TreeNode("Mountain View"))
    cal.add_child(TreeNode("Palo Alto"))

    us.add_child(nj)
    us.add_child(cal)

    glb.add_child(ind)
    glb.add_child(us)

    return glb

if __name__ == "__main__":
    root_node = build_location_tree()
    root_node.print_tree(0)
    root_node.print_tree(1)
    root_node.print_tree(2)
    root_node.print_tree(3)
    #root_node.print_tree(4)