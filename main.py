import collections
import graphviz

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour)               
                queue.append(neighbour)
                g.edge(str(vertex + 1), str(neighbour + 1)) # Добавление ребра в каркас

# Считывание графа. Форма входных данных — матрица смежности (в первой строке количество вершин графа)
f = open('graph_carc_input.txt', 'r')
n = int(f.readline())
graph = {x:[] for x in range(n)}

i = 0
for lines in f:
    j = 0
    for t in lines.split():
        if int(t) and j > i:
            graph[i].append(j)
        j += 1
    i += 1

# Создание нового графа — каркаса исходного
g = graphviz.Graph('G')
bfs(graph, 0)

# Визуализация с помощью graphviz
g.view()
