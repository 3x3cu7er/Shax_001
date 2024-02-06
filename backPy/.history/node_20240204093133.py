class Node:

    def __init__(self, parent, state, action):
        self.parent = parent
        self.action = action
        self.state = state
        

class StackPointer:

    def __init__(self):
        self.frontier = []
        
    def add(self, node):
        return self.frontier.append(node)
    
    def exists(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0

    def remove(self, node):
        if self.empty():
            raise Exception("Node is empty")
        else:
            node = self.frontier[:-1]
            self.frontier = self.frontier[:-1]
            return node
