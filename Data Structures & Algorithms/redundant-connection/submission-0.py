class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(c):
            ans = c
            while parent[ans]!=ans:
                parent[ans]= parent[parent[ans]]
                ans = parent[ans]
            return ans

        def union(c1,c2):
            p1 = find(c1)
            p2=find(c2)

            if p1==p2:
                return 0
            
            parent[p1]=p2
            return 1
        
        for i,j in edges:
            if not union(i,j):
                return [i,j]
        return [-1,-1]


        