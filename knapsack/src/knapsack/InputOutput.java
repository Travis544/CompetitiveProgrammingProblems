package knapsack;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class InputOutput {
    private static int R, C;
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		 BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
		  String[] line = sc.readLine().split(" ");
		  R = Integer.parseInt(line[0]);
	      C = Integer.parseInt(line[1]);
	      for (int r = 0; r < R; r++) {
	          char[] d = sc.readLine().toCharArray();
	          for (char v : d) {
	        	  System.out.println(v);
	          }
	      }
	            	
	            
	}

}
