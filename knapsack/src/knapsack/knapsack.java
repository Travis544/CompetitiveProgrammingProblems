package knapsack;

import java.io.*;
import java.util.*;
import java.math.*;

public class knapsack {

    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        String line = "";
        while ((line = in.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
//            c is capacity of knapsack
            int c = Integer.parseInt(st.nextToken());
//            n is number of objects
            int n = Integer.parseInt(st.nextToken());
            int[] wt = new int[n];
            int[] v = new int[n];
            for (int i = 0; i < n; i++) {
            	
                st = new StringTokenizer(in.readLine());
                v[i] = Integer.parseInt(st.nextToken());
                wt[i] = Integer.parseInt(st.nextToken());
            }
            
            
            int[][] dp = new int[n + 1][c + 1];
            for (int i = 0; i < dp.length; i++)
                Arrays.fill(dp[i], -1);
            for (int i = 0; i <= n; i++) {
                for (int w = 0; w <= c; w++) {
//                	first row is all zeros.
                    if (i == 0  || w == 0)
                        dp[i][w] = 0;
//                    if current item's
                    else if (wt[i - 1] <= w)
                        dp[i][w] = Math.max(dp[i - 1][w], v[i - 1] + dp[i - 1][w - wt[i - 1]]);
                    else
                        dp[i][w] = dp[i - 1][w]; 
                }
            }
            
//            System.out.println(Arrays.toString(dp[0]));
//            System.out.println("SSS");
           // System.out.println(Arrays.toString(dp[n]));
//            out.println(dp[n - 1][c]);
            int temp = c;
            ArrayList<Integer> indices = new ArrayList<Integer>();
            for(int i = n; i > 0; i--) {
                if(dp[i][temp] != dp[i - 1][temp]) {
//                	since first item has index 0, we need to do i-1 for i. 
                    indices.add(i - 1);
                    temp -= wt[i - 1];
                }
                
                System.out.println(i);

            }
            out.println(indices.size());
            for(int i : indices)
                out.print(i + " ");
            out.println();
            break;
        }
        out.close();
    }
}