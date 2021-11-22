def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {}
graph['start'] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['v'] = 4
graph['a']['k'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['k'] = 7
graph['v'] = {}
graph['v']['k'] = 6
graph['v']['fin'] = 3
graph['k'] = {}
graph['k']['fin'] = 1
graph['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 5
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
processed = []
node = find_lowest_cost_node(costs)
print(parents)
print(costs)
print(graph)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(parents)
print(costs)

