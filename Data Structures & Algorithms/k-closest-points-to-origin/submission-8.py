class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        extended = []
        distance = []
        for x in points:
            d = (x[0]**2 + x[1]**2) ** 0.5 # no need to actually implement sqrt, as we only need to compare
            d = x[0]**2 + x[1]**2
            distance.append(d)
            extended.append([x, d])
        
        heapq.heapify(distance)
        top_k = []
        while len(top_k) < k:
            top_k.append(heapq.heappop(distance))
        
        res = []
        for y in extended:
            if y[1] in top_k:
                res.append(y[0])
        return res

        