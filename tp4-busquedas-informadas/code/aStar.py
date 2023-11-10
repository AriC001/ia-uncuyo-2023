from queue import PriorityQueue
from node import Node


def h(state, finish):
    return abs(state.state[0] - finish[0]) + abs(state.state[1] - finish[1])

def aStar(env, start, finish):
    node = Node(start)
    queue = PriorityQueue()
    queue.put((0, node))
    came_from = {}
    g = {node.state: 0}

    while not queue.empty():
        _, current = queue.get()  
  

        if current.state == finish:
            path = getPath(came_from, current)
            return path

        for action in ["up", "down", "left", "right"]:
            next_pos = env.performAction(current.state, action)

            if next_pos is not None and g[current.state] + 1 < g.get(next_pos, float('inf')):
                env.statesExplored += 1
                next_node = Node(state=next_pos, cost=g[current.state] + 1, parent=current)
                came_from[next_node] = current
                g[next_pos] = g[current.state] + 1
                f = g[next_pos] + h(next_node, finish)
                queue.put((f, next_node))
        
    return None

def getPath(came_from, current):
    path = [current.state]
    while current in came_from:
        current = came_from[current]
        path.append(current.state)
    path.reverse()
    return path