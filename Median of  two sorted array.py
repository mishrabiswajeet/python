class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        finalarray=[]
        nums1.extend(nums2)
        finalarray.extend(nums1)
        finalarray.sort()
        poco=len(finalarray)
        if poco==1:
            return finalarray[0]
        mid = poco//2
        if poco%2==0:
            median=(finalarray[mid-1]+finalarray[mid])/2
            return float(median)
        else:
            return float(finalarray[mid])
