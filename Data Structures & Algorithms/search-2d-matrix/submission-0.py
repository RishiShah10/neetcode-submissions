class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        could we binary search the lists themselves so find the middle of the list so row 2, check min max and if target in that range
        if so bs that row
        else move l and find middle row between l and r right
        """
        lRow,rRow = 0,len(matrix) - 1
        columns = len(matrix[0]) - 1
        def binarySearch(nums, target):
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return False
        while lRow <= rRow:
            mRow = (rRow + lRow) // 2
            if matrix[mRow][0] <= target <= matrix[mRow][columns]:
                return binarySearch(matrix[mRow], target)
            elif matrix[mRow][0] > target:
                rRow = mRow - 1
            else:
                lRow = mRow + 1
        return False