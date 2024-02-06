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
    
