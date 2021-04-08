class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        output = []
        for i in range(length - 1):
            print("lists: ", nums1, nums2)
            print("output: ", output)
            if len(nums1) > 0 and len(nums2) > 0:
                if nums1[0] <= nums2[0]:
                    output.append(nums1.pop())
                elif nums1[0] > nums2[0]:
                    output.append(nums2.pop())
            elif len(nums1) > 0:
                output.append(nums1.pop())
            elif len(nums2) > 0:
                output.append(nums2.pop())
        print(output)
        return float(1)
