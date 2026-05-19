class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = set()

        for i in nums:
            if i in store:
                return i
            store.add(i)

        return -1