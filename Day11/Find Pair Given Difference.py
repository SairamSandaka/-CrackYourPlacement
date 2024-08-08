from typing import List


class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        # code here
        seen = set()
        for i in arr:
            if(i+x in seen or i-x in seen):
                return 1
            seen.add(i)
        return -1
