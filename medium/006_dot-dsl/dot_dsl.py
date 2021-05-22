NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        if data:
            if type(data) is not list:
                raise TypeError("Inserted data must be a list.")

            for d in data:
                if len(d) < 2:
                    raise TypeError("Value cannot be empty.")

                if d[0] == NODE:
                    if len(d) != 3:
                        raise ValueError("NODE takes exactly 3 parameters.")
                    self.nodes.append(Node(d[1], d[2]))
                elif d[0] == EDGE:
                    if len(d) != 4:
                        raise ValueError("EDGE takes exactly 4 parameters.")
                    self.edges.append(Edge(d[1], d[2], d[3]))
                elif d[0] == ATTR:
                    if len(d) != 3:
                        raise ValueError("ATTR takes exactly 2 parameters.")
                    self.attrs[d[1]] = d[2]
                else:
                    raise ValueError('Inserted item is unknown or the format is invalid.')
