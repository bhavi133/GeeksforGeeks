Link : https://practice.geeksforgeeks.org/problems/arranging-the-array1131/1?page=3&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

from typing import List

class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        positive_list = []
        negative_list = []
        for i in arr:
            if i >= 0:
                positive_list.append(i)
            else:
                negative_list.append(i)
        nums = negative_list + positive_list 
        for i in range(n):
            arr[i] = nums[i]
        return arr

 
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):       
        n = int(input())
        arr=IntArray().Input(2)
        obj = Solution()
        obj.Rearrange(n, arr)
        print(*arr, end=' ')
        print()

# Driver Code Ends
