/* 2014 Practice: Problem A
 * The Navi-Computer is Down!
 * 
 * By David Newton & Cyrus Xi.
 */

import java.io.*;
import java.util.*;

class a {
	public static void main(String[] args) throws FileNotFoundException {
		Scanner scanner = new Scanner(new File("a.in"));
		
		// Number of entries.
		int n;
		n = scanner.nextInt();
		
		// Consume the newline.
		scanner.nextLine();
		
		// Galaxy coordinates.
		double x1;
		double y1;
		double z1;
		
		double x2;
		double y2;
		double z2;
		
		double distance;
		
		// Galaxy names.
		String start;
		String end;
		
		for (int i = 0; i < n; i++) {
			start = scanner.nextLine();
			x1 = scanner.nextDouble();
			y1 = scanner.nextDouble();
			z1 = scanner.nextDouble();
			scanner.nextLine();
			
			end = scanner.nextLine();
			x2 = scanner.nextDouble();
			y2 = scanner.nextDouble();
			z2 = scanner.nextDouble();
			scanner.nextLine();
			
			// Get 3d distance.
			distance = Math.sqrt( Math.pow( (x1 - x2), 2) + 
					Math.pow( (y1 - y2), 2) + Math.pow((z1 - z2), 2 ) );
			
			System.out.printf("%s to %s: %.2f\n", start, end, distance);
		}
	}
}
			
