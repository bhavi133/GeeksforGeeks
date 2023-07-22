Link : https://practice.geeksforgeeks.org/problems/median-of-2-sorted-arrays-of-different-sizes/1?page=3&status[]=unsolved&category[]=Arrays&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def MedianOfArrays(self, array1, array2):
        array3 = sorted(array1 + array2)
        if len(array3) % 2 == 1:
            return array3[len(array3) // 2]
        else:
            median1 = array3[len(array3) // 2]
            median2 = array3[(len(array3) // 2) - 1]
            result = ((median1 + median2) / 2)
            if str(result)[-1] == '0':
                return int(result)
            else:
                return result
            

# Driver Code Starts

if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# Driver Code Ends
