Link : https://practice.geeksforgeeks.org/problems/remove-vowels-from-string1446/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

# User function Template for python3

class Solution:
	def removeVowels(self, S):
	    vowels = list('aeiou')
	    l = []
        for i in S:
            if i not in vowels:
                l.append(i)
        return ''.join(l)
                
 
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()	
		ob = Solution()	
		answer = ob.removeVowels(s)
		print(answer)
    
# Driver Code Ends
