Link : https://practice.geeksforgeeks.org/problems/java-arrays-set-11354/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=difficulty

Code :

class Compute
{
    String average(int A[], int N)
    {
        int i;
        float sum = 0, avg;
        for (i = 0; i < N; i++)
        {
            sum = sum + A[i];
        }
        avg = sum / N;
        return String.format("%.2f", avg);
    }
}
