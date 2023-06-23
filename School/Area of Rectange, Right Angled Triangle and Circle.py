Link : https://practice.geeksforgeeks.org/problems/area-of-rectange-right-angled-triangle-and-circle2600/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def getAreas(self, L , W , B , H , R):
        area_of_rectangle = L * W
        area_of_triangle = 0.5 * B * H
        area_of_circle = 3.14 * (R * R)
        return area_of_rectangle, int(area_of_triangle), int(area_of_circle)
        

# Driver Code Starts
# Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,W,B,H,R=map(int,input().split())     
        ob = Solution()
        ptr = ob.getAreas(L,W,B,H,R)      
        print(ptr[0],ptr[1],ptr[2])

# Driver Code Ends
