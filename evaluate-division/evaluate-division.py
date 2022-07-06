class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Note
        1. There is some sort of relationship between the equations resulting in a value
        2. The query will not result in zero division and there is no contradiction
        3. We can build new values from the equations by doing a reciprocal
        4. This is a graph problem and we can connect each equation node to another by computing its value. The graph is bi-directional
        5. We can use BFS or DFS for the problem but we'll use DFS here
        '''
        
        
        '''
        First, we build the graph, we use a defaultdict library to handle case of when there is no value in dict that gives error
        Next, we iterate though equations and values to populate graph using zip function
        '''
        graph = collections.defaultdict(dict)
        
        for (x,y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0/val
        
        def dfs(x,y,visited):
            if x not in graph or y not in graph:
                return -1.0
            
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                if i not in visited:
                    visited.add(i) # add i to visited set so it is marked and we won't re-visit
                    temp = dfs(i, y, visited) # holds the result of the dfs
                    if temp == -1:
                        continue # if we don't find a connection, we continue to for loop
                    else:
                        return graph[x][i] * temp # now that we found a value in our temp dfs solution, we multiply it with the node that hlped with connection
            return -1
        result = []
        '''
        The DFS function starts here
        
        The DFS function lets us know what nodes we have visited so we don't visit it another time. We use a set as it has faster lookup time.
        First condition is to check if x or y is in the graph, if not one or both we return -1
        Second condition is if there is a direct connection between the nodes, we return the connection value
        Third condition is if the connection between the two nodes can be found in another node, we go through all the nodes conneced to the current node and perform dfs on each node connected to that node
        to find if a connection exist.
        The dfs function call use a set that always refreshes and we add the value to our result
        
        '''        
        for query in queries:
            result.append(dfs(query[0], query[1],set()))
        return result