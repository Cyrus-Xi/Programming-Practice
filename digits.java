/* 2012 Problem B: Digit Solitaire.
 * 
 * "We start with a positive integer S. So long as it has more than one digit, 
 * we compute the product of its digits and repeat. For example, if starting 
 * with 95, we compute 9 × 5 = 45. Since 45 has more than one digit, we 
 * compute 4 × 5 = 20. Continuing with 20, we compute 2 × 0 = 0. Having 
 * reached 0, which is a single-digit number, the game is over."
 */

import java.io.*;
import java.util.*;

public class digits {
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
        if (currVal >= 10) {
            for (int i = 0; i < valStr.length(); i++) {
                currChar = (Character)valStr.charAt(i);
                currInt = Character.getNumericValue(currChar);
                product *= currInt;
            }
            System.out.print(currVal + " ");
            outputCalculatedValue(product);
        }
        // Else, end.
        else {
            System.out.print(currVal);
        }
    }
}

