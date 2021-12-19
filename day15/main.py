import numpy as np

def get_data():
    with open("input.txt", "r") as file:
        lines = [list(map(int, list(l.strip()))) for l in file.readlines()]
        
        return np.array(lines)

  
def get_to_compare(x, y, max_x, max_y):
    to_compare = []
    if x > 0:
        to_compare.append((x-1, y))
    if y > 0:
        to_compare.append((x, y-1))
    return to_compare

def quiz1():
    graph = get_data()
    weights = np.ones(graph.shape, dtype="int")*np.inf
    
    return dijkstra(graph, weights)

def dijkstra(graph, weights):
    again = False

    visited = np.zeros(graph.shape, dtype="bool")
    to_visit = {(0, 0)}
    weights[0, 0] = 0
    repeat = True
    while repeat:
        repeat = False
        to_visit = {(pos[0]+1, pos[1]) for pos in to_visit if pos[0] < graph.shape[0]-1 and not visited[pos[0]+1, pos[1]]} | {(pos[0], pos[1]+1) for pos in to_visit if pos[1] < graph.shape[1]-1 and not visited[pos[0], pos[1]+1]}        print(len(to_visit))
        for new_pos in to_visit:
            visited[new_pos] = True
            to_compare = get_to_compare(*new_pos, graph.shape[0]-1, graph.shape[1]-1)
            current_weight = weights[new_pos]
            minimum = min([weights[pos] + graph[new_pos] for pos in to_compare] + [current_weight])
            if minimum < current_weight:
                repeat = True
                weights[new_pos] = minimum
            if new_pos[0] == graph.shape[0]-1 and new_pos[1] == graph.shape[1]-1:
                return int(weights[graph.shape[0]-1, graph.shape[1]-1])
            
    return int(weights[graph.shape[0]-1, graph.shape[1]-1])

def quiz2():
    graph = get_data()
    new_graph = np.tile(graph, (5, 5))
    
    for i in range(5):
        for j in range(5):
            curx = graph.shape[0]*i
            cury = graph.shape[1]*j
            new_graph[curx:curx+graph.shape[0], cury:cury+graph.shape[1]] += i+j
    new_graph[new_graph > 9] -= 9
    weights = np.ones(new_graph.shape, dtype="int")*np.inf
    return dijkstra(new_graph, weights)

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
                