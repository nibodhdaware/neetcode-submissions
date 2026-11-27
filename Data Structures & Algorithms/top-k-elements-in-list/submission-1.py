from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        top_k = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
        return list(top_k)[:k]