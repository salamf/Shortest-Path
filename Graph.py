class Graph:
    """ Graph adjacency list (using dict) implementation """

    def __init__(self):
        self.dict = {}
        self.num_vertices = 0

    def add_edge(self, vertex, edge):
        """ Insert a vertex and edge into graph
            if vertex exists, just add the edge to it """

        if vertex not in self.dict:
            self.dict[vertex] = [edge]
            self.num_vertices += 1
        else:
            self.dict[vertex].append(edge)

    def find_shortest_path(self, data, start, end):
        """ Find shortest path from vertex at pos 'start' to vertex
            at pos 'end' using breadth-first search traversal
            (O(v + e)) """

        visited = [False] * self.num_vertices

        queue = [start]
        visited[start] = True

        dist = [0] * self.num_vertices

        while queue:
            pos = queue.pop(0)

            if pos == end:
                break

            neighbours = self.dict[pos]

            for neighbour in neighbours:
                if not visited[neighbour] and data[neighbour] != '#':
                    queue.append(neighbour)
                    visited[neighbour] = True
                    dist[neighbour] = dist[pos] + 1

        if dist[end] == 0:
            return -1

        return dist[end]

    def __repr__(self):
        res = ""
        for k, v in self.dict.items():
            res += str(k) + " " + str(v) + "\n"

        return res
