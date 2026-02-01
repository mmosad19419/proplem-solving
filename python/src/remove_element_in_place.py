from typing import List

def remove_element(nums: List[int], val: int) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indx = 0
        for element in nums:
            if element != val:
                nums[indx] = element
                indx +=1
        return indx, nums