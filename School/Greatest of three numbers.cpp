Link : https://practice.geeksforgeeks.org/problems/greatest-of-three-numbers2520/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// User function Template for C++

class Solution {
  public:
    int greatestOfThree(int A, int B, int C) {
        if (A > B && A > C){
            return A;
        }
        else if (B > A && B > C){
            return B;
        }
        else{
            return C;
        }
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int A, B, C;
        cin >> A >> B >> C;
        Solution ob;
        cout << ob.greatestOfThree(A, B, C) << "\n";
    }
}
