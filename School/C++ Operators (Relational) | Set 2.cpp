Link : https://practice.geeksforgeeks.org/problems/c-operators-relational-set-21407/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

#include<bits/stdc++.h> 
using namespace std; 

class Solution{   
public:
    string compareNum(int A,int B){
        if (A > B){
            cout << A << " is greater than " << B;
        }
        else if (A == B){
             cout << A << " is equals to " << B;   
        }
        else{
             cout << A << " is less than " << B;
        }
    }
};

int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int A,B;
        cin >> A>>B;
        Solution ob;
        cout << ob.compareNum(A,B) << endl;
    }
    return 0; 
} 
