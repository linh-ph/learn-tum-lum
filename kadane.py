# find a non-empty subarray with the largest sum
#return the left and right index of the max subarray sum
# assuming there's exactly one result 
# Sliding window variation of O(n)

def slidingWindow(arr):
    maxSum = arr[0]
    curSum = 0
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(arr)):
        if curSum < 0:
            curSum = 0
            L = R
        
        curSum += arr[R]
        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R
        
    return [maxL, maxR, maxSum]


arr = [3,-10,4,2,1,3,5]
print(slidingWindow(arr))
