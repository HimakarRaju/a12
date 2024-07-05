"""
Name : HimakarRaju Gunda
Date : 03-07-2024
Trainer Name : Saynam

Description of program :
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are(i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""


def max_area(height):
    m_area = 0
    h1 = 0
    h2 = len(height) - 1
    while h1 < h2:
        area = min(height[h1], height[h2]) * (h2 - h1)
        m_area = max(m_area, area)
        if height[h1] < height[h2]:
            h1 += 1
        else:
            h2 -= 1
    return m_area


"""
FOR REFERENCE PURPOSE :
def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        H = max(height)

        while left < right:
            W = (right - left)

            if H*W < maxArea:
                return maxArea
            
            currentArea = min(height[left], height[right]) * W
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
"""

h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(h))

h = [1, 1]
print(max_area(h))
