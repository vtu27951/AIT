vertices = ["v1", "v2", "v3", "v4"]

graph = {
    "v1": ["v2", "v3"],
    "v2": ["v1", "v3", "v4"],
    "v3": ["v1", "v2", "v4"],
    "v4": ["v3", "v2"]
}

num_colors = 3

color = {v: 0 for v in vertices}


def is_safe(vertex, c):
    for neighbour in graph[vertex]:
        if color[neighbour] == c:
            return False
    return True


def graph_coloring(index):
    if index == len(vertices):
        return True

    vertex = vertices[index]

    for c in range(1, num_colors + 1):
        if is_safe(vertex, c):
            color[vertex] = c

            if graph_coloring(index + 1):
                return True

            color[vertex] = 0

    return False


if graph_coloring(0):
    print("Graph can be colored using", num_colors, "colors.")
    print("Color assignment:", color)
else:
    print("Graph cannot be colored using", num_colors, "colors.")
