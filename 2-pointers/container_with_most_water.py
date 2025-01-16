'''
Given an integer input array heights representing the heights of vertical lines, write a function that returns the maximum area of water that can be contained by two of the lines (and the x-axis). The function should take in an array of integers and return an integer.
Brute force: Find out all combinations of two lines and calculate the area. Return the maximum area. Time complexity: O(n^2)
Optimal: Use two pointers. Start with the first and last lines. Calculate the area. Move the pointer with the smaller height. Repeat the process until the pointers meet. Time complexity: O(n)
'''
def max_area(heights):
    if not heights:
        return 0
    
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area, min(heights[left], heights[right]) * (right - left))
        if heights[left] < heights[right]:
            left+=1
        else:
            right-=1

    return max_area
