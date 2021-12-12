import sys

def get_data():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        lines = [tuple(l.strip().split('-')) for l in lines]
        result = {}
        for line in lines:
            if not line[0] in result:
                result[line[0]] = []
            if not line[1] in result:
                result[line[1]] = []
            result[line[0]].append(line[1])
            result[line[1]].append(line[0])

        return result

def visit_graph_quiz1(graph, current_node, visited_lowers):
    if current_node in visited_lowers:
        return 0
    if current_node == 'end':
        return 1
    else:
        if current_node.islower():
            visited_lowers.add(current_node)
        next_nodes = graph[current_node]
        return sum([visit_graph_quiz1(graph, node, visited_lowers.copy()) for node in next_nodes])
                

def visit_graph_quiz2(graph, current_node, visited_lowers, temp):
    if current_node == 'end':
        return 1
    else:
        if current_node.islower():
            visited_lowers.add(current_node)
        next_nodes = graph[current_node]
        total = sum([visit_graph_quiz2(graph, node, visited_lowers, temp) for node in next_nodes if not node in visited_lowers])
        if temp == None: 
            total += sum([visit_graph_quiz2(graph, node, visited_lowers, node) for node in next_nodes if node in visited_lowers and node != 'start'])
        if current_node != temp:
            visited_lowers.discard(current_node)
        return total

def quiz1():
    graph = get_data()
    return visit_graph_quiz1(graph, 'start', set())

def quiz2():
    graph = get_data()
    return visit_graph_quiz2(graph, "start", set(), None)
    

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())