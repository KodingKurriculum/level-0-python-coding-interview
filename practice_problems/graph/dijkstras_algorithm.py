from plumbum import cli
from graph import Graph, inf
from collections import deque
import pprint

'''
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc
http://interactivepython.org/courselib/static/pythonds/Graphs/DijkstrasAlgorithm.html
'''
class DijkstrasAlgorithm(cli.Application):

    # a - 2  -> b - 7 -> |
    # |         | 10     |
    # | - 9  -> c        |
    # |         | 2      |
    # | - 14 -> d <- - - |

    _graph = Graph([
        ("a", "b", 2), ("a", "c", 9), ("b", "c", 10),
        ("b", "d", 7), ("a", "d", 14), ("c", "d", 2)
    ])

    def main(self):
        if list is None or len(self._graph.vertices) is 0:
            print("List should have at least one element")
            return 1
        else:
            dijkstras = self.run_dijkstras(self._graph, "a", "d")
            pprint.pprint(dijkstras)

    def run_dijkstras(self, graph, source, destination):

        # 1.)   Create a shortest path tree set, initially empty
        #       Optimization - use a parent path dict to retain previous short path
        shortest_path_tree = []
        previous_vertices = {vertex: None for vertex in graph.vertices}

        # 2.)   Creates a map of each vertex (variable) to infinity
        #       Set the source to 0
        distances = {vertex: inf for vertex in graph.vertices}
        distances[source] = 0

        # 3.)   While we have visited all vertices in set
        #       Technique is to create a copy, and remove from set as its consumed
        vertices = graph.vertices.copy()
        while vertices:

            # 4.)   Select node with the minimum distance value
            #       Once we pull from minimum distance, remove from our vertices
            next_node = min(vertices, key=lambda key: distances[key])
            vertices.remove(next_node)

            # 5.)   Add the minimum distance node to set
            #       ... As long as we're not left with all unreachable vertices
            if distances[next_node] == inf:
                break
            shortest_path_tree.append(next_node)
            distance = distances[next_node]

            # 6.)   Update the distance values the next node's neighbors
            neighbors = graph.neighbours[next_node]
            for neighbor, cost in neighbors:
                neighbor_distance = distance + cost

                #   ... either if we've found a shorter distance to neighbor
                #       or we haven't been here before
                if neighbor not in distances or \
                        (neighbor in distances
                            and neighbor_distance < distances[neighbor]):
                    distances[neighbor] = neighbor_distance
                    previous_vertices[neighbor] = next_node

        # 7.)   Work our way backwards from the destination and
        #       Find the shortest path by looking up in the previous_vertices map
        shortest_path, current_vertex = deque(), destination
        while previous_vertices[current_vertex] is not None:
            shortest_path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        #       When we reach the source, append to the path
        if shortest_path:
            shortest_path.appendleft(current_vertex)
        return shortest_path, distances

