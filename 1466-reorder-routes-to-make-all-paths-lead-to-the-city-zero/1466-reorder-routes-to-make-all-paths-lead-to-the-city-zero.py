class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # no loops and a connected graph
        # start at 0, recursively check neighbors, count outgoing edges
        
        edges = { (a,b) for a,b in connections}
        neighbors = { city:[] for city in range(n)}
        visit = set()
        changes = 0

        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        
        visit.add(0)
        dfs(0)
        return changes

        