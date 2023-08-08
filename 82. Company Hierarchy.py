class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
    
    def print_tree(self, style):
        if style.upper() == "NAME":
            spaces = "   " * self.get_level()
            prefix = spaces + "|__" if self.parent else ""
            print(prefix, self.name)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree(style)

        elif style.upper() == "DESIGNATION":
            spaces = "   " * self.get_level()
            prefix = spaces + "|__" if self.parent else ""
            print(prefix, self.designation)
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree(style)

        elif style.upper() == "BOTH":
            spaces = "   " * self.get_level()
            prefix = spaces + "|__" if self.parent else ""
            print(prefix, self.name, ' (', self.designation, ')')
            if len(self.children) > 0:
                for child in self.children:
                    child.print_tree(style)

        else:
            print("Please enter a valid style to display the hierarchy.")

def build_management_tree():
    ceo = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    
    infra_hd = TreeNode("Vishwa", "Infrastructure Head")
    infra_hd.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra_hd.add_child(TreeNode("Abhijit", "App Manager"))

    app_hd = TreeNode("Aamir", "Application Head")

    cto.add_child(infra_hd)
    cto.add_child(app_hd)

    hr_hd = TreeNode("Gels", "HR Head")
    hr_hd.add_child(TreeNode("Peter", "Recruitment Head"))
    hr_hd.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo.add_child(cto)
    ceo.add_child(hr_hd)

    return ceo



if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy