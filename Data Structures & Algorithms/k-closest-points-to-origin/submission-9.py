class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # # --- Method too complicated; no need to construct distance list separately ---
        # extended = []
        # distance = []
        # for x in points:
        #     d = (x[0]**2 + x[1]**2) ** 0.5 # no need to actually implement sqrt, as we only need to compare
        #     d = x[0]**2 + x[1]**2
        #     distance.append(d)
        #     extended.append([x, d])
        
        # heapq.heapify(distance)
        # top_k = []
        # while len(top_k) < k:
        #     top_k.append(heapq.heappop(distance))
        # res = []
        # for y in extended:
        #     if y[1] in top_k:
        #         res.append(y[0])
        # return res

        # --- Method 2: more efficient in code, but same time complexity ---
        points_ext = []
        for x, y in points:
            d_sq = x**2 + y**2
            points_ext.append([d_sq, x, y])
        heapq.heapify(points_ext)
        res = []
        while len(res) < k:
            d_sq, x, y = heapq.heappop(points_ext)
            res.append([x, y])
        return res

            

        