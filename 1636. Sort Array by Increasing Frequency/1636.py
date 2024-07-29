class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequencies = dict()
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        #return sorted(nums, key=lambda x:(frequencies[x], -x))
        return sorted(sorted(nums, reverse=True), key=lambda x: frequencies[x])