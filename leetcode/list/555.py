class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        count = 0
        if K == 0:
            return 0
        for i in xrange(len(A)):
            if i == (len(A)-1):
                if A[-1] % K == 0:
                    count = count + 1 
            else:
                for j in xrange(i+1,(len(A)+1)):
                    if sum(A[i:j]) % K == 0:
                        count = count + 1 
        return count