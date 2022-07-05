class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # create adjancency list to map each source to its destination
        adjacencyList = {source: [] for source,destination in tickets}
        
        tickets.sort() # sort the tickets in lexical order
        #populate the adjacency list
        for source, destination in tickets:
            adjacencyList[source].append(destination)
        #create resulting list with 'JFK' because we always start from 'JFK'
        result = ['JFK']
        
        # DFS function to recurse and backtrack through the tickets array
        def dfs(source):
            # a solution is found when the resulting array is equal to the length of tickets + 1
            if len(result) == len(tickets) + 1:
                return True
            
            # if the source is not in the adjacency list, we return False
            if source not in adjacencyList:
                return False
            
            # create a temporary list to store the list incase we need a node back and iterate through the copy of the list
            temp = list(adjacencyList[source])
            print(temp)
            for i, v in enumerate(temp):
                adjacencyList[source].pop(i) # when we visit a node we pop the node
                result.append(v) # add the destination to our result
                
                # now we run a dfs on the destination(v)
                if dfs(v): return True
                
                # if the destination does not lead to another destination and we still have nodes left, we have to backtrack
                adjacencyList[source].insert(i,v)
                result.pop()
                # if we don't find a solution we return False
            return False
        dfs("JFK")
        return result