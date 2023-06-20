Link : https://practice.geeksforgeeks.org/problems/java-operatorsrelational-set-22338/1?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

Code :

class Solution{
    static void relationalOperators(int A,int B){
        if (A > B){
            System.out.println(A + " is greater than " + B);
        }
        else if (A == B){
            System.out.println(A + " is equals to " + B);
        }
        else{
            System.out.println(A + " is less than " + B);
        }
    }
}
