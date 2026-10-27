class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def find(component):
            ans = component

            while parents[ans]!= ans:
                ans = parents[ans]
            return ans
     


        def union(c1, c2):
            p1 = find(c1)
            p2 = find(c2)

            if p1==p2:
                return 0
            
            parents[p2]=p1
            return 1 


        res = n
        for i,j in edges:
            res-=union(i,j)
        return res

        