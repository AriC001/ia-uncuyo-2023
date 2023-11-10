class Node:
    def __init__(self, state, cost=0, parent=None):
        self.parent = parent
        self.state = state
        self.cost = cost
    
    def __lt__(self, other):
        return self.cost < other.cost