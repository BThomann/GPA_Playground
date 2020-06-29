class Node(object):
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def __str__(self):
        return self._name


class Edge(object):
    def __init__(self, src, dest):
        self._src = src
        self._dest = dest

    def getSource(self):
        return self._src

    def getDestination(self):
        return self._dest

    def __str__(self):
        return self._src.getName() + "->" + self._dest.getName()


class Digraph(object):
    def __init__(self):
        self._nodes = []
        self._edges = {}

    def addNode(self, node):
        if node in self._nodes:
            raise ValueError("Duplicate node")
        else:
            self._nodes.append(node)
            self._edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self._nodes and dest in self._nodes):
            raise ValueError("Node not in graph")
        self._edges[src].append(dest)

    def childrenOf(self, node):
        return self._edges[node]

    def hasNode(self, node):
        return node in self._nodes

    def __str__(self):
        result = ''
        for src in self._nodes:
            for dest in self._edges[src]:
                result = result + src.getName() + '->' \
                         + dest.getName() + '\n'
        return result[:-1]


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def printPath(path):
    result = ""
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + "->"
    return result


def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print("Current DFS path:", printPath(path))
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
    return shortest


def shortestPath(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)


def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print("Current BFS path:", printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


def test():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))
    sp = shortestPath(g, nodes[0], nodes[5], True)
    print("Shortest path found by DFS:", printPath(sp))
    bf = BFS(g, nodes[0], nodes[5], True)
    print("Shortest path found by DFS:", printPath(bf))


if __name__ == '__main__':
    test()
