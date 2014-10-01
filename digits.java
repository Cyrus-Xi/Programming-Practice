/* MCPC 2012 Problem B
 * Digit Solitaire.
 * By Daniel Graham, David Newton, & Cyrus Xi.
 */

import java.io.*;
import java.util.*;

class digits {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner scanner = new Scanner(new File("digits.in"));
		int nextInt;
		nextInt = scanner.nextInt();
		
		// '0' marks end of input.
		while(nextInt != 0) {
			outputCalculatedValue(nextInt);
			System.out.print("\n");
			nextInt = scanner.nextInt();
		}
	}
	
	// Recursive method.
	static void outputCalculatedValue(int currVal) {
		String valStr = "" + currVal;
		int currInt;
		int product = 1;
		Character currChar;
		
		// Check that currVal is not a single digit.
		// Else, end.
		if (currVal >= 10) {
			for (int i = 0; i < valStr.length(); i++) {
				currChar = (Character)valStr.charAt(i);
				currInt = Character.getNumericValue(currChar);
				product *= currInt;
			}
			System.out.print(currVal + " ");
			outputCalculatedValue(product);
		}
		else {
			System.out.print(currVal);
		}
	}
}
			
