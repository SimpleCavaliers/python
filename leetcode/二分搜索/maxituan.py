#https://leetcode-cn.com/problems/circus-tower-lcci/
'''
源码:(要用等号自己敲一下)
def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x < a[mid]: hi = mid
        else: lo = mid+1
    return lo
'''
import bisect
def bestSeqAtIndex(self, height, weight) -> int:
        order_height = sorted(range(len(height)),key= lambda d:(height[d],-weight[d]))
        dp = [weight[order_height[0]]]
        for i in range(1,len(order_height)):
            #严格单调递增(不严格就是>=)
            get_num = weight[order_height[i]]
            if weight[order_height[i]] > dp[-1]:
                dp.append(get_num)
            else:
                '''
                pos = bisect.bisect_right(dp,get_num)
		        if dp[pos-1]!=get_num:
                    dp[pos] = get_num
                '''
                L,R = 0,len(dp)-1
                while L < R:
                    mid = (L+R)//2
                    if dp[mid] < weight[order_height[i]]:
                        L = mid+1
                    else:
                        R = mid
                dp[L] = get_num
        return len(dp)
