/* 2009 Problem I
 * The History of the Sith Rulers.
 * 
 * By Cyrus Xi.
 */

import java.io.*;
import java.util.*;

class i {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("i.in"));

        // Number of rulers.
        int n;
        n = scanner.nextInt();
        // Consume newline.
        scanner.nextLine();

        String name;
        double firstYr;
        double lastYr;
        int firstYear;
        int lastYear;

        ArrayList<String> rulers = new ArrayList<String>();
        HashMap<Integer, ArrayList<String>> mapping = new
                HashMap<Integer, ArrayList<String>>();

        for (int i = 0; i < n; ++i) {
            name = scanner.nextLine();
            firstYr = scanner.nextDouble();
            lastYr = scanner.nextDouble();

            // Consume newline token.
            scanner.nextLine();

            // Converts doubles to ints and rounds down.
            firstYear = (int) firstYr;
            lastYear = (int) lastYr;

            // Array of rulers in that year.
            ArrayList<String> temp;

            for (int j = firstYear; j <= lastYear; ++j) {
                // Add year:ruler mapping.
                if (mapping.containsKey(j)) {
                    // If contains year, add new name to value array.
                    mapping.get(j).add(name);
                }
                else {
                    // Else, create new array and map to year.
                    temp = new ArrayList<String>();
                    temp.add(name);
                    mapping.put(j, temp);
                }
            }
        }

        // Now do output.

        int yearEntries = scanner.nextInt();
        // Consume newline.
        scanner.nextLine();

        int year;
        ArrayList<String> printTemp = new ArrayList<String>();

        for (int k = 0; k < yearEntries; ++k) {
            year = scanner.nextInt();
            scanner.nextLine();
            // If no mapping, print None.
            if (!mapping.containsKey(year)) {
                System.out.println("None");
            }
            else {
                printTemp = mapping.get(year);
                String rulerName;
                // Instead of foreach to get formatting right.
                for (int q = 0; q < printTemp.size(); q++) {
                    rulerName = printTemp.get(q);
                    // Comma after unless last one in list.
                    if (q != (printTemp.size() - 1)) {
                        System.out.printf("%s, ", rulerName);
                    }
                    else {
                        System.out.printf("%s", rulerName);
                    }
                }
                System.out.println();
            }
        }

    }
}

