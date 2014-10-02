/* 2010 Problem C: Voting.
 * 
 * Take list of votes and determine outcome.
 */

import java.io.*;
import java.util.*;

public class voting {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("voting.in"));
        String line;

        line = scanner.nextLine();
        
        // '#' marks end of input.
        while(!line.equals("#")) {
            int lineLength = line.length();
            char currChar;
            int numAbsent = 0;
            int numYes = 0;
            int numNo = 0;
            
            // Count number of yes & no votes, along with absentees.
            for (int i = 0; i < lineLength; ++i) {
                currChar = line.charAt(i);
                switch (currChar) {
                    case 'Y':
                        numYes++;
                        break;
                    case 'N':
                        numNo++;
                        break;
                    case 'A':
                        numAbsent++;
                        break;
                    default:
                        break;
                }
            }
            // Not enough people present.
            if (numAbsent >= (lineLength/2.0)) {
                System.out.println("need quorum");  
            }
            else {
                if (numYes > numNo) {
                    System.out.println("yes");
                }
                else if (numNo > numYes) {
                    System.out.println("no");
                }
                // Equal number of yes and no votes.
                else {
                    System.out.println("tie");
                }
            }
            line = scanner.nextLine();
        }
    }
}
            
            
