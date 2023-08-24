# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        copies = {None: None}

        def deep_copy(node):
            if node in copies:
                return copies[node]

            copies[node] = c_node = Node(node.val)
            c_node.neighbors = list(map(deep_copy, node.neighbors))

            return c_node

        return deep_copy(node)