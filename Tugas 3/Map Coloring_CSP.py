class MapColoring:
    def __init__(self, country, graph):
        self.country = country
        self.graph = graph
        self.colors = {}
        
    def color_graph(self):
        for node in self.country:
            if node not in self.colors:
                for color in range(1, len(self.country) + 1):
                    if self.is_color_valid(node, color):
                        self.colors[node] = color
                        if self.color_graph():
                            return True
                        del self.colors[node]
                return False
        return True

    def is_color_valid(self, node, color):
        for neighbor in self.graph[node]:
            if neighbor in self.colors and self.colors[neighbor] == color:
                return False
        return True

country = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
graph = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

mc = MapColoring(country, graph)
mc.color_graph()

for node, color in mc.colors.items():
    print(f"{node}: {color}")