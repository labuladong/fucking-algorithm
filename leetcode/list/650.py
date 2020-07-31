class Solution:
    def subarraySum(self, nums, k):
        import collections
        pre_sum_times = collections.defaultdict(int)
        pre_sum_times[0] = 1  ## it is need ,
        pre_sum, count= 0, 0
        for i in xrange(len(nums)):
            pre_sum = pre_sum + nums[i]
            if pre_sum - k in pre_sum_times:
                count = count + pre_sum_times[pre_sum - k]
            pre_sum_times[pre_sum] += 1
        return count


        