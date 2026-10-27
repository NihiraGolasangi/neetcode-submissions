class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1]*n

        def find(component):
            ans = component

            while parents[ans]!= ans:
                
                parents[ans]= parents[parents[ans]]
                ans = parents[ans]
            return ans
     


        def union(c1, c2):
            p1 = find(c1)
            p2 = find(c2)

            if p1==p2:
                return 0
            
            if size[p1]>size[p2]:
                parents[p2]=p1
                size[p1]+= size[p2]
            else:
                parents[p1]=p2
                size[p2]+= size[p1]
            return 1 


        res = n
        for i,j in edges:
            res-=union(i,j)
        return res

        