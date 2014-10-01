/* 2010 Problem A: Judges' Time Calculation.
 * Output table to determine elapsed time for submissions.
 * 
 * By Daniel Graham, David Newton and Cyrus Xi.
 */

import java.io.*;
import java.util.*;

public class calc {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner scanner = new Scanner(new File("calc.in"));
		String line;
		int N = scanner.nextInt();
		int startHr;
		int startMin;
		int durationHr;
		int durationMin;
		
		// N is number of cases.
		for (int i = 0; i < N; ++i) {
			startHr = scanner.nextInt();
			startMin = scanner.nextInt();
			durationHr = scanner.nextInt();
			durationMin = scanner.nextInt();
			//System.out.printf("%d %d %d %d\n", startHr, startMin, 
							//durationHr, durationMin);
			System.out.println("------+---------");
			System.out.println(" time | elapsed ");
			System.out.println("------+---------");
			if (startMin != 0) {
				System.out.printf("%2d:XX | XX - %-2d\n", startHr, 
									startMin);
			} else {
				System.out.printf("%2d:XX | XX\n", startHr);
			}
			int numHrs = durationHr;
			if ( (startMin + durationMin) >= 60 ) {
				numHrs++;
			}
			int realHr = startHr;
			boolean isPastTwelve = false;
			for (int j = 1; j <= numHrs; ++j) {
				realHr++;
				if (realHr > 12) {
					isPastTwelve = true;
				}
				if (isPastTwelve) {
					realHr -= 12;
					isPastTwelve = false;
				}
				System.out.printf("%2d:XX | XX + %-2d\n", 
								realHr, j*60 - startMin);
			}
		}
	}
}
			
			
