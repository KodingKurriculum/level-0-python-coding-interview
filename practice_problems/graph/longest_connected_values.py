from plumbum import cli
import pprint

class LongestConnectedValues(cli.Application):
    # Making the assumption that values are not repeated!
    # 6 , 5 , 7
    # 1 , 4 , 8
    # 2 , 3 , 9
    _graph = {
        6: [1, 5],
        1: [6, 4, 2],
        2: [1, 3],
        5: [6, 4, 7],
        4: [5, 8, 3, 1],
        3: [2, 4, 9],
        7: [5, 8],
        8: [7, 4, 9],
        9: [3, 8]
    }

    def main(self):
        if list is None or len(self._graph) is 0:
            print("List should have at least one element")
            return 1
        else:
            longest = self.search_graph(self._graph)
            pprint.pprint(longest)

    def search_graph(self, graph):
        found_longest = {}

        for parent,children in graph.items():
            found_longest[parent] = self.find_longest(graph, parent, children, [parent], found_longest)
        return found_longest

    def find_longest(self, graph, parent, children, longest, found_longest):
            for child in children:
                if parent+1 == child:
                    if child in found_longest:
                        longest.extend(found_longest[child])
                    else:
                        longest.append(child)
                        self.find_longest(graph, child, graph[child], longest, found_longest)

            return longest