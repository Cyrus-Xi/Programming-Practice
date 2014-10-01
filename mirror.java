/* 2010 Problem E: Mirror, Mirror on the Wall.
 * Take list of votes and determine outcome.
 * 
 * By David Newton and Cyrus Xi.
 */

import java.io.*;
import java.util.*;

public class mirror {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner scanner = new Scanner(new File("mirror.in"));
		String line;

		line = scanner.nextLine();
		
		// '#' marks end of input.
		while(!line.equals("#")) {
			int lineLength = line.length();
			char currChar;
			String result = "";
			
			boolean breakLoop = false;
			
			for (int i = lineLength - 1; i >= 0; --i) {
				if (breakLoop) {
					break;
				}
				currChar = line.charAt(i);
				switch (currChar) {
					case 'b':
						result += "d";
						break;
					case 'd':
						result += "b";
						break;
					case 'p':
						result += "q";
						break;
					case 'q':
						result += "p";
						break;
					case 'i':
					case 'o':
					case 'v':
					case 'w':
					case 'x':
						result += Character.toString(currChar);
						break;
					default:
						result = "INVALID";
						breakLoop = true;
						break;
					}
				
			}
			System.out.println(result);
			line = scanner.nextLine();
		}
	}
}
			
			
