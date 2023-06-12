Link : https://practice.geeksforgeeks.org/problems/precise-fomat-java/1?page=4&difficulty[]=0&status[]=unsolved&sortBy=submissions

Code :

// Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

// Driver Code Ends
// User function Template for Java

class Geeks{
    static void printInFormat(float a, float b){
        float result = a/b;
        System.out.format("%.7f", result);
        System.out.format(" %.3f", result);
    }    
}

// Driver Code Starts.

class GFG {
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		int testcases = sc.nextInt();
		while(testcases-- > 0){
    		float a = sc.nextFloat();
    		float b = sc.nextFloat();
    		Geeks g = new Geeks();
    		g.printInFormat(a, b);
    		System.out.println();		
		}
	}
}

// Driver Code Ends
