"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.cloneMap = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        clone = Node(node.val)
        self.cloneMap[node] = clone

        for neighbor in node.neighbors:
            if neighbor not in self.cloneMap:
                self.cloneGraph(neighbor)
            clone.neighbors.append(self.cloneMap[neighbor])

        return clone