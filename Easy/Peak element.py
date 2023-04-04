Link : https://practice.geeksforgeeks.org/problems/peak-element/1?page=1&status[]=bookmarked&sortBy=submissions

Code :

class Solution:   
    def peakElement(self,arr, n):
        # for i in range(n-1, 0, -1):
        #     if arr[i] > arr[i-1]:
        #         return i
        # else:
        #     return 0
            
        return arr.index(max(arr))


# Driver Code Starts

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False
        if flag:
            print(1)
        else:
            print(0)

# Driver Code Ends
