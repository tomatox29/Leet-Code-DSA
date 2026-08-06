class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = {}
        for i in range(n):
            graph[i] = []

        for u, v in invocations:
            graph[u].append(v)

        visited = set()

        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
        dfs(k)
        for u,v in invocations:
            if u not in visited and v in visited:
                return list(range(n))
        ans=[]
        for i in range(n):
            if i not in visited:
                ans.append(i)
        return ans 
