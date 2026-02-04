class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lmax=[0]*n
        rmax=[0]*n
        count=0
        lmax[0]=height[0]
        rmax[n-1]=height[n-1]
        for i in range (1,n):
            lmax[i]=max(lmax[i-1],height[i])
        for i in range (n-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i])
        for i in range (1,n):
            count+=min(lmax[i],rmax[i])-height[i]
        return count