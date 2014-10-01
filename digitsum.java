/* 2013 Problem F: Digit Sum.
 * What is the smallest possible sum of two numbers that together use 
 * the N numerals provided?
 */

import java.io.*;
import java.util.*;

class digitsum {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner scanner = new Scanner(new File("digitsum.in"));
		String line;
		String strN;
		int N;  // Number of numerals included.
		int[] nums;  // Array of all numerals.
		line = scanner.nextLine();
		
		// '0' marks end of input.
		while(!line.equals("0")) {
			strN = "" + line.charAt(0);
			
			if (line.charAt(1) != ' ') {
				strN += line.charAt(1);
			}
			N = Integer.valueOf(strN); 
			
			nums = new int[N];
			
			for (int i = 0; i < N; i++) {
				// A space between each numeral.
				if (N > 9) {
					nums[i] = line.charAt(3 + 2*i) - '0';
				}
				else {
					nums[i] = line.charAt(2 + 2*i) - '0';
				}				
			}
			Arrays.sort(nums);
			
			String num1 = "";
			String num2 = "";
			
			for (int j = 0; j < N; j++) {
				int i = 0;
				int newNum = nums[j];
				//System.out.println(newNum);
				if (newNum == -1) continue;
				
				// To handle the special case where there's only one
				// 0.
				if (j % 2 == 0 && (num1.length() - num2.length() < 2)) {
					// 0 can't be first digit.
					if (num1 == "" && newNum == 0) {
						i = j;
						while (nums[i] == 0 || nums[i] == -1) {
							i++;
						}
						//System.out.println(i);
						num1 += nums[i];
						nums[i] = -1;
						num1 += 0; // Concatenate 0 back in.
					}
					else {
						num1 += newNum;
						//System.out.println(num1);
					}
				}
				else {
					if (num2 == "" && newNum == 0) {
						i = j;
						while (nums[i] == 0 || nums[i] == -1) {
							i++;
						}
						num2 += nums[i];
						nums[i] = -1;
						num2 += 0;
					}
					else {
						num2 += newNum;
						//System.out.println(num2);
					}
				}
			}
			//System.out.println(N);
			//System.out.println(num1);
			//System.out.println(num2);
			int number1 = Integer.valueOf(num1);
			int number2 = Integer.valueOf(num2);
			System.out.println(number1 + number2);
			line = scanner.nextLine();
		}
	}
}
			
			
