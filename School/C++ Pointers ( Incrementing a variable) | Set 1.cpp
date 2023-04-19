Link : https://practice.geeksforgeeks.org/problems/c-pointers-set-1introduction/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

// Driver Code Starts

#include<iostream>
using namespace std;
void updateVar(int *a);

int main()
{
    int t;
    cin>>t;
    while(t--)
    {   int a;
        cin>>a;
        updateVar(&a);
        cout<<a<<"\n";
    }
    return 0;
}

// Driver Code Ends

void updateVar(int *a)
{
      (*a) += 10;
}
