# graph = {
#         '1': ['2', '3', '4'],
#         '2': ['5', '6'],
#         '5': ['9', '10'],
#         '4': ['7', '8'],
#         '7': ['11', '12']
#         }


from collections import deque

def bfs(graph, start=None, end=None):
    path = []
    queue = deque([])

    queue.append([start])

    while len(queue):
        current = queue.popleft()
        path.append([current[0]])
        print current
        for node in graph.get(current[0], []):
            if node == end:
                return path
            queue.append([node])
    return 'not found'

def main():

    graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

    bfs(graph, '1', '7')

main()
