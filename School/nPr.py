Link : https://practice.geeksforgeeks.org/problems/npr4253/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

import math

class Solution:
  
    def nPr(self, n, r):
        return math.factorial(n) // math.factorial(n-r)
