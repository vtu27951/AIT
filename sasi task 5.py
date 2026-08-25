import random

random.seed(42)

places = ["A", "B", "C","D"]

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
    
]

n = len(places)
ants = 20
iterations = 500

alpha = 1
beta = 2
rho = 0.5
Q = 100

pheromone = [[1.0] * n for _ in range(n)]

def route_distance(route):
    total = 0
    for i in range(n - 1):
        total += distance[route[i]][route[i + 1]]
    total += distance[route[-1]][route[0]]
    return total

best_route = None
best_dist = float("inf")

for _ in range(iterations):

    routes = []

    for _ in range(ants):
        route = [0]
        unvisited = list(range(1, n))

        while unvisited:
            current = route[-1]
            probabilities = []

            for city in unvisited:
                p = (pheromone[current][city] ** alpha) * \
                    ((1 / distance[current][city]) ** beta)
                probabilities.append(p)

            next_city = random.choices(
                unvisited, weights=probabilities
            )[0]

            route.append(next_city)
            unvisited.remove(next_city)

        d = route_distance(route)
        routes.append((route, d))

        if d < best_dist:
            best_dist = d
            best_route = route[:]

    # Evaporation
    for i in range(n):
        for j in range(n):
            pheromone[i][j] *= (1 - rho)

    # Pheromone update
    for route, d in routes:
        amount = Q / d

        for i in range(n):
            a = route[i]
            b = route[(i + 1) % n]

            pheromone[a][b] += amount
            pheromone[b][a] += amount

print("Best Route:")
print(" -> ".join(places[i] for i in best_route))
print(" ->", places[best_route[0]])

print("Minimum Distance:", best_dist, "km")
