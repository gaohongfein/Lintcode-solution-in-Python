'''
Find K-th largest element in N arrays.

Notice
You can swap elements in the array

Have you met this question in a real interview? Yes
Example
In n=2 arrays [[9,3,2,4,7],[1,2,3,4,8]], the 3rd largest element is 7.
In n=2 arrays [[9,3,2,4,8],[1,2,3,4,2]], the 1st largest element is 9,
2nd largest element is 8, 3rd largest element is 7 and etc.
'''
from heapq import heappop, heappush
class Solution:

    """
    @param: arrays: a list of array
    @param: k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    # def KthInArrays(self, arrays, k):
