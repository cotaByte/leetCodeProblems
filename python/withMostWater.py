"""
You are given an integer array height of length n. There are n vertical lines drawn
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container
contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.


Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


def maxArea(height):
    max_volume = 0
    l, r = 0, len(height)-1
    while (l <= r):
        current_volume = ((r-l) * min(height[l], height[r]))
        print(f"Current volume of the iteration {current_volume}")
        max_volume = max(max_volume, current_volume)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return max_volume


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [2, 3, 4, 5, 18, 17, 6]
max = maxArea(height)
print(f"The max volume possible is {max}")
