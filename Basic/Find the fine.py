Link : https://practice.geeksforgeeks.org/problems/find-the-fine4353/1?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
    def totalFine(self, n, date, car, fine):
        # l = []
        # if date % 2 == 0:
        #     for i, j in zip(car, fine):
        #         if i % 2 == 1:
        #             l.append(j)
        #     return sum(l)
        # else:
        #     for i, j in zip(car, fine):
        #         if i % 2 == 0:
        #             l.append(j)
        #     return sum(l)
        
        # l = []
        # for i in range(len(car)):
        #     if date % 2 == 0:
        #         if car[i] % 2 == 1:
        #             l.append(fine[i])
        #     if date % 2 == 1:
        #         if car[i] % 2 == 0:
        #             l.append(fine[i])
        # return sum(l)
            
        l = []
        for i, j in zip(car, fine):
            if date % 2 == 0:
                if i % 2 == 1:
                    l.append(j)
            else:
                if i % 2 == 0:
                    l.append(j)
        return sum(l)
    

# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())
    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        print(Solution().totalFine( n, k, arr, brr))
        T -= 1

if __name__ == "__main__":
    main()

# Driver Code Ends
