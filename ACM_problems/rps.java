/* 2009 Problem F
 * Rock, Paper, Scissors
 * 
 * By Cyrus Xi.
 */

import java.io.*;
import java.util.*;

class rps {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("rps.in"));
        String line;
        String secondLine;

        line = "";
        int length;
        char p1;
        char p2;
        int p1wins;
        int p2wins;

        while (true) {
            line = scanner.nextLine();
            secondLine = scanner.nextLine();
            // Input file ends on "E" and "E" won't otherwise appear.
            if (line.equals("E")) {
                break;
            }
            p1wins = 0;
            p2wins = 0;
            length = line.length();
            for (int i = 0; i < length; ++i) {
                p1 = line.charAt(i);
                p2 = secondLine.charAt(i);
                if (p1 == 'R') {
                    if (p2 == 'S') {
                        p1wins++;
                    }
                    else if (p2 == 'P') {
                        p2wins++;
                    }
                }
                else if (p1 == 'S') {
                    if (p2 == 'P') {
                        p1wins++;
                    }
                    else if (p2 == 'R') {
                        p2wins++;
                    }
                }
                // p1 == 'P'
                else {
                    if (p2 == 'R') {
                        p1wins++;
                    }
                    else if (p2 == 'S') {
                        p2wins++;
                    }
                }
            }
            System.out.printf("P1: %d\n", p1wins);
            System.out.printf("P2: %d\n", p2wins);
        }
    }
}

